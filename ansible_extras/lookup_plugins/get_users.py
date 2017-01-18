import json

import grp
import pwd
import spwd

from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase

DOCUMENTATION = """
---
module: get_users
short_description:
    - A module for gathering facts about Linux users.
description:
    - This module gathers facts about the Linux users and groups that exist
      on the system.
author: major@mhtx.net
refactored to lookup module: git@voronenko.info
"""

EXAMPLES = '''
    - set_fact: users={{ lookup('get_users', 'min_uid=0 max_uid=40000') }}
    - debug: var="{{users}}"

       "users": [
            {
                "dir": "/root"
                "gecos": "root",
                "gid": 0,
                "group": {
                    "gid": 0
                    "name": "root"
                    "passwd": "x"
                },
                "name": "root",
                "shadow": false,
                "shell": "/bin/bash",
                "uid": 0
            },
            {
                "dir": "/usr/sbin",
                "gecos": "daemon",
                "gid": 1,
                "group": {
                    "gid": 1,
                    "name": "daemon",
                    "passwd": "x"
                },
                "name": "daemon",
                "shadow": false,
                "shell": "/usr/sbin/nologin",
                "uid": 1
            },
            {
                "dir": "/bin",
                "gecos": "bin",
                "gid": 2,
                "group": {
                    "gid": 2,
                    "name": "bin",
                    "passwd": "x"
                },
                "name": "bin",
                "shadow": false,
                "shell": "/usr/sbin/nologin",
                "uid": 2
            }
            ]
'''

RETURN = '''
users:
    description: users matching arguments provided
    returned: success
    type: list
'''

def make_user_dict(user_record):
    """Create a dictionary of user attributes."""
    user_dict = {
        'name': user_record.pw_name,
        'uid': user_record.pw_uid,
        'gid': user_record.pw_gid,
        'gecos': user_record.pw_gecos,
        'dir': user_record.pw_dir,
        'shell': user_record.pw_shell,
        'group': make_group_dict(user_record.pw_gid),
        'shadow': make_shadow_dict(user_record.pw_name)
    }
    return user_dict


def make_group_dict(gid):
    """Create dictionary from group record."""
    try:
        group_record = grp.getgrgid(gid)
    except KeyError:
        return False

    group_dict = {
        'name': group_record.gr_name,
        'passwd': group_record.gr_passwd,
        'gid': group_record.gr_gid,
    }
    return group_dict


def make_shadow_dict(username):
    """Create a dictionary of user shadow password database attributes."""
    try:
        shadow_record = spwd.getspnam(username)
    except KeyError:
        return False

    shadow_dict = {
        'last_changed': shadow_record.sp_lstchg,
        'min_days': shadow_record.sp_min,
        'max_days': shadow_record.sp_max,
        'warn_days': shadow_record.sp_warn,
        'inact_days': shadow_record.sp_inact,
        'expire_days': shadow_record.sp_expire,
    }
    return shadow_dict



class LookupModule(LookupBase):
    def run(self, terms, variables, **kwargs):

        ret = []

        if not isinstance(terms, list):
            lookupTerms = [terms]
        else:
            lookupTerms = terms[0]

        for term in terms:
            params = lookupTerms.split(' ', 2)

        paramvals = {
            'min_uid': 0,
            'max_uid': 65535
        }

        try:
            for param in params:
                name, value = param.split('=')
                assert(name in paramvals)
                paramvals[name] = int(value)
        except (ValueError, AssertionError) as e:
            raise AnsibleError(e)

        try:
            # Get all of the users on the system into a list of dicts.
            # The 'pwd' module
            # returns them in a struct.
            all_users = [make_user_dict(x) for x in pwd.getpwall()]

            # Get the users that match our criteria.
            user_list = [x for x in all_users
                         if (x['uid'] >= paramvals['min_uid'] and
                             x['uid'] <= paramvals['max_uid'])]
        except Exception as e:
            raise AnsibleError("Postgres query error:" % e.message)

        finally:
            pass

#        jsonret = json.dumps([{users: user_list}], ensure_ascii=False)
        return user_list
