import json
import logging

import boto3
from botocore.exceptions import ClientError

AWS_REGION = 'us-east-2'

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

kms_client = boto3.client("kms", region_name=AWS_REGION)


def list_kms_keys(max_items):
    """
    Gets a list of all KMS keys.
    """
    try:
        # creating paginator object for list_keys() method
        paginator = kms_client.get_paginator('list_keys')

        # creating a PageIterator from the paginator
        response_iterator = paginator.paginate(
            PaginationConfig={'MaxItems': max_items})

        full_result = response_iterator.build_full_result()

        key_list = []

        for page in full_result['Keys']:
            key_list.append(page)

    except ClientError:
        logger.exception('Could not list KMS Keys.')
        raise
    else:
        return key_list


if __name__ == '__main__':
    # Constants
    MAX_ITEMS = 10
    logger.info('Getting a list of KMS keys...')
    kms_keys = list_kms_keys(MAX_ITEMS)
    for kms_key in kms_keys:
        logger.info(f'Key Details: {kms_key}')