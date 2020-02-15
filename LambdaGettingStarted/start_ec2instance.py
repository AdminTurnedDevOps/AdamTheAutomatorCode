import boto3

ec2 = boto3.client('ec2')

def start_ec2instance(event, context):
    
    ec2.start_instances(InstanceIds= ['i-07fb99ce1b5fb4446'])