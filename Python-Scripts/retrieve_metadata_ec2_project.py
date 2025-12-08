import requests

# IMDSv2 token
token = requests.put(
    "http://169.254.169.254/latest/api/token",
    headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"}
).text

def get_metadata(key):
    url = f"http://169.254.169.254/latest/meta-data/{key}"
    response = requests.get(url, headers={"X-aws-ec2-metadata-token": token})
    return response.text

metadata_keys = [
    "ami-id",
    "instance-id",
    "instance-type",
    "hostname",
    "local-ipv4",
    "public-ipv4",
    "placement/availability-zone",
    "security-groups"
]

metadata = {}
for key in metadata_keys:
    metadata[key] = get_metadata(key)

for k, v in metadata.items():
    print(f"{k}: {v}")
