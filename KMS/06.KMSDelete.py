import json
import logging
from datetime import date, datetime

import boto3
from botocore.exceptions import ClientError

AWS_REGION = 'us-east-2'

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

kms_client = boto3.client("kms", region_name=AWS_REGION)


def json_datetime_serializer(obj):
    """
    Helper method to serialize datetime fields
    """
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


def delete_kms_key(key_id, pending_window_in_days):
    """
    Schedules the deletion of a KMS key.
    """
    try:
        response = kms_client.schedule_key_deletion(
            KeyId=key_id, PendingWindowInDays=pending_window_in_days)

    except ClientError:
        logger.exception('Could not delete a KMS key.')
        raise
    else:
        return response


if __name__ == '__main__':
    # Constants
    KEY_ID = '1e7ca6bf-884d-4e46-8195-f9aa5a3c1569'
    PENDING_WINDOW_IN_DAYS = 7
    logger.info('Scheduling deletion of KMS key...')
    kms = delete_kms_key(KEY_ID, PENDING_WINDOW_IN_DAYS)
    logger.info(
        f'Deletion Details: {json.dumps(kms, indent=4, default=json_datetime_serializer)}'
    )