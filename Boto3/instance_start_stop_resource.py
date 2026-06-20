import boto3
import sys

awsconsole = boto3.session.Session(profile_name="root")
ec2resource = awsconsole.resource(service_name="ec2", region_name="us-east-1")
ec2client = awsconsole.client(service_name="ec2", region_name="us-east-1")

while True:
    print("This script performs the following functions")
    print("""
    1. start 
    2. terminate
    3. stop
    4. exit
    """)
    option = int(input("please enter your option: "))
    if option == 1:
        instance_id = input("enter your ec2 id: ")
        instance_object = ec2resource.Instance(instance_id)
        print(dir(instance_object))
        print("starting the instance")
        instance_object.start()
    elif option == 2:
        instance_id = input("enter your ec2 id: ")
        instance_object = ec2resource.Instance(instance_id)
        print("terminating the instance")
        instance_object.terminate()
    elif option == 3:
        instance_id = input("enter your ec2 id: ")
        instance_object = ec2resource.Instance(instance_id)
        print("stoping the instance")
        instance_object.stop()
    elif option == 4:
        sys.exit
    else:
        print("your option is invalid")
        print("try again")
