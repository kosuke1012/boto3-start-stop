import boto3
import yaml
import subprocess
from botocore.exceptions import ClientError

f = open('awsconf.yml', 'r+')
awsconf = yaml.load(f)

ec2 = boto3.client('ec2')

# Get GlobalIP of client machine
globalip = subprocess.check_output(['wget', '-q', '-O', '-', 'ipcheck.ieserver.net'])
globalip = globalip.decode('utf-8').strip() + '/32'
print(globalip)

# Allow client access for specific security group
try:
    data = ec2.authorize_security_group_ingress(
            GroupId=awsconf['securitygroupid'],
            IpPermissions=[
                {'IpProtocol': 'tcp',
                    'FromPort': 22,
                    'ToPort': 22,
                    'IpRanges': [{'CidrIp': globalip,
                                 'Description': awsconf['securitygrouprulename']}]}
                ])
    print('ingress SuccessFully Set %s' % data)
except ClientError as e:
    print(e)

# Start EC2 instance
response = ec2.start_instances(
        InstanceIds=[
            awsconf['instanceid']
            ]
        )

print(response)
