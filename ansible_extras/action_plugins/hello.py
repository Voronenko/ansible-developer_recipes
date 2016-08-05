#!/usr/bin/python
# This file is part of Ansible Developer Recipes
# https://github.com/Voronenko/ansible-developer_recipes

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action import ActionBase
from ansible.utils.unicode import to_unicode
from ansible.errors import AnsibleUndefinedVariable


class ActionModule(ActionBase):
    ''' Action plugin stub '''

    VALID_ARGS = set(['msg'])

    def run(self, tmp=None, task_vars=None):
        self._display.warning('This is how you can debug')
        if task_vars is None:
            task_vars = dict()
            for arg in self._task.args:
                if arg not in self.VALID_ARGS:
                    return {"failed": True, "msg": "'%s' is not a valid option in debug" % arg}
        result = super(ActionModule, self).run(tmp, task_vars)
        result['msg'] = "Hello World"
        # force flag to make debug output module always verbose
        result['_ansible_verbose_always'] = True

        return result
