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


def enable_kms_key(key_id):
    """
    Sets the key state of a KMS key to enabled..
    """
    try:
        response = kms_client.enable_key(KeyId=key_id)

    except ClientError:
        logger.exception('Could not enable a KMS key.')
        raise
    else:
        return response


def cancel_kms_key_deletion(key_id):
    """
    Cancels the deletion of a KMS key.
    """
    try:
        response = kms_client.cancel_key_deletion(KeyId=key_id)

        # After canclling the deletion, enable the key again
        _ = enable_kms_key(key_id)

    except ClientError:
        logger.exception('Could not cancel key deletion.')
        raise
    else:
        return response


if __name__ == '__main__':
    # Constants
    KEY_ID = '1e7ca6bf-884d-4e46-8195-f9aa5a3c1569'
    logger.info('Canceling deletion of KMS key...')
    kms = cancel_kms_key_deletion(KEY_ID)
    logger.info(
        f'Key Deletion cancelled and enabled for encryption operations. \nDetails: {json.dumps(kms, indent=4)}'
    )