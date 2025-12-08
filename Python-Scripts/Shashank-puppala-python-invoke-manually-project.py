import boto3
import json

# Initialize Lambda client
lambda_client = boto3.client('lambda', region_name='us-east-1')


function_name = "MyHelloLambda" #input the name of your lambda function which you want to invoke


payload = {
    "message": "Manual invocation from Python script"
}

# Invoke Lambda
response = lambda_client.invoke(
    FunctionName=function_name,
    InvocationType='RequestResponse', 
    Payload=json.dumps(payload)
)


response_payload = json.load(response['Payload'])
print("Lambda Response:", response_payload)
