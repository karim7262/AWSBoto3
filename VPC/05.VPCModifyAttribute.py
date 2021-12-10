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


def modify_vpc_attribute(vpc_id, dns_support):
    """
    Modifies the specified attribute of the specified VPC.
    """
    try:
        response = vpc_client.modify_vpc_attribute(
            EnableDnsSupport={'Value': dns_support}, VpcId=vpc_id)

    except ClientError:
        logger.exception('Could not modify the vpc attribute.')
        raise
    else:
        return response


if __name__ == '__main__':
    # Constants
    VPC_ID = 'vpc-0bd00c7e9d953cb23'
    enableDnsSupport = True
    vpc_attribute = modify_vpc_attribute(VPC_ID, enableDnsSupport)
    logger.info(
        f'VPC attribute enableDnsSupport modified. New value: {enableDnsSupport}'
    )