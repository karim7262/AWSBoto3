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


def get_policy_kms_key(key_id):
    """
    Gets a key policy attached to the specified KMS key.
    """
    try:
        response = kms_client.get_key_policy(KeyId=key_id,
                                             PolicyName='default')

    except ClientError:
        logger.exception('Could not get the key policy.')
        raise
    else:
        return response


if __name__ == '__main__':
    # Constants
    KEY_ID = '1e7ca6bf-884d-4e46-8195-f9aa5a3c1569'
    logger.info('Gettign a key policy...')
    kms = get_policy_kms_key(KEY_ID)
    logger.info(f'Key policy: {json.dumps(kms, indent=4)}')