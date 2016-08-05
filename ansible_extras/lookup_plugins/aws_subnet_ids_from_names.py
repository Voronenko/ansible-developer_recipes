"""
Description: This lookup takes an AWS region and a list of one or more
subnet names and returns a list of matching subnet ids.
Example Usage:
{{ lookup('aws_subnet_ids_from_names', 'eu-west-1', ['subnet1', 'subnet2']) }}
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

    def run(self, terms, inject=None, **kwargs):
        if isinstance(terms, basestring):
            terms = [terms]
        subnet_ids = []
        region = terms[0]
        subnet_names = terms[1]
        vpc_conn = boto.vpc.connect_to_region(region)
        filters = {'tag:Name': subnet_names}
        subnets = vpc_conn.get_all_subnets(filters=filters)
        subnet_ids = [x.id.encode('utf-8') for x in subnets]
        return subnet_ids
