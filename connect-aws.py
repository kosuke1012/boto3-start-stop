import boto3
import yaml
import subprocess
from botocore.exceptions import ClientError

f = open("awsconf.yml","r+")
awsconf = yaml.load(f)

ec2 = boto3.client('ec2')

res = ec2.describe_instances(
        InstanceIds=[
            awsconf['instanceid']
            ]
        )

publicDnsName = res['Reservations'][0]['Instances'][0]['PublicDnsName']

print("ssh -i " + awsconf['rsapath'] + " ubuntu@" + publicDnsName)
#subprocess.check_output(["ssh","-i",awsconf['rsapath'],"ubuntu@"+ publicDnsName])

