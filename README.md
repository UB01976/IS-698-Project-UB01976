<h1>Deploying a Scalable AWS Architecture with Infrastructure as Code.</h1>
<h3>Step 1</h3>
The project begins from creation of Networking resources using Terraform. First the Networking resource components like VPC, Subnets, Route tables, Associations, IGW (Internet Gateway), and Security Groups are created using terraform.
The terraform files are pushed into the AWS using the following commands:
<b>terraform init</b> - To initialize the terraform
<b>terraform plan</b> - to preview the resources being deployed
<b>terrform apply</b> - deploy the resources
(Note: - Before deploying the resources, make sure to configure with AWS CLI, use your AWS credentials for programmatic user to configure into the system (using access key, and secret access key) and the cd to the terraform directory)
Once deployed verify the resources in Console.

<h3>Step 2</h3>
Use CloudFormation to provision the EC2, RDS, and Lambda Resources.
Using the provided Cloudformation yaml templates deploy the resources with the following commands;
For EC2-Stack -> aws cloudformation deploy --stack-name ec2-stack --template-file <file-name-ec2.yaml> --parameter-overrides KeyName=<key-value-pair> --region us-east-1
For RDS-Stack -> aws cloudformation deploy --stack-name rds-stack --template-file <file-name-rds.yaml> --region us-east-1
For Lambda-Stack -> aws cloudformation deploy --stack-name lambda-stack --template-file <file-name-lambda.yaml> --capabilities CAPABILITY_NAMED_IAM --region us-east-1
Once, all the Cloudformation stacks are deployed, verify in the console.
