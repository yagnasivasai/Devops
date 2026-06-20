import boto3
import time


awsconsole = boto3.session.Session(profile_name="default")
ec2_resource = awsconsole.resource(service_name="ec2", region_name="us-east-1")
ec2_client = awsconsole.client(service_name="ec2", region_name="us-east-1")


def lambda_handler(event, context):
    current_time = time.time("%m/%d/%Y, %H:%M:%S")
    print(current_time)

    filter = [
        {   'Name': 'tag:Schedule',
            'Values': ['True']}
    ]
    instances = ec2_resource.instances.filter(Filters=filter)
    print(instances)
    stopInstances = []   
    startInstances = []   

    # Locate all instances that are tagged to start or stop.
    for instance in instances:
            
        for tag in instance.tags:

            if tag['Key'] == 'StopInstance':

                if tag['Value'] == current_time:

                    stopInstances.append(instance.id)

                    pass

                pass

            if tag['Key'] == 'StartInstance':

                if tag['Value'] == current_time:

                    startInstances.append(instance.id)

                    pass

                pass

            pass

        pass
    
    print (current_time)
    
    # shut down all instances tagged to stop. 
    if len(stopInstances) > 0:
        # perform the shutdown
        stop = ec2_resource.instances.filter(InstanceIds=stopInstances).stop()
        print (stop)
    else:
        print ("No instances to shutdown.")

    # start instances tagged to stop. 
    if len(startInstances) > 0:
        # perform the start
        start = ec2_resource.instinstances.filter(InstanceIds=startInstances).start()
        print(start) 
    else:
        print ("No instances to start.")    