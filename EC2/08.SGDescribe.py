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


def describe_security_groups(tag, tag_values, max_items):
    """
    Describes one or more of your security groups.
    """
    try:
        # creating paginator object for describe_subnets() method
        paginator = vpc_client.get_paginator('describe_security_groups')

        # creating a PageIterator from the paginator
        response_iterator = paginator.paginate(
            Filters=[{
                'Name': f'tag:{tag}',
                'Values': tag_values
            }],
            PaginationConfig={'MaxItems': max_items})

        full_result = response_iterator.build_full_result()

        security_groups_list = []

        for page in full_result['SecurityGroups']:
            security_groups_list.append(page)

    except ClientError:
        logger.exception('Could not describe Security Groups.')
        raise
    else:
        return security_groups_list


if __name__ == '__main__':
    # Constants
    TAG = 'Name'
    TAG_VALUES = ['hands-on-cloud-security-group']
    MAX_ITEMS = 10
    security_groups = describe_security_groups(TAG, TAG_VALUES, MAX_ITEMS)
    logger.info('Security Groups details: ')
    for security_group in security_groups:
        logger.info(json.dumps(security_groups, indent=4) + '\n')