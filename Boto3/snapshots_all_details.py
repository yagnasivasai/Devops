import boto3
import datetime


awsconsole = boto3.session.Session(profile_name="root")
awsres = awsconsole.resource(service_name="ec2", region_name="us-east-1")
awscli = awsconsole.client(service_name="sts", region_name="us-east-1")
response = awscli.get_caller_identity()
owner = response.get('Account')

start_time = str(datetime.datetime(
    year=2021, month=3, day=27, hour=3, minute=15, second=00))
print(start_time)

for each in awsres.snapshots.filter(OwnerIds=[owner]):
    print(each.start_time.strftime("%Y-%m-%d %H-%M-%S"))
    print(each.start_time)
    print(each.owner_id)
    print(each.snapshot_id)
    print(each.volume_id)
    print(each.volume_size)
    print(each.description)
    print(each.data_encryption_key_id)
