"""
Description: This lookup takes params to lookup records from route53
name and returns a matching value parameter
Example Usage:
{{ lookup('aws_route53_get_value', 'E13IGA03V7VA8Q', 'CNAME' ,'www.voronenko.info') }}
"""
from __future__ import (absolute_import, division, print_function)
from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase
import os

import json


# class PrimitiveJSONEncoder(JSONEncoder):
#     def default(self, o):
#         return o.__dict__

if os.getenv('AWS_ACCESS_KEY_ID') is not None:
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']

if os.getenv('AWS_SECRET_ACCESS_KEY') is not None:
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']


__metaclass__ = type

try:
    import boto
    from boto import route53
except ImportError:
    raise AnsibleError("aws_route53_get_value lookup cannot be run without boto installed")


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        zoneid = terms[0]
        recordtype = terms[1]
        recordname = terms[2]
        r53conn = route53.connect_to_region('universal',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )
        records = r53conn.get_all_rrsets(zoneid,recordtype,recordname,maxitems=1)[0]
        recordvalue = records.resource_records[0]
        if recordvalue:
            return [recordvalue]
        return None
