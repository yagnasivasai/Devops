import boto3

ec2 = boto3.resource(service_name='ec2',
                     region_name='us-east-1',
                     aws_access_key_id='',
                     aws_secret_access_key='/')


vpc = ec2.create_vpc(CidrBlock='10.10.10.10/16')
vpc.create_tags(Tags=[{
                'Key': 'Name',
                'Value': 'testresource'}])
vpc.wait_until_available()
print(vpc.vpc_id)
