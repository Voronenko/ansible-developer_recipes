"""
Description: This lookup takes an AWS region and an s3 bucket name.
Example Usage:
{{ lookup('aws_s3_bucket_exists', 'bucketname') }}
"""
from __future__ import (absolute_import, division, print_function)
from ansible.errors import (AnsibleError, AnsibleLookupError)
from ansible.plugins.lookup import LookupBase
import os

__metaclass__ = type

if os.getenv('AWS_ACCESS_KEY_ID') is not None:
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']

if os.getenv('AWS_SECRET_ACCESS_KEY') is not None:
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

try:
    from boto.s3.connection import S3Connection
except ImportError:
    raise AnsibleError("aws_vpc_id_from_name lookup cannot be run without boto installed")


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        if isinstance(terms, basestring):
            terms = [terms]
        bucket_name = terms[0]
        conn = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
        bucket = conn.lookup(bucket_name)
        if bucket is None:
            raise AnsibleLookupError("Bucket %s not found" % bucket_name)
        return [bucket_name.encode('utf-8')]
