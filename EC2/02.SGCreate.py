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


def create_security_group(description, groupname, vpc_id):
    """
    Creates a security group with the specified configuration.
    """
    try:
        response = vpc_resource.create_security_group(Description=description,
                                                      GroupName=groupname,
                                                      VpcId=vpc_id,
                                                      TagSpecifications=[{
                                                          'ResourceType':
                                                          'security-group',
                                                          'Tags': [{
                                                              'Key':
                                                              'Name',
                                                              'Value':
                                                              groupname
                                                          }]
                                                      }])

    except ClientError:
        logger.exception('Could not create a security group.')
        raise
    else:
        return response


if __name__ == '__main__':
    # Constants
    DESCRIPTION = 'Security group created for hands-on-cloud blog'
    GROUPNAME = 'hands-on-cloud-security-group'
    VPC_ID = 'vpc-048604f523ad01d74'
    logger.info(f'Creating a security group...')
    security_group = create_security_group(DESCRIPTION, GROUPNAME, VPC_ID)
    logger.info(f'Security group created with ID: {security_group.id}')