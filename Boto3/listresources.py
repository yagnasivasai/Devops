import boto3

awsconsole = boto3.session.Session(profile_name="root")
dir(awsconsole)
print(awsconsole.get_available_resources())
