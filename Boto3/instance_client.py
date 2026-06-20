import boto3


ec2 = boto3.resource(service_name='ec2', region_name="us-east-1", aws_access_key_id="",
                     aws_secret_access_key="/")
ec2 = boto3.client(service_name='ec2', region_name="us-east-1", aws_access_key_id="",
                   aws_secret_access_key="/")

'''
filter = {"Name": "tag:env", "Value": ["linux"]}
for eachinstance in ec2.instances.filter(Filters=[filter]):
    print(eachinstance.id)
'''
ec2 = ec2.describe_instances()
for eachec2 in ec2['Reservations']:
    for eachinstance in eachec2['Instances']:
        print(eachinstance['InstanceId'])
