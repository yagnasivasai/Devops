import boto3
from datetime import datetime

session = boto3.session.Session(profile_name="root")
iamres = session.resource(service_name='iam')
'''
iamobj = iamres.User('s3_developer')
'''
for iamobj in iamres.users.all():
    print(iamobj)
    print(iamobj.user_id)
    print(iamobj.user_name)
    print(iamobj.arn)
    print(iamobj.create_date.strftime("%m/%d/%Y, %H:%M:%S"))
