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


def create_ingress_rule(security_group_id):
    """
    Creates a security group ingress rule with the specified configuration.
    """
    try:
        response = vpc_client.authorize_security_group_ingress(
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
        logger.exception('Could not create ingress security group rule.')
        raise
    else:
        return response


if __name__ == '__main__':
    # Constants
    SECURITY_GROUP_ID = 'sg-08e4ffb1b4087e728'
    logger.info(f'Creating a security group ingress rule...')
    rule = create_ingress_rule(SECURITY_GROUP_ID)
    logger.info(
        f'Security group ingress rule created: \n{json.dumps(rule, indent=4)}')