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


def delete_subnet(subnet_id):
    """
    Deletes the specified Subnet.
    """
    try:
        response = vpc_client.delete_subnet(SubnetId=subnet_id)

    except ClientError:
        logger.exception('Could not delete the subnet.')
        raise
    else:
        return response


if __name__ == '__main__':
    # Constants
    SUBNET_ID = 'subnet-071923fde0da8166e'
    subnet = delete_subnet(SUBNET_ID)
    logger.info(f'Subnet {SUBNET_ID} is deleted successfully.')