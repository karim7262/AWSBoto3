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


def put_policy_kms_key(key_id, policy):
    """
    Attaches a key policy to the specified KMS key.
    """
    try:
        response = kms_client.put_key_policy(KeyId=key_id,
                                             PolicyName='default',
                                             Policy=policy)

    except ClientError:
        logger.exception('Could not attach a key policy.')
        raise
    else:
        return response


if __name__ == '__main__':
    # Constants
    KEY_ID = '1e7ca6bf-884d-4e46-8195-f9aa5a3c1569'
    POLICY = '''
    {
        "Version": "2012-10-17",
        "Statement": [{
            "Sid": "Allowing Access",
            "Effect": "Allow",
            "Principal": {"AWS": [
                "arn:aws:iam::979450158315:user/iamadmin"
            ]},
            "Action": "kms:*",
            "Resource": "*"
        }]
    }'''
    logger.info('Attaching a key policy...')
    kms = put_policy_kms_key(KEY_ID, POLICY)
    logger.info('Key policy is attached.')