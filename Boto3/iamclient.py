import boto3


awsconsole = boto3.session.Session(profile_name="root")
iamconsole = awsconsole.client(service_name='iam', region_name="us-east-1")
## iamconsole = awsconsole.resource(service_name='iam', region_name="us-east-1")

# for each in iamconsole.users.all():
# print(each.name)


for eachuser in iamconsole.list_users()['Users']:
    print(eachuser)


print("******************")

for each_user in iamconsole.list_users()['Users']:
    print(each_user['UserName'])
