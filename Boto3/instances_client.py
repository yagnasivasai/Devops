import boto3


ec2service = boto3.client(service_name='ec2', region_name='us-east-1', aws_access_key_id="",
                          aws_secret_access_key='/')

mine = []
variable = ec2service.describe_instances()['Reservations']
for everyinstance in variable['Instances']:
    print(everyinstance['InstanceId'])
    mine.append(everyinstance['InstanceId'])
