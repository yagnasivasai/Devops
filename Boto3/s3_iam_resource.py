import boto3
import botostubs

awsconsole = boto3.session.Session(profile_name="root")
iamres = awsconsole.resource(service_name="iam", region_name="us-east-1")
ec2res = awsconsole.resource(service_name="ec2", region_name="us-east-1")
s3res = awsconsole.resource(service_name="s3", region_name="us-east-1")

for eachuser in iamres.users.all():
    print(eachuser)

for eachbuc in s3res.buckets.all():
    print(eachbuc.name)
