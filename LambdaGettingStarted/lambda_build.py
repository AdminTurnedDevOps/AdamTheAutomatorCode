import boto3
import logging
import sys

def lambda_build(LambdafunctionName, iamRole):
    client = boto3.client('lambda')

    create_lambda_function = client.create_function(
        FunctionName=LambdafunctionName,
        Runtime='python3.7',
        Role=iamRole,
        Handler='{}.lambda_handler'.format('lambda_build'),
        Description='Start a virtual machine',
        Code = {'S3Bucket':'clouddev.engineering', 'S3Key': 'start_ec2instance.py'}
    )

LambdafunctionName = sys.argv[1]
iamRole = sys.argv[2]

lambda_build(LambdafunctionName, iamRole)