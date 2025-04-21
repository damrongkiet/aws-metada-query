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

4. create ec2 instance and tag
```
aws ec2 run-instances --image-id ami-001c2a00563d136eb --count 1 \
--instance-type t2.micro --key-name <key_name> \
--security-group-ids <sg_group_id_xxx> \
--subnet-id <subnet_id_xxx>

aws ec2 create-tags \
--resources i-0c97ab48f7855d88f \
--tags 'Key="Name",Value=financial'
```

5. query metadata of ec2 instance
- no specifiy any ec2 instance id
  ```
  aws ec2 describe-instances --query 'Reservations[*]'
  ```
  ```
  [
    {
        "Groups": [],
        "Instances": [
            {
                "AmiLaunchIndex": 0,
                "ImageId": "ami-001c2a00563d136eb",
                "InstanceId": "i-0c97ab48f7855d88f",
                "InstanceType": "t2.micro",
                "KeyName": "key-for-myvm",
                "LaunchTime": "2025-04-21T14:50:14+00:00",
                "Monitoring": {
                    "State": "disabled"
                },
                "Placement": {
                    "AvailabilityZone": "ap-southeast-1a",
                    "GroupName": "",
                    "Tenancy": "default"
                },
                "PrivateDnsName": "ip-172-31-20-138.ap-southeast-1.compute.internal",
                "PrivateIpAddress": "172.31.20.138",
                "ProductCodes": [],
                "PublicDnsName": "ec2-18-136-119-118.ap-southeast-1.compute.amazonaws.com",
                "PublicIpAddress": "18.136.119.118",
                "State": {
                    "Code": 16,
                    "Name": "running"
                },
                "StateTransitionReason": "",
                "SubnetId": "subnet-0a8dbbb82559dd9aa",
                "VpcId": "vpc-0489e52138c11e68e",
                "Architecture": "x86_64",
                "BlockDeviceMappings": [
                    {
                        "DeviceName": "/dev/sda1",
                        "Ebs": {
                            "AttachTime": "2025-04-21T14:50:15+00:00",
                            "DeleteOnTermination": true,
                            "Status": "attached",
                            "VolumeId": "vol-08f19c2a6effe9776"
                        }
                    }
                ],
                "ClientToken": "c0e15935-1039-4dc3-8dc5-ceee17b2fead",
                "EbsOptimized": false,
                "EnaSupport": true,
                "Hypervisor": "xen",
                "NetworkInterfaces": [
                    {
                        "Association": {
                            "IpOwnerId": "amazon",
                            "PublicDnsName": "ec2-18-136-119-118.ap-southeast-1.compute.amazonaws.com",
                            "PublicIp": "18.136.119.118"
                        },
                        "Attachment": {
                            "AttachTime": "2025-04-21T14:50:14+00:00",
                            "AttachmentId": "eni-attach-0cd66fc0f4a9eb9fe",
                            "DeleteOnTermination": true,
                            "DeviceIndex": 0,
                            "Status": "attached",
                            "NetworkCardIndex": 0
                        },
                        "Description": "",
                        "Groups": [
                            {
                                "GroupName": "default",
                                "GroupId": "sg-080710eb061ca382b"
                            }
                        ],
                        "Ipv6Addresses": [],
                        "MacAddress": "02:c8:f2:59:35:a5",
                        "NetworkInterfaceId": "eni-0e1e8f3ddc7ba769c",
                        "OwnerId": "367906484832",
                        "PrivateDnsName": "ip-172-31-20-138.ap-southeast-1.compute.internal",
                        "PrivateIpAddress": "172.31.20.138",
                        "PrivateIpAddresses": [
                            {
                                "Association": {
                                    "IpOwnerId": "amazon",
                                    "PublicDnsName": "ec2-18-136-119-118.ap-southeast-1.compute.amazonaws.com",
                                    "PublicIp": "18.136.119.118"
                                },
                                "Primary": true,
                                "PrivateDnsName": "ip-172-31-20-138.ap-southeast-1.compute.internal",
                                "PrivateIpAddress": "172.31.20.138"
                            }
                        ],
                        "SourceDestCheck": true,
                        "Status": "in-use",
                        "SubnetId": "subnet-0a8dbbb82559dd9aa",
                        "VpcId": "vpc-0489e52138c11e68e",
                        "InterfaceType": "interface"
                    }
                ],
                "RootDeviceName": "/dev/sda1",
                "RootDeviceType": "ebs",
                "SecurityGroups": [
                    {
                        "GroupName": "default",
                        "GroupId": "sg-080710eb061ca382b"
                    }
                ],
                "SourceDestCheck": true,
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "financial"
                    }
                ],
                "VirtualizationType": "hvm",
                "CpuOptions": {
                    "CoreCount": 1,
                    "ThreadsPerCore": 1
                },
                "CapacityReservationSpecification": {
                    "CapacityReservationPreference": "open"
                },
                "HibernationOptions": {
                    "Configured": false
                },
                "MetadataOptions": {
                    "State": "applied",
                    "HttpTokens": "optional",
                    "HttpPutResponseHopLimit": 1,
                    "HttpEndpoint": "enabled",
                    "HttpProtocolIpv6": "disabled",
                    "InstanceMetadataTags": "disabled"
                },
                "EnclaveOptions": {
                    "Enabled": false
                },
                "BootMode": "uefi-preferred",
                "PlatformDetails": "Linux/UNIX",
                "UsageOperation": "RunInstances",
                "UsageOperationUpdateTime": "2025-04-21T14:50:14+00:00",
                "PrivateDnsNameOptions": {
                    "HostnameType": "ip-name",
                    "EnableResourceNameDnsARecord": false,
                    "EnableResourceNameDnsAAAARecord": false
                },
                "MaintenanceOptions": {
                    "AutoRecovery": "default"
                },
                "CurrentInstanceBootMode": "legacy-bios"
            }
        ],
        "OwnerId": "367906484832",
        "ReservationId": "r-0e619f539fd7b5784"
    }
  ]
  ```
