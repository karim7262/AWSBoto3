import logging
import boto3
from botocore.exceptions import ClientError
import json

AWS_REGION = 'us-east-2'

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

vpc_resource = boto3.resource("ec2", region_name=AWS_REGION)


def create_custom_subnet(az, vpc_id, cidr_block):
    """
    Creates a custom subnet with the specified configuration.
    """
    try:
        response = vpc_resource.create_subnet(TagSpecifications=[
            {
                'ResourceType': 'subnet',
                'Tags': [{
                    'Key': 'Name',
                    'Value': 'hands-on-cloud-custom-subnet'
                }]
            },
        ],
                                              AvailabilityZone=az,
                                              VpcId=vpc_id,
                                              CidrBlock=cidr_block)

    except ClientError:
        logger.exception(f'Could not create a custom subnet.')
        raise
    else:
        return response


if __name__ == '__main__':
    # Constants
    CIDR_BLOCK = '192.168.1.0/20'
    VPC_ID = 'vpc-048604f523ad01d74'
    AZ = 'us-east-2a'
    logger.info(f'Creating a custom Subnet...')
    custom_subnet = create_custom_subnet(AZ, VPC_ID, CIDR_BLOCK)
    logger.info(f'Custom Subnet is created with Subnet ID: {custom_subnet.id}')