"""
Description: This lookup takes an AWS region and a list of one or more
security Group Names and returns a list of matching security Group IDs.
Example Usage:
{{ lookup('aws_secgroup_ids_from_names', 'eu-west-1', ['nginx_group', 'mysql_group']) }}
"""
from __future__ import (absolute_import, division, print_function)
from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase

__metaclass__ = type

try:
    import boto.vpc
except ImportError:
    raise AnsibleError("aws_vpc_id_from_name lookup cannot be run without boto installed")


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        if isinstance(terms, basestring):
            terms = [terms]
        region = terms[0]
        group_names = terms[1]
        conn = boto.ec2.connect_to_region(region)
        filters = {'group_name': group_names}
        sg = conn.get_all_security_groups(filters=filters)
        sg_list = [x.id.encode('utf-8') for x in sg]
        return sg_list
