import boto3
import botostubs
import boto3_type_annotations

awsconsole = boto3.session.Session(profile_name="root")
stsclient = awsconsole.client(service_name="sts", region_name="us-east-1")
variable = stsclient.get_caller_identity()
print(variable)
print(variable.get('Account'))
print(variable['UserId'])

awsconsole = boto3.session.Session(profile_name="ec2developer")
stsclient = awsconsole.client(service_name="sts", region_name="us-east-1")
variable = stsclient.get_caller_identity()
print(variable)
print(variable.get('Account'))
print(variable.get('UserId'))
print(variable['UserId'])
