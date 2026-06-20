import boto3
import time


awsconsole = boto3.session.Session(profile_name="default")
ec2_resource = awsconsole.resource(service_name="ec2", region_name="us-east-1")
ec2_client = awsconsole.client(service_name="ec2", region_name="us-east-1")


current_time = time.strftime("%m/%d/%Y, %H:%M:%S")

ec2response = ec2_client.describe_instances()
for eachec2 in ec2response['Reservations']:
    for eceryec2 in eachec2['Instances']:
        print(eceryec2['InstanceId'])

ec2status = ec2_client.describe_instance_status()
print(ec2status)

ec2start = ec2_client.start_instances(
    InstanceIds=['i-08636edc1603ac094'])
print(ec2start)
ec2stop = ec2_client.stop_instances(
    InstanceIds=['i-08636edc1603ac094'])
print(ec2stop)
