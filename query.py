import boto3
import json
import sys
import botocore.exceptions

def get_ec2_metadata(instance_id=None, metadata_names=None):
    ec2_client = boto3.client('ec2')

    try:
        if instance_id:
            response = ec2_client.describe_instances(InstanceIds=[instance_id])
        else:
            response = ec2_client.describe_instances()

        instances_metadata = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_info = {
                    'InstanceId': instance['InstanceId'],
                    'State': instance['State']['Name'],
                    'Type': instance['InstanceType'],
                    'AMI_ID': instance['ImageId'],
                    'PublicIP': instance.get('PublicIpAddress', 'N/A'),
                    'PrivateIP': instance.get('PrivateIpAddress', 'N/A'),
                    'SubnetId': instance.get('SubnetId', 'N/A'),
                    'SecurityGroups': [sg['GroupName'] for sg in instance.get('SecurityGroups', [])],
                    'Volumes': [vol['Ebs']['VolumeId'] for vol in instance.get('BlockDeviceMappings', []) if 'Ebs' in vol],
                    'Tags': instance.get('Tags', []),
                    'LaunchTime': str(instance['LaunchTime']),
                    'IAMInstanceProfile': instance.get('IamInstanceProfile', {}).get('Arn', 'N/A'),
                    'Monitoring': instance.get('Monitoring', {}).get('State', 'N/A'),
                }

                if metadata_names:
                    filtered_metadata = {key: instance_info[key] for key in metadata_names if key in instance_info}
                    if filtered_metadata:
                        instances_metadata.append(filtered_metadata)
                else:
                    instances_metadata.append(instance_info)

        return json.dumps(instances_metadata, indent=4)

    except botocore.exceptions.ClientError as e:
        return json.dumps({"Error": str(e)}, indent=4)
    except Exception as e:
        return json.dumps({"Error": f"Unexpected error: {str(e)}"}, indent=4)

if __name__ == "__main__":
    instance_id = sys.argv[1] if len(sys.argv) > 1 else None
    metadata_names = sys.argv[2:] if len(sys.argv) > 2 else None
    print(get_ec2_metadata(instance_id, metadata_names))