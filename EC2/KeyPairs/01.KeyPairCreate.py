import boto3

ec2 = boto3.resource('ec2')
key_pair = ec2.KeyPair('m1')