import boto3
import csv

awsconsole = boto3.session.Session(profile_name="root")
awsres = awsconsole.resource(service_name="ec2", region_name="us-east-1")

count = 1
csvobj = open("inventory.csv", "w", newline='')
csv_w = csv.writer(csvobj)
csv_w.writerow(["sno", "instanceid", "instancetype", "instancearchitecture",
                "launchtime", "privateip"])
for eachitem in awsres.instances.all():
    print([count, eachitem, eachitem.instance_id, eachitem.instance_type, eachitem.architecture,
           eachitem.launch_time, eachitem.private_ip_address])
    csv_w.writerow([count, eachitem.instance_id, eachitem.instance_type,
                    eachitem.architecture, eachitem.launch_time, eachitem.private_ip_address])
    count += 1
csvobj.close()
