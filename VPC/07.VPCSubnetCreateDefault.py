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


def create_default_subnet(az):
    """
    Creates a default subnet in the configured availability zone.
    """
    try:
        response = vpc_client.create_default_subnet(AvailabilityZone=az)

    except ClientError:
        logger.exception('Could not create default subnet.')
        raise
    else:
        return response


if __name__ == '__main__':
    # Constants
    AvailabilityZone = 'us-east-2b'
    logger.info(f'Creating default subnet...')
    default_subnet = create_default_subnet(AvailabilityZone)
    logger.info(
        f'Default Subnet is created with ID: \n{json.dumps(default_subnet, indent=4)}'
    )