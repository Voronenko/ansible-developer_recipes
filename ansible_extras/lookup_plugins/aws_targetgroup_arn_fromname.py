"""
https://github.com/Voronenko/ansible-developer_recipes/tree/master/ansible_extras
Description: This lookup takes an AWS region and a load balancer targetgroup name
name and returns a matching group arn
Example Usage:
{{ lookup('aws_targetgroup_arn_fromname', 'eu-west-1', 'groupname') }}
"""
from __future__ import (absolute_import, division, print_function)
from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase

__metaclass__ = type

try:
    import boto3
except ImportError:
    raise AnsibleError("aws_targetgroup_arn_fromname lookup cannot be run without boto3 installed")


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        region = terms[0]
        group_name = terms[1]
        client = boto3.client('elbv2', region)
        # client.describe_target_groups(Names=['killme']);
# {'ResponseMetadata': {'RetryAttempts': 0, 'HTTPStatusCode': 200, 'RequestId': '2aed4558-0444-11e8-a5bc-e55c047b3f92', 'HTTPHeaders': {'x-amzn-requestid': '2aed4558-0444-11e8-a5bc-e55c047b3f92', 'date': 'Sun, 28 Jan 2018 15:59:05 GMT', 'content-length': '1192', 'content-type': 'text/xml'}}, u'TargetGroups': [{u'HealthCheckPath': '/', u'HealthCheckIntervalSeconds': 30, u'VpcId': 'vpc-0364237b', u'Protocol': 'HTTP', u'HealthCheckTimeoutSeconds': 5, u'TargetType': 'instance', u'HealthCheckProtocol': 'HTTP', u'LoadBalancerArns': [], u'UnhealthyThresholdCount': 2, u'HealthyThresholdCount': 5, u'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-east-1:143579570832:targetgroup/killme/f91cfb9c919252a5', u'Matcher': {u'HttpCode': '200'}, u'HealthCheckPort': 'traffic-port', u'Port': 80, u'TargetGroupName': 'killme'}]}
        try:
            target_groups = client.describe_target_groups(
                # LoadBalancerArn='string',
                # TargetGroupArns=[
                #     'string',
                # ],
                Names=[
                    group_name,
                ],
                # Marker='string',
                # PageSize=123
            )
            if target_groups['TargetGroups'] and target_groups['TargetGroups'][0]:
                return [target_groups['TargetGroups'][0]['TargetGroupArn'].encode('utf-8')]
        except Exception:  # TargetGroupNotFoundException:
            return None
        return None
