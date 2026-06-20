import boto3

awsconsole = boto3.session.Session(profile_name="root")
ec2client = awsconsole.client(service_name="ec2", region_name="us-east-1")


response = ec2client.describe_volumes()
for eachitem in response['Volumes']:
    if not "Tags" in eachitem and eachitem['State'] == 'available':
        print('Deleting', eachitem['VolumeId'])
        ec2client.delete_volume(VolumeId=eachitem['VolumeId'])
