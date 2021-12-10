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


def delete_vpc(vpc_id):
    """
    Deletes the specified VPC.
    """
    try:
        response = vpc_client.delete_vpc(VpcId=vpc_id)

    except ClientError:
        logger.exception('Could not delete the vpc.')
        raise
    else:
        return response


if __name__ == '__main__':
    # Constants
    VPC_ID = 'vpc-0bd00c7e9d953cb23'
    vpc = delete_vpc(VPC_ID)
    logger.info(f'VPC {VPC_ID} is deleted successfully.')