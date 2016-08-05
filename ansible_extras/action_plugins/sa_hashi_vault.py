#!/usr/bin/python
# This file is part of Ansible Developer Recipes
# https://github.com/Voronenko/ansible-developer_recipes

import os
from ansible.errors import AnsibleError
from ansible.plugins.action import ActionBase

__metaclass__ = type

ANSIBLE_HASHI_VAULT_ADDR = 'http://127.0.0.1:8200'

if os.getenv('VAULT_ADDR') is not None:
    ANSIBLE_HASHI_VAULT_ADDR = os.environ['VAULT_ADDR']

if os.getenv('VAULT_TOKEN') is not None:
    ANSIBLE_HASHI_VAULT_TOKEN = os.environ['VAULT_TOKEN']


class SaHashiVault:
    def __init__(self, logger=None, **kwargs):
        try:
            import hvac
        except ImportError:
            AnsibleError("Please pip install hvac to use this module")

        self.url = kwargs.get('url', ANSIBLE_HASHI_VAULT_ADDR)

        self.token = kwargs.get('token', ANSIBLE_HASHI_VAULT_TOKEN)
        if self.token is None:
            raise AnsibleError("No Vault Token specified")

        self.value = kwargs.get('value', None)

        # split secret arg, which has format 'secret/hello:value'
        # into secret='secret/hello' and secret_field='value'
        s = kwargs.get('secret')
        if s is None:
            raise AnsibleError("No secret specified")

        s_f = s.split(':')
        self.secret = s_f[0]
        if len(s_f) >= 2:
            self.secret_field = s_f[1]
        else:
            self.secret_field = 'value'

        self.client = hvac.Client(url=self.url, token=self.token)

        if self.client.is_authenticated():
            pass
        else:
            raise AnsibleError("Invalid Hashicorp Vault Token Specified")

    def get(self):
        data = self.client.read(self.secret)
        if data is None:
            raise AnsibleError("The secret %s doesn't seem to exist"
                               % self.secret)

        if self.secret_field == '':  # secret was specified with trailing ':'
            return data['data']

        if self.secret_field not in data['data']:
            raise AnsibleError("The secret %s does not contain the field '%s'."
                               % (self.secret, self.secret_field))

        return data['data'][self.secret_field]

    def write(self):
        if self.value is None:
            raise AnsibleError("Value is required for write operation")
        return self.client.write(self.secret, value=self.value)

    def delete(self):
        return self.client.delete(self.secret)


class ActionModule(ActionBase):
    ''' Write operations with hashicorp vault '''

    VALID_ARGS = set(['action', 'url', 'token', 'secret', 'value'])
    VALID_ACTIONS = set(['read', 'write', 'delete'])

    def run(self, tmp=None, task_vars=None):
        #  self._display.warning('This is how you can debug')

        module_args = dict()
        for arg in self._task.args:
            if arg not in self.VALID_ARGS:
                return {"failed": True, "msg": "'%s' is not a valid option in sa_hashi_vault" % arg}
            else:
                module_args[arg] = self._task.args.get(arg)

        if task_vars is None:
            task_vars = module_args.deepcopy(module_args)

        result = super(ActionModule, self).run(tmp, task_vars)
        result['_ansible_verbose_always'] = True

        action = self._task.args.get('action', 'read')

        vault_conn = SaHashiVault(self._display, **module_args)

        if action == 'read':
            result['value'] = vault_conn.get()
            result['changed'] = True
        elif action == 'write':
            result['status'] = vault_conn.write()
            result['changed'] = True
        elif action == 'delete':
            result['status'] = vault_conn.delete()
            result['changed'] = True
        else:
            return {"failed": True, "msg": "'%s' is not a valid action in sa_hashi_vault" % action}

        return result
