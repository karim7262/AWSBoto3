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


def delete_security_group(security_group_id):
    """
    Deletes the specified security group.
    """
    try:
        response = vpc_client.delete_security_group(GroupId=security_group_id)

    except ClientError:
        logger.exception('Could not delete the security group.')
        raise
    else:
        return response


if __name__ == '__main__':
    # Constants
    SECURITY_GROUP_ID = 'sg-08e4ffb1b4087e728'
    security_group = delete_security_group(SECURITY_GROUP_ID)
    logger.info(f'Security group {SECURITY_GROUP_ID} is deleted successfully.')