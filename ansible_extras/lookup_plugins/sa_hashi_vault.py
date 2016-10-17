from __future__ import (absolute_import, division, print_function)
import os
from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase

__metaclass__ = type

ANSIBLE_HASHI_VAULT_ADDR = 'http://127.0.0.1:8200'

if os.getenv('VAULT_ADDR') is not None:
    ANSIBLE_HASHI_VAULT_ADDR = os.environ['VAULT_ADDR']

if os.getenv('VAULT_TOKEN') is not None:
    ANSIBLE_HASHI_VAULT_TOKEN = os.environ['VAULT_TOKEN']


class SaHashiVault:
    def __init__(self, **kwargs):
        try:
            import hvac
        except ImportError:
            AnsibleError("Please pip install hvac to use this module")

        self.url = kwargs.get('url', ANSIBLE_HASHI_VAULT_ADDR)

        self.token = kwargs.get('token', ANSIBLE_HASHI_VAULT_TOKEN)
        if self.token is None:
            raise AnsibleError("No Vault Token specified")

        # split secret arg, which has format 'secret/hello:value'
        # into secret='secret/hello' and secret_field='value'
        s = kwargs.get('secret')
        if s is None:
            raise AnsibleError("No secret specified")

        self.default = kwargs.get('default', None)

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
            if not self.default is None:
                return self.default
            else:
                raise AnsibleError("The secret %s doesn't seem to exist"
                               % self.secret)

        if self.secret_field == '':  # secret was specified with trailing ':'
            return data['data']

        if self.secret_field not in data['data']:
            raise AnsibleError("The secret %s does not contain the field '%s'."
                               % (self.secret, self.secret_field))

        return data['data'][self.secret_field]


class LookupModule(LookupBase):
    def run(self, terms, variables, **kwargs):
        vault_args = terms[0].split(' ')
        vault_dict = {}
        ret = []

        for param in vault_args:
            try:
                key, value = param.split('=')
            except ValueError as e:
                raise AnsibleError("hashi_vault plugin needs key=value pairs, but received %s %s"
                                   % (terms, e.message))
            vault_dict[key] = value

        vault_conn = SaHashiVault(**vault_dict)

        for term in terms:
            key = term.split()[0]
            value = vault_conn.get()
            ret.append(value)

        if 'write_to_file' in vault_dict.keys():
            text_file = open(vault_dict['write_to_file'], "w")
            text_file.write(value)
            text_file.close()

        return ret