- specify ec2 instance id
  ```
  export EC2ID=i-0c97ab48f7855d88f
  aws ec2 describe-instances --query 'Reservations[*]'  --filters Name=instance-id,Values=$EC2ID
  ```
  ```
  [
    {
        "Groups": [],
        "Instances": [
            {
                "AmiLaunchIndex": 0,
                "ImageId": "ami-001c2a00563d136eb",
                "InstanceId": "i-0c97ab48f7855d88f",
                "InstanceType": "t2.micro",
                "KeyName": "key-for-myvm",
                "LaunchTime": "2025-04-21T14:50:14+00:00",
                "Monitoring": {
                    "State": "disabled"
                },
                "Placement": {
                    "AvailabilityZone": "ap-southeast-1a",
                    "GroupName": "",
                    "Tenancy": "default"
                },
                "PrivateDnsName": "ip-172-31-20-138.ap-southeast-1.compute.internal",
                "PrivateIpAddress": "172.31.20.138",
                "ProductCodes": [],
                "PublicDnsName": "ec2-18-136-119-118.ap-southeast-1.compute.amazonaws.com",
                "PublicIpAddress": "18.136.119.118",
                "State": {
                    "Code": 16,
                    "Name": "running"
                },
                "StateTransitionReason": "",
                "SubnetId": "subnet-0a8dbbb82559dd9aa",
                "VpcId": "vpc-0489e52138c11e68e",
                "Architecture": "x86_64",
                "BlockDeviceMappings": [
                    {
                        "DeviceName": "/dev/sda1",
                        "Ebs": {
                            "AttachTime": "2025-04-21T14:50:15+00:00",
                            "DeleteOnTermination": true,
                            "Status": "attached",
                            "VolumeId": "vol-08f19c2a6effe9776"
                        }
                    }
                ],
                "ClientToken": "c0e15935-1039-4dc3-8dc5-ceee17b2fead",
                "EbsOptimized": false,
                "EnaSupport": true,
                "Hypervisor": "xen",
                "NetworkInterfaces": [
                    {
                        "Association": {
                            "IpOwnerId": "amazon",
                            "PublicDnsName": "ec2-18-136-119-118.ap-southeast-1.compute.amazonaws.com",
                            "PublicIp": "18.136.119.118"
                        },
                        "Attachment": {
                            "AttachTime": "2025-04-21T14:50:14+00:00",
                            "AttachmentId": "eni-attach-0cd66fc0f4a9eb9fe",
                            "DeleteOnTermination": true,
                            "DeviceIndex": 0,
                            "Status": "attached",
                            "NetworkCardIndex": 0
                        },
                        "Description": "",
                        "Groups": [
                            {
                                "GroupName": "default",
                                "GroupId": "sg-080710eb061ca382b"
                            }
                        ],
                        "Ipv6Addresses": [],
                        "MacAddress": "02:c8:f2:59:35:a5",
                        "NetworkInterfaceId": "eni-0e1e8f3ddc7ba769c",
                        "OwnerId": "367906484832",
                        "PrivateDnsName": "ip-172-31-20-138.ap-southeast-1.compute.internal",
                        "PrivateIpAddress": "172.31.20.138",
                        "PrivateIpAddresses": [
                            {
                                "Association": {
                                    "IpOwnerId": "amazon",
                                    "PublicDnsName": "ec2-18-136-119-118.ap-southeast-1.compute.amazonaws.com",
                                    "PublicIp": "18.136.119.118"
                                },
                                "Primary": true,
                                "PrivateDnsName": "ip-172-31-20-138.ap-southeast-1.compute.internal",
                                "PrivateIpAddress": "172.31.20.138"
                            }
                        ],
                        "SourceDestCheck": true,
                        "Status": "in-use",
                        "SubnetId": "subnet-0a8dbbb82559dd9aa",
                        "VpcId": "vpc-0489e52138c11e68e",
                        "InterfaceType": "interface"
                    }
                ],
                "RootDeviceName": "/dev/sda1",
                "RootDeviceType": "ebs",
                "SecurityGroups": [
                    {
                        "GroupName": "default",
                        "GroupId": "sg-080710eb061ca382b"
                    }
                ],
                "SourceDestCheck": true,
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "financial"
                    }
                ],
                "VirtualizationType": "hvm",
                "CpuOptions": {
                    "CoreCount": 1,
                    "ThreadsPerCore": 1
                },
                "CapacityReservationSpecification": {
                    "CapacityReservationPreference": "open"
                },
                "HibernationOptions": {
                    "Configured": false
                },
                "MetadataOptions": {
                    "State": "applied",
                    "HttpTokens": "optional",
                    "HttpPutResponseHopLimit": 1,
                    "HttpEndpoint": "enabled",
                    "HttpProtocolIpv6": "disabled",
                    "InstanceMetadataTags": "disabled"
                },
                "EnclaveOptions": {
                    "Enabled": false
                },
                "BootMode": "uefi-preferred",
                "PlatformDetails": "Linux/UNIX",
                "UsageOperation": "RunInstances",
                "UsageOperationUpdateTime": "2025-04-21T14:50:14+00:00",
                "PrivateDnsNameOptions": {
                    "HostnameType": "ip-name",
                    "EnableResourceNameDnsARecord": false,
                    "EnableResourceNameDnsAAAARecord": false
                },
                "MaintenanceOptions": {
                    "AutoRecovery": "default"
                },
                "CurrentInstanceBootMode": "legacy-bios"
            }
        ],
        "OwnerId": "367906484832",
        "ReservationId": "r-0e619f539fd7b5784"
    }
  ]
  ```
  
- query public ip address
  ```
  aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId, PublicIpAddress]' --filters Name=instance-id,Values=$EC2ID
  ```
  ```
  [
    [
        [
            "i-0c97ab48f7855d88f",
            "18.136.119.118"
        ]
    ]
  ]
  ```
- query tags metadata
  ```
  aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId, Tags]' --filters "Name=tag:Name,Values=financial"
  ```
  ```
  [
    [
        [
            "i-0c97ab48f7855d88f",
            [
                {
                    "Key": "Name",
                    "Value": "financial"
                }
            ]
        ]
    ]
  ]
  ```

Notes

Default output of aws command is json format. However we can explicit this by add `--output json`.
```
aws ec2 describe-instances --query 'Reservations[*]'  --filters Name=instance-id,Values=$EC2ID --output json
```
