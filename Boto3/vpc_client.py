import boto3

ec2client = boto3.client(service_name='ec2',
                         region_name='us-east-1',
                         aws_access_key_id='',
                         aws_secret_access_key='/')

vpc = ec2client.create_vpc(CidrBlock='10.10.0.0/16', TagSpecifications=[
                           {'ResourceType': 'vpc', 'Tags': [{'Key': 'Name', 'Value': 'customvpc'}]}])
vpcid = vpc['Vpc']['VpcId']
print(vpcid)
sub = ec2client.create_subnet(VpcId=vpcid, CidrBlock='10.10.1.0/24')
subid = sub['Subnet']['SubnetId']
print(subid)


ig = ec2client.create_internet_gateway(TagSpecifications=[
                                       {'ResourceType': 'internet-gateway', 'Tags': [{'Key': 'Name', 'Value': 'customig'}]}])
igid = ig['InternetGateway']['InternetGatewayId']
print(igid)
ig_a = ec2client.attach_internet_gateway(InternetGatewayId=igid, VpcId=vpcid)

rt = ec2client.create_route_table(VpcId=vpcid, TagSpecifications=[
                                  {'ResourceType': 'route-table', 'Tags': [{'Key': 'Name', 'Value': 'customrt'}]}])
routetableid = rt['RouteTable']['RouteTableId']
print(routetableid)
rt_a = ec2client.create_route(
    DestinationCidrBlock='0.0.0.0/0', RouteTableId=routetableid, GatewayId=igid)
