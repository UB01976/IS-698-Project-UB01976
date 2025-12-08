import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

response = ec2.describe_instances(
    InstanceIds=['i-0ca785c90daabf6f1']  #Put the actual instance ID you have in your AWS account
)

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("Instance ID:", instance['InstanceId'])
        print("Type:", instance['InstanceType'])
        print("State:", instance['State']['Name'])
        print("AZ:", instance['Placement']['AvailabilityZone'])
        print("Private IP:", instance.get('PrivateIpAddress'))
        print("Public IP:", instance.get('PublicIpAddress'))
        name = "N/A"
        for tag in instance.get("Tags", []):
            if tag["Key"] == "Name":
                name = tag["Value"]
        print("Name:", name)