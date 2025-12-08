import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances(
    Filters=[
        {"Name": "instance-state-name", "Values": ["running", "stopped", "pending", "stopping"]}
    ]
)

if not response["Reservations"]:
    print("No EC2 instances found.")
else:
    print("EC2 Instances:\n")
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            # Get Name tag if exists
            name = "N/A"
            if "Tags" in instance:
                for tag in instance["Tags"]:
                    if tag["Key"] == "Name":
                        name = tag["Value"]
            print("Name:", name)
            print("Instance ID:", instance["InstanceId"])
            print("State:", instance["State"]["Name"])
            print("Type:", instance["InstanceType"])
            print("AZ:", instance["Placement"]["AvailabilityZone"])
            print("Private IP:", instance.get("PrivateIpAddress"))
            print("Public IP:", instance.get("PublicIpAddress"))
            print("-" * 50)
