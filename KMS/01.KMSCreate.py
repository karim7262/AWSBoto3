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


def create_kms_key():
    """
    Creates a unique customer managed KMS key.
    """
    try:
        response = kms_client.create_key(Description='hands-on-cloud-cmk',
                                         Tags=[{
                                             'TagKey': 'Name',
                                             'TagValue': 'hands-on-cloud-cmk'
                                         }])

    except ClientError:
        logger.exception('Could not create a CMK key.')
        raise
    else:
        return response


if __name__ == '__main__':
    # Constants
    logger.info('Creating a symetric CMK...')
    kms = create_kms_key()
    logger.info(
        f'Symetric CMK is created with details: {json.dumps(kms, indent=4, default=json_datetime_serializer)}'
    )