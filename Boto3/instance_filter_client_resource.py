import boto3


awsconsole = boto3.session.Session(profile_name="root")
ec2resource = awsconsole.resource(service_name="ec2", region_name="us-east-1")
ec2client = awsconsole.client(service_name="ec2", region_name="us-east-1")

nonpodids = []

f1 = {'Name': "tag:Name", 'Values': ['pod']}

for each in ec2resource.instances.filter(Filters=[f1]):
    nonpodids.append(each.id)

for eachitem in ec2client.describe_instances(Filters=[f1])['Reservations']:
    for ieach in eachitem['Instances']:
        print(ieach['InstanceId'])
