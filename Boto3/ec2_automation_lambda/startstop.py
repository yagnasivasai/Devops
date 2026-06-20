import json
import boto3


def lambda_handler(event, context):

    ec2 = boto3.resource('ec2')
    sns = boto3.client('sns')
    my = ec2.Instance('i-059a21b5618b885bc')
    print(my.state['Name'])

    for everyec2 in ec2.Instances.all():
        print(everyec2.id)
        everyec2.start()

    sns.publish(TargetArn="arn:aws:sns:us-east-1:346874795843:EC2",
                Message=my.state['Name'])

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
