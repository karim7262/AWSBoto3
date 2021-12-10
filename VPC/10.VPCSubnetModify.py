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


def modify_subnet_attribute(subnet_id, map_public_ip_on_launch):
    """
    Modifies the specified attribute of the specified subnet.
    """
    try:
        response = vpc_client.modify_subnet_attribute(
            MapPublicIpOnLaunch={'Value': map_public_ip_on_launch},
            SubnetId=subnet_id)

    except ClientError:
        logger.exception('Could not modify the Subnet attribute.')
        raise
    else:
        return response


if __name__ == '__main__':
    # Constants
    SUBNET_ID = 'subnet-071923fde0da8166e'
    MAP_PUBLIC_IP_ON_LAUNCH = True
    subnet_attribute = modify_subnet_attribute(SUBNET_ID,
                                               MAP_PUBLIC_IP_ON_LAUNCH)
    logger.info(
        f'Subnet attribute MapPublicIpOnLaunch modified. New value: {MAP_PUBLIC_IP_ON_LAUNCH}'
    )