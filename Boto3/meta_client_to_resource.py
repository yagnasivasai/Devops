import boto3

awsconsole = boto3.session.Session(profile_name="root")
ec2res = awsconsole.resource(service_name="ec2")

'''meta is client objects to resource objects'''

for each_region in ec2res.meta.client.describe_regions()['Regions']:
    print(each_region['RegionName'])
