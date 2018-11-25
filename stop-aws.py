import boto3
import yaml
import subprocess
from botocore.exceptions import ClientError

f = open('awsconf.yml', 'r+')
awsconf = yaml.load(f)

ec2 = boto3.client('ec2')

# Stop EC2 instance
response = ec2.stop_instances(
        InstanceIds=[
            awsconf['instanceid']
            ]
        )

print(response)


# Get GlobalIP of client machine
globalip = subprocess.check_output(['wget', '-q',
                                    '-O', '-', 'ipcheck.ieserver.net'])
globalip = globalip.decode('utf-8').strip() + '/32'
print(globalip)

# Remove client access rule
try:
    removeddata = ec2.revoke_security_group_ingress(
            GroupId=awsconf['securitygroupid'],
            IpPermissions=[
                {'IpProtocol': 'tcp',
                    'FromPort': 22,
                    'ToPort': 22,
                    'IpRanges': [{'CidrIp': globalip,
                                  'Description': awsconf['securitygrouprulename']}]}
                ])
    print('ingress SuccessFully removed %s' % removeddata)
except ClientError as e:
    print(e)
