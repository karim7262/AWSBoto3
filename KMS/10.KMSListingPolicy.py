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


def list_kms_policies(key_id, max_items):
    """
    Gets the names of the key policies that are attached to a KMS key.
    """
    try:
        # creating paginator object for list_key_policies() method
        paginator = kms_client.get_paginator('list_key_policies')

        # creating a PageIterator from the paginator
        response_iterator = paginator.paginate(
            KeyId=key_id, PaginationConfig={'MaxItems': max_items})

        full_result = response_iterator.build_full_result()

        policy_list = []

        for page in full_result['PolicyNames']:
            policy_list.append(page)

    except ClientError:
        logger.exception('Could not list KMS Key policies.')
        raise
    else:
        return policy_list


if __name__ == '__main__':
    # Constants
    KEY_ID = '1e7ca6bf-884d-4e46-8195-f9aa5a3c1569'
    MAX_ITEMS = 10
    logger.info('Getting a list of KMS key policies...')
    kms_policies = list_kms_policies(KEY_ID, MAX_ITEMS)
    for kms_policy in kms_policies:
        logger.info(f'Key Policy: {kms_policy}')