import boto3
import datetime


awsconsole = boto3.session.Session(profile_name="default")
ec2_resource = awsconsole.resource(service_name="ec2", region_name="us-east-1")
ec2_client = awsconsole.client(service_name="ec2", region_name="us-east-1")


start_time = str(datetime.datetime(
    year=2021, month=10, day=13, hour=19, minute=10, second=00))
print(start_time)

stop_time = str(datetime.datetime(
    year=2021, month=10, day=13, hour=19, minute=15, second=00))
print(stop_time)

ec2response = ec2_client.describe_instances()
for eachec2 in ec2response['Reservations']:
    for eceryec2 in eachec2['Instances']:
        print(eceryec2['InstanceId'])

ec2status = ec2_client.describe_instance_status()
print(ec2status)

ec2start = ec2_client.start_instances(
    InstanceIds=['i-08636edc1603ac094'])
print(ec2start)
