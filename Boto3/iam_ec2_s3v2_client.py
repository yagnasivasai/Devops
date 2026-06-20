import boto3

awsconsole_object = boto3.session.Session(profile_name="root")

iam_client = awsconsole_object.client(
    service_name="iam", region_name="us-east-1")
ec2_client = awsconsole_object.client(
    service_name="ec2", region_name="us-east-1")
s3_client = awsconsole_object.client(
    service_name="s3", region_name="us-east-1")

# Getting IAM USERS
for eachitem in iam_client.list_users()['Users']:
    print(eachitem)
    print("//////////////////////")

# Getting EC2 INSTANCES
for eachec2 in ec2_client.describe_instances()['Reservations']:
    for eachinstance in eachec2['Instances']:
        print(eachinstance['InstanceId'])
    print("!!!!!!!!!!!!!!!!!!!!")
ec2status = ec2_client.describe_instance_status()
print(ec2status)

# Getting S3 BUCKETS
for eachs3 in s3_client.list_buckets()['ResponseMetadata']:
    print(eachs3)
    print("**************************")
for everybuck in s3_client.list_buckets()['Buckets']:
    print(everybuck)
