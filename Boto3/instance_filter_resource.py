from logging import Filter
import boto3
import botostubs

awsconsole = boto3.session.Session(profile_name="root")
s3 = awsconsole.resource(service_name='s3', region_name="us-east-1")
ec2 = awsconsole.resource(service_name='ec2', region_name="us-east-1")

filter1 = {
    'Name': "instance-state-name", 'Values': ['stopped', 'running']
}
filter2 = {
    'Name': "instance-type", 'Values': ['t2.micro']
}


for each in ec2.instances.filter(Filters=[filter1, filter2]):
    print(each)
