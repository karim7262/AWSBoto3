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


def modify_rule(security_group_id, security_group_rule_id):
    """
    Modify the existing security group rules with the specified configuration.
    """
    try:
        response = vpc_client.modify_security_group_rules(
            GroupId=security_group_id,
            SecurityGroupRules=[
                {
                    'SecurityGroupRuleId': security_group_rule_id,
                    'SecurityGroupRule': {
                        'IpProtocol': 'tcp',
                        'FromPort': 8080,
                        'ToPort': 8080,
                        'CidrIpv4': '0.0.0.0/0',
                        'Description': 'hands-on-cloud-security-group-rules'
                    }
                },
            ])

    except ClientError:
        logger.exception('Could not modify security group rule.')
        raise
    else:
        return response


if __name__ == '__main__':
    # Constants
    SECURITY_GROUP_ID = 'sg-08e4ffb1b4087e728'
    SECURITY_GROUP_RULE_ID = 'sgr-0587b4899af1c7a2f'
    logger.info(f'Modifing a security group rule...')
    rule = modify_rule(SECURITY_GROUP_ID, SECURITY_GROUP_RULE_ID)
    logger.info(
        f'Security group rule modified: \n{json.dumps(rule, indent=4)}')