import boto3
import sys


awsconsole = boto3.session.Session(profile_name="root")
ec2resource = awsconsole.resource(service_name="ec2", region_name="us-east-1")
ec2client = awsconsole.client(service_name="ec2", region_name="us-east-1")

while True:
    print("select the option for ec2 instances: ")
    print(
        """
        1. start
        2. stop
        3. exit
    """)
    option = int(input())
    all_instance_ids = []
    for each_id in ec2resource.instances.all():
        all_instance_ids.append(each_id.id)
        if option == 1:
            waiter = ec2client.get_waiter('instance_running')
            print("starting instances")
            ec2resource.instances.start()
            waiter.wait(InstanceIds=all_instance_ids)
            print("instance up and running")

        if option == 2:
            waiter = ec2client.get_waiter('instance_stopped')
            print("stopping instances")
            ec2resource.instances.stop()
            waiter.wait(InstanceIds=all_instance_ids)
            print("instances stopped")
        if option == 3:
            sys.exit()
