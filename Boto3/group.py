import boto3

aws = boto3.session.Session(profile_name='root')
grp = aws.client(service_name="iam")

all = grp.list_groups()
print(all)

'''
for eachuser in grp.users.all():
    print(eachuser)
'''
