import boto3
ec2=boto3.client("ec2")
waiter=ec2.get_waiter("instance_running")
waiter.wait(InstanceIds=["i-abc123"])
print("Now instance is ready...")