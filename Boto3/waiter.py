import boto3

awsconsole = boto3.session.Session(profile_name="root")
ec2client = awsconsole.client(service_name="ec2", region_name="us-east-1")
ec2resource = awsconsole.resource(service_name="ec2", region_name="us-east-1")


'''
response = ec2resource.Instance('i-0131e858cf2d1e460')
print("starting ec2 instance")
response.start()
response.wait_until_running()
print("your instance is up and runing")
'''

print("starting ec2 instances")
ec2client.start_instances(InstanceIds=['i-0131e858cf2d1e460'])
waiter = ec2client.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-0131e858cf2d1e460'])
print("your ec2 instance is up and running")
