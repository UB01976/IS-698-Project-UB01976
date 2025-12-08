
<h1>Project</h1> - <h1>Deploying a Scalable AWS Architecture with Infrastructure as Code.</h1>

<h1>Overview</h1>
This project demonstrates building a Scalable web application on AWS using a mix of IaC tools.

The system consists of following resource components:
- Terraform to create VPC, subnets, route tables, and security groups
- Cloudformation to Deploy EC2, RDS, and Lambda
- RDS MySQL database integrated with EC2
- Auto Scaling Group creation
- Lambda function triggered by S3 uploads
- AWS CLI and Python Boto3 scripts for AWS interaction



<h3>Step 1</h3>
<b>The project begins from creation of Networking resources using Terraform.</b><br/>
First the Networking resource components like VPC, Subnets, Route tables, Associations, IGW (Internet Gateway), and Security Groups are created using terraform.
The terraform files are pushed into the AWS using the following commands:<br/>
<b>terraform init</b> - To initialize the terraform<br/>
<b>terraform plan</b> - to preview the resources being deployed<br/>
<b>terrform apply</b> - deploy the resources<br/>
(Note: - Before deploying the resources, make sure to configure with AWS CLI, use your AWS credentials for programmatic user to configure into the system (using access key, and secret access key) and the cd to the terraform directory)
Once deployed verify the resources in Console.

<h3>Step 2</h3>
<b>Use CloudFormation to provision the EC2, RDS, and Lambda Resources.</b>
Using the provided Cloudformation yaml templates deploy the resources with the following commands;<br/>
For EC2-Stack:  aws cloudformation deploy --stack-name ec2-stack --template-file {file-name-ec2.yaml} --parameter-overrides KeyName={key-value-pair} --region us-east-1  <br/>
For RDS-Stack:  aws cloudformation deploy --stack-name rds-stack --template-file <file-name-rds.yaml> --region us-east-1  <br/>
For Lambda-Stack:  aws cloudformation deploy --stack-name lambda-stack --template-file <file-name-lambda.yaml> --capabilities CAPABILITY_NAMED_IAM --region us-east-1  <br/>
Once, all the Cloudformation stacks are deployed, verify in the console.

<h3>Step 3</h3>
<b>Deploy a Web Application on EC2 <br/></b>
Run the Following yaml template (Shashank-puppala-ec2-static-webpage-project.yaml) to display a static Web page on the browser.
Use the following command to deploy the stack <br/>
aws cloudformation deploy --stack-name ec2-stack --template-file {file-name-ec2-static.yaml} --parameter-overrides KeyName={key-pair-value} --region us-east-1

<h3>Step 4</h3>
<b>Configure the database backend for the application.</b>
Get the RDS endpoints from the Console and SSH into the instance using;<br/>
ssh -i {Key_Value_Pair} ec2-user@{Public_IP} <br/>
Then run the following commands; <br/>
  
sudo yum update –y <br/>
sudo dnf install mariadb105 -y <br/>
sudo systemctl enable httpd <br/>
sudo systemctl start httpd <br/>
mysql -h {RDS-endpoint} -u {username} -p <br/>

Once Database is installed into the EC2 instance, insert the employee data that has to be displayed: <br/>
CREATE TABLE employees (Id INT  PRIMARY KEY, Name VARCHAR(50) NOT NULL, email VARCHAR(100), Department VARCHAR(50) );<br/>

INSERT INTO employees (Id, name, email, Department) VALUES (1, ‘test', 'test@example.com', ‘IS’); <br/>

Use the php file to display the inserted data and restart using the command: <br/>
sudo systemctl restart httpd <br/>

Verify the output on the browser.

<h3>Step 5</h3>
<b>Implement autoscaling for EC2 instances.</b>
Steps to Create Web Server Instance – 
1.	Go to EC2 on Console → Click on Instances → Select Launch Instance <br/>
2.	Set:<br/>
    Name: WebServer-Base<br/>
    AMI: Amazon Linux 2 (ex: - ami-0fa3fe0fa7920f68e)<br/>
    Instance Type: t3.micro<br/>
    Key Pair: Select existing from your Account<br/>
    Network: Choose public subnet which we have created for web server <br/>
    Auto-assign Public IP: Enabled<br/>
  Security Group: Select the web server sg created using Terraform (Which allows SSH (from 22) & HTTP (80)<br/>
3.	Launch the instance.<br/>

Step 2 would be creating the AMI Image of the instance;<br/>
1.	Select the instance → Actions → Image → Create Image<br/>
2.	Name the AMI: Provide a Name to the Image <br/>
3.	Click Create Image<br/>
4.	Wait until status is “available.”<br/>

Step 3: - Create a Launch Template<br/>
1.	Go to EC2 → Launch Templates → Create Template<br/>
2.	Use the created AMI from the above step once it is available.<br/>
3.	Set instance type and security group (Web-sg).<br/>
4.	Note: - Do not select any subnet while creation.<br/>
5.	Create a template.<br/>

Step 4: - ALB and Target Groups
For Target Group creation: -<br/>
1.	Go to EC2 → Target Groups → Create<br/>
2.	Choose  Instance target type.<br/>
3.	Select Protocol:HTTP1 <br/>
4.	Set port 80 , Name the Target group , and health check path  to /.<br/>
5.	Note: - Do not register targets manually; autoscaling will allocate automated resources.<br/>

Next for ALB creation;
1.	Go to EC2 → Load Balancers → Create ALB <br/>
2.	Name ALB (Application Load Balancing)<br/>
3.	Select the Scheme: Internet-facing<br/>
4.	Listeners: HTTP 80<br/>
5.	Subnets: Select Two public subnets in different AZs (Which we have created in the earlier steps using terraform)<br/>
6.	Security Group: ALB-SG<br/>
7.	Attach the previously created Target Group from the above step.<br/>
8.	Click Create Load Balancer and wait until it is active.<br/>

Step 5: - Creation of Auto Scaling Group (ASG)<br/>
1.	Go to EC2 → Select Auto Scaling Groups → Click on Create<br/>
2.	Select the Launch Template which you created earlier.<br/>
3.	Select the VPC and 2 of the public subnets (Created before, the custom VPC from terraform and respective 2 public subnets in different availability zones).<br/>
4.	Attach to the ALB by selecting the Target Group.<br/>
5.	Set capacities: Minimum: 1<br/>
                    Maximum: 3<br/>
6.	Click Next and Click on Create Auto Scaling Group.<br/>

Auto Scaling Policy:<br/>
1.	Open ASG → Click on Automatic Scaling → Add Policy<br/>
2.	Select Target Tracking Policy<br/>
3.	Choose Average CPU Utilization<br/>
4.	Set target threshold (e.g., 30–50%).<br/>
5.	Save policy.<br/>

Run the following commands to stress test the system:<br/>
sudo yum install -y stress<br/>
stress –cpu 4 –timeout 60 <br/>









