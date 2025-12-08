<h1>Deploying a Scalable AWS Architecture with Infrastructure as Code.</h1>
<h3>Step 1</h3>
The project begins from creation of Networking resources using Terraform. First the Networking resource components like VPC, Subnets, Route tables, Associations, IGW (Internet Gateway), and Security Groups are created using terraform.
The terraform files are pushed into the AWS using the following commands:
<n><b>terraform init</b> - To initialize the terraform</n>
<n><b>terraform plan</b> - to preview the resources being deployed</n>
<n><b>terrform apply</b> - deploy the resources</n>
(Note: - Before deploying the resources, make sure to configure with AWS CLI, use your AWS credentials for programmatic user to configure into the system (using access key, and secret access key) and the cd to the terraform directory)
Once deployed verify the resources in Console.

<h3>Step 2</h3>
Use CloudFormation to provision the EC2, RDS, and Lambda Resources.
