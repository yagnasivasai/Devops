import json
import boto3


def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    tag = {'Name': 'tag:Schedule', 'Values': ['True']}
    instance_iterator = ec2.instances.filter(Filters=[tag])
    for everyinstance in instance_iterator:
        everyinstance.start()

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
