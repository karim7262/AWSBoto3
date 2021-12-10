import logging
import boto3
from botocore.exceptions import ClientError
import json

AWS_REGION = 'us-east-2'

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

vpc_client = boto3.client("ec2", region_name=AWS_REGION)


def create_egress_rule(security_group_id):
    """
    Creates a security group egress rule with the specified configuration.
    """
    try:
        response = vpc_client.authorize_security_group_egress(
            GroupId=security_group_id,
            IpPermissions=[{
                'IpProtocol': 'tcp',
                'FromPort': 80,
                'ToPort': 80,
                'IpRanges': [{
                    'CidrIp': '0.0.0.0/0'
                }]
            }, {
                'IpProtocol': 'tcp',
                'FromPort': 22,
                'ToPort': 22,
                'IpRanges': [{
                    'CidrIp': '0.0.0.0/0'
                }]
            }])

    except ClientError:
        logger.exception('Could not create egress security group rule.')
        raise
    else:
        return response


if __name__ == '__main__':
    # Constants
    SECURITY_GROUP_ID = 'sg-08e4ffb1b4087e728'
    logger.info(f'Creating a security group egress rule...')
    rule = create_egress_rule(SECURITY_GROUP_ID)
    logger.info(
        f'Security group egress rule created: \n{json.dumps(rule, indent=4)}')