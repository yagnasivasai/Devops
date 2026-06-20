import boto3
import sys

awsconsole = boto3.session.Session(profile_name="root")
ec2client = awsconsole.client(service_name="ec2", region_name="us-east-1")

while True:
    print("Ec2 instance: ")
    print(
        """
        1. start
        2. stop
        3. terminate
        4. exit
        """
    )
    option = int(input("option: "))
    if option == 1:
        req_instance = ec2client.start_instances(
            InstanceIds=['i-0131e858cf2d1e460'])
        print("starting")
    elif option == 2:
        req_instance = ec2client.stop_instances(
            InstanceIds=['i-0131e858cf2d1e460'])
        print("stopping")
    elif option == 3:
        req_instance = ec2client.terminate_instances(
            InstanceIds=['i-0131e858cf2d1e460'])
        print("terminating")
    elif option == 4:
        sys.exit()
    else:
        print("option not valid")
