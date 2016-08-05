"""
Description: This lookup takes an AWS region and a vpc
name and returns a matching VPC ID.
Example Usage:
{{ lookup('aws_vpc_id_from_name', 'eu-west-1', 'vpc1') }}
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
        region = terms[0]
        vpc_name = terms[1]
        vpc_conn = boto.vpc.connect_to_region(region)
        filters = {'tag:Name': vpc_name}
        vpc = vpc_conn.get_all_vpcs(filters=filters)
        if vpc and vpc[0]:
            return [vpc[0].id.encode('utf-8')]
        return None
