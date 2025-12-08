import boto3
import uuid

s3 = boto3.client('s3')

bucket_name = f"shahsank-puppala-test-project-bucket-{uuid.uuid4().hex[:6]}"
region = "us-east-1"

s3.create_bucket(Bucket=bucket_name)

print("Bucket created:", bucket_name)

# Uploading a sample text file
file_name = "sample.txt"
with open(file_name, "w") as f:
    f.write("This is a sample upload via Boto3.")

s3.upload_file(file_name, bucket_name, file_name)
print("File uploaded:", file_name)
