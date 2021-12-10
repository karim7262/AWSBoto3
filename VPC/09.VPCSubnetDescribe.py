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


def describe_subnets(tag, tag_values, max_items):
    """
    Describes one or more of your Subnets.
    """
    try:
        # creating paginator object for describe_subnets() method
        paginator = vpc_client.get_paginator('describe_subnets')

        # creating a PageIterator from the paginator
        response_iterator = paginator.paginate(
            Filters=[{
                'Name': f'tag:{tag}',
                'Values': tag_values
            }],
            PaginationConfig={'MaxItems': max_items})

        full_result = response_iterator.build_full_result()

        subnet_list = []

        for page in full_result['Subnets']:
            subnet_list.append(page)

    except ClientError:
        logger.exception('Could not describe subnets.')
        raise
    else:
        return subnet_list


if __name__ == '__main__':
    # Constants
    TAG = 'Name'
    TAG_VALUES = ['hands-on-cloud-custom-subnet']
    MAX_ITEMS = 10
    subnets = describe_subnets(TAG, TAG_VALUES, MAX_ITEMS)
    logger.info('Subnet Details: ')
    for subnet in subnets:
        logger.info(json.dumps(subnet, indent=4) + '\n')