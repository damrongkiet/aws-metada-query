## This file is an instruction how to query metadata of AWS EC2 instances with python code
In AWS, metadata refers to additional information about your resources. It acts as a data about data, providing details about the configuration, 
state, and properties of AWS resources. Such as EC2 resource, there are various data that describe an instance properties ie. name, instance-id, 
tag, public ip, private ip, subnet, image id. We can query these metadata for detail or investigate if need. In this document we'll use Python on Ubuntu Linux to do a job.

### Step by Step
1. install aws cli tool
   ```
   curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
   unzip awscliv2.zip
   sudo ./aws/install
   ```
2. setup aws credentials
   ```
   export AWS_ACCESS_KEY_ID="AKIAQ..."
   export AWS_SECRET_ACCESS_KEY="j8NoF4..."
   ```
3. verify installation is successful
   ```
   aws sts get-caller-identity
   aws s3 ls
   ```
4. create 2 ec2 instances with tag
   ```
   aws ec2 run-instances --image-id ami-001c2a00563d136eb --count 1 \
    --instance-type t2.micro --key-name key-for-myvm \
    --security-group-ids sg-080710eb061ca382b \
    --subnet-id subnet-0a8dbbb82559dd9aa \
	  --tag-specifications 'ResourceType=instance,Tags=[{Key=project,Value=cs-01}]'

   aws ec2 run-instances --image-id ami-001c2a00563d136eb --count 1 \
    --instance-type t2.micro --key-name key-for-myvm \
    --security-group-ids sg-080710eb061ca382b \
    --subnet-id subnet-0a8dbbb82559dd9aa \
	  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=financial},{Key=project,Value=cs-01}]'
   ```
5. clone this repo and setup python environment
   ```
   git clone https://github.com/damrongkiet/aws-metada-query
   cd aws-metada-query
   python3 -m venv .
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
6. query metadata of ec2 instance
   - no specifiy any ec2 instance id
     ```
     python query.py
     ```
     ```
      [
          {
              "InstanceId": "i-0bbb2de8b85c2c90d",
              "State": "running",
              "Type": "t2.micro",
              "AMI_ID": "ami-001c2a00563d136eb",
              "PublicIP": "47.129.236.182",
              "PrivateIP": "172.31.31.186",
              "SubnetId": "subnet-0a8dbbb82559dd9aa",
              "SecurityGroups": [
                  "default"
              ],
              "Volumes": [
                  "vol-04a12d86f2145ef45"
              ],
              "Tags": [
                  {
                      "Key": "project",
                      "Value": "cs-01"
                  }
              ],
              "LaunchTime": "2025-04-25 07:03:59+00:00",
              "IAMInstanceProfile": "N/A",
              "Monitoring": "disabled"
          },
          {
              "InstanceId": "i-088073f4ebda28161",
              "State": "running",
              "Type": "t2.micro",
              "AMI_ID": "ami-001c2a00563d136eb",
              "PublicIP": "13.229.104.53",
              "PrivateIP": "172.31.18.180",
              "SubnetId": "subnet-0a8dbbb82559dd9aa",
              "SecurityGroups": [
                  "default"
              ],
              "Volumes": [
                  "vol-0cd4c62b4fa70e868"
              ],
              "Tags": [
                  {
                      "Key": "Name",
                      "Value": "financial"
                  },
                  {
                      "Key": "project",
                      "Value": "cs-01"
                  }
              ],
              "LaunchTime": "2025-04-25 06:57:45+00:00",
              "IAMInstanceProfile": "N/A",
              "Monitoring": "disabled"
          }
      ]
     ```
   - specify ec2 instance id
     ```
     python query.py i-0bbb2de8b85c2c90d
     ```
     ```
      [
          {
              "InstanceId": "i-0bbb2de8b85c2c90d",
              "State": "running",
              "Type": "t2.micro",
              "AMI_ID": "ami-001c2a00563d136eb",
              "PublicIP": "47.129.236.182",
              "PrivateIP": "172.31.31.186",
              "SubnetId": "subnet-0a8dbbb82559dd9aa",
              "SecurityGroups": [
                  "default"
              ],
              "Volumes": [
                  "vol-04a12d86f2145ef45"
              ],
              "Tags": [
                  {
                      "Key": "project",
                      "Value": "cs-01"
                  }
              ],
              "LaunchTime": "2025-04-25 07:03:59+00:00",
              "IAMInstanceProfile": "N/A",
              "Monitoring": "disabled"
          }
      ]
     ```
   - specify ec2 instance id and list of metadata
     ```
     python query.py i-0bbb2de8b85c2c90d Type AMI_ID PublicIP Tags
     ```
     ```
      [
          {
              "Type": "t2.micro",
              "AMI_ID": "ami-001c2a00563d136eb",
              "PublicIP": "47.129.236.182",
              "Tags": [
                  {
                      "Key": "project",
                      "Value": "cs-01"
                  }
              ]
          }
      ]
     ```