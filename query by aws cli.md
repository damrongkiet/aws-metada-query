## Metadata of AWS Resources
  In AWS, metadata refers to additional information about your resources. It acts as a data about data, providing details about the configuration, state, and properties of AWS resources. Such as EC2 resource, there are various data that describe an instance properties ie. name, instance-id, tag, public ip, private ip, subnet, image id.
We can query these metadata for detail or investigate if need. In this document we'll use AWS CLI tool on Ubuntu Linux to do a job.

### Step by Stey
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

4. query metadata of ec2 instance
- no specifiy any ec2 instance id
  ```
  aws ec2 describe-instances --query 'Reservations[*]'
  ```
- specify ec2 instance id
  ```
  export EC2ID=i-0a4xxxxx
  aws ec2 describe-instances --query 'Reservations[*]'  --filters Name=instance-id,Values=$EC2ID
  ```
- query public ip address
  ```
  aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId, PublicIpAddress]' --filters Name=instance-id,Values=$EC2ID
  ```
- query tags metadata
  ```
  aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId, Tags]' --filters "Name=tag:Name,Values=financial"
  ```

Notes

Default output of aws command is json format. However we can explicit this by add `--output json`.
```
aws ec2 describe-instances --query 'Reservations[*]'  --filters Name=instance-id,Values=$EC2ID --output json
```
