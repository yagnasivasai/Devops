import boto3
from pprint import pprint

awsconsole = boto3.session.Session(profile_name="ec2developer")
ec2client = awsconsole.client(service_name="ec2", region_name="us-east-1")

response = ec2client.describe_instances()['Reservations']
for eachitem in response:
    for eachinstaceinfo in eachitem['Instances']:
        print("the image ID is: {}\nthe instance ID is:{}\nthe launch date of instance is: {}".format(
            eachinstaceinfo['ImageId'], eachinstaceinfo['InstanceId'], eachinstaceinfo['LaunchTime']))

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
response = ec2client.describe_volumes()['Volumes']
for eachitem in response:
    print(eachitem)
    print(eachitem['VolumeId'])
    print(eachitem['AvailabilityZone'])
    print(eachitem['CreateTime'])
    print(eachitem['SnapshotId'])
    print(eachitem['VolumeType'])
