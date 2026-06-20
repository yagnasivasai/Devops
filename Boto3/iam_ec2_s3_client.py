import boto3

awsconsole_object = boto3.session.Session(profile_name="root")

iam_client = awsconsole_object.client(
    service_name="iam", region_name="us-east-1")
ec2_client = awsconsole_object.client(
    service_name="ec2", region_name="us-east-1")
s3_client = awsconsole_object.client(
    service_name="s3", region_name="us-east-1")

# Getting IAM USERS
iamresponse = iam_client.list_users()
for eachitem in iamresponse['Users']:
    print(eachitem)
    print("//////////////////////")

# Getting EC2 INSTANCES
ec2response = ec2_client.describe_instances()
for eachec2 in ec2response['Reservations']:
    for eachinstance in eachec2['Instances']:
        print(eachinstance['InstanceId'])
    print("!!!!!!!!!!!!!!!!!!!!")
ec2status = ec2_client.describe_instance_status()
print(ec2status)

# Getting S3 BUCKETS
s3response = s3_client.list_buckets()
for eachs3 in s3response['ResponseMetadata']:
    print(eachs3)
    print("**************************")
for everybuck in s3response['Buckets']:
    print(everybuck)
