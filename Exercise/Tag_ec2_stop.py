import boto3
from pprint import pprint
import time

awsconsole = boto3.session.Session(profile_name="default")
ec2_client = awsconsole.client(service_name="ec2", region_name="us-east-1")

################################
tag = {'Name': 'tag:Schedule', 'Values': ['True']}
for ec2 in ec2_client.describe_instances(Filters=[tag])['Reservations']:
    for id in ec2['Instances']:
        print(id['InstanceId'])
        ec2_client.stop_instances(InstanceIds=[id['InstanceId']])
        print("stop_instances")
