# boto3-start-stop
Start/Stop ec2 instances via boto3. Add a inbound rules with your client's IP, and then start ec2.

## Requirement
### Install AWS CLI
Install AWS CLI.
<https://docs.aws.amazon.com/cli/latest/userguide/installing.html>   
```
$ pip install awscli --upgrade --user
```

### Configure AWS CLI
Configure AWS CLI
<https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html>  
```
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-west-2
Default output format [None]: json
```
### Install Boto3
Install Boto3.
<https://aws.amazon.com/sdk-for-python/>  
```
$ pip install boto3
```
### Setup conf file
Replace awsconf.yml with your securitygroupid, securitygrouprulename, instansid and rsapath(used for generate ssh command)


