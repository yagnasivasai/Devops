import json
import boto3
#from mypy_boto3_ec2.service_resource import Instance
ec2 = boto3.resource(service_name="ec2", region_name="us-east-1", aws_access_key_id='',
                     aws_secret_access_key='/')
create = ec2.create_instances(
    ImageId='ami-0742b4e673072066f',
    InstanceType='t1.micro',
    KeyName='Yegna',
    MaxCount=2,
    MinCount=1)
print(dir(create))
