# Getting all the s3 bucket in my Account

import boto3
from pprint import pprint
from mypy_boto3_s3.client import S3Client
from mypy_boto3_s3.service_resource import S3ServiceResource

aws = boto3.session.Session(profile_name="default")
s3 = aws.resource(service_name='s3')


for everybucket in s3.buckets.all():
    print(everybucket)
    print(everybucket.creation_date)
