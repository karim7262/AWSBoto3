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


def delete_egress_rule(security_group_id, security_group_rule_ids):
    """
    Deletes a security group egress rule.
    """
    try:
        response = vpc_client.revoke_security_group_egress(
            GroupId=security_group_id,
            SecurityGroupRuleIds=security_group_rule_ids)

    except ClientError:
        logger.exception('Could not delete egress security group rule.')
        raise
    else:
        return response


if __name__ == '__main__':
    # Constants
    SECURITY_GROUP_ID = 'sg-08e4ffb1b4087e728'
    SECURITY_GROUP_RULE_ID = ['sgr-0c1b8c264ea2d0e6f']
    logger.info(f'Removing a security group egress rule(s)...')
    rule = delete_egress_rule(SECURITY_GROUP_ID, SECURITY_GROUP_RULE_ID)
    logger.info(
        f'Security group egress rule(s) deleted: \n{json.dumps(rule, indent=4)}'
    )