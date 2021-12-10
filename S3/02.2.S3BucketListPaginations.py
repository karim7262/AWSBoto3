import boto3

# Create a client
client = boto3.client('s3', region_name='us-west-2')

#list_objects operation of Amazon S3 returns up to 1000 objects at a time
# Create a reusable Paginator
paginator = client.get_paginator('list_objects')

# Create a PageIterator from the Paginator
# page_iterator = paginator.paginate(Bucket='bktd1mujahed')

# for page in page_iterator:
#     print(page['Contents'])

#Customizing Data
page_iterator = paginator.paginate(Bucket='bktd1mujahed',
                                   PaginationConfig={'MaxItems': 10})

for page in page_iterator:
    print(page['Contents'])