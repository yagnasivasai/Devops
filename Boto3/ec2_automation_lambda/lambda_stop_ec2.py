import json
import boto3
ec2_client = boto3.client(service_name="ec2", region_name="us-east-1")

def lambda_handler(event, context):
    tag = {'Name': 'tag:Schedule', 'Values': ['True']}
    for ec2 in ec2_client.describe_instances(Filters=[tag])['Reservations']:
        for id in ec2['Instances']:
            print(id['InstanceId'])
            ec2_client.stop_instances(InstanceIds=[id['InstanceId']])
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

