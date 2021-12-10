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


def describe_security_groups_rules(security_group_ids, max_items):
    """
    Describes one or more of your security groups rules.
    """
    try:
        # creating paginator object for describe_subnets() method
        paginator = vpc_client.get_paginator('describe_security_group_rules')

        # creating a PageIterator from the paginator
        response_iterator = paginator.paginate(
            Filters=[{
                'Name': 'group-id',
                'Values': security_group_ids
            }],
            PaginationConfig={'MaxItems': max_items})

        full_result = response_iterator.build_full_result()

        security_groups_rules = []

        for page in full_result['SecurityGroupRules']:
            security_groups_rules.append(page)

    except ClientError:
        logger.exception('Could not describe Security Groups Rules.')
        raise
    else:
        return security_groups_rules


if __name__ == '__main__':
    # Constants
    SECURITY_GROUP_IDS = ['sg-08e4ffb1b4087e728']
    MAX_ITEMS = 10
    rules = describe_security_groups_rules(SECURITY_GROUP_IDS, MAX_ITEMS)
    logger.info('Security groups rules: ')
    for rule in rules:
        logger.info(json.dumps(rule, indent=4) + '\n')