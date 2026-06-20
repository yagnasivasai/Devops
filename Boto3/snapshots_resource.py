import boto3


awsconsole = boto3.session.Session(profile_name="root")
awsres = awsconsole.resource(service_name="ec2", region_name="us-east-1")
awscli = awsconsole.client(service_name="sts", region_name="us-east-1")
response = awscli.get_caller_identity()
owner = response.get('Account')

for each in awsres.snapshots.filter(OwnerIds=[owner]):
    print(each)
'''
for each in awscli.describe_snapshots(OwnerIds=[owner]):
    print(each)
'''
