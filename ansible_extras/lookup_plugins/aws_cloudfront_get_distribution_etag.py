"""
Description: This lookup takes cloud front distributionId
name and returns a matching etag needed to dismount distribution
Example Usage:
{{ lookup('aws_cloudfront_get_distribution_etag', 'E13IGA03V7VA8Q') }}
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
except ImportError:
    raise AnsibleError("aws_cloudfront_get_distribution_etag lookup cannot be run without boto installed")


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        distributionId = terms[0]
        cloudfront_conn = boto.connect_cloudfront(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
        distributionConfig = cloudfront_conn.get_distribution_config(distributionId)
        if distributionConfig:
#            zz = dir(distributionConfig)
            return [distributionConfig.etag]
        return None
