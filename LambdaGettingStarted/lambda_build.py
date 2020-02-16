import boto3
import logging
import sys

def lambda_build(LambdaFunctionName, iamRole):
    client = boto3.client('lambda')

    create_lambda_function = client.create_function(
        FunctionName=LambdaFunctionName,
        Runtime='python3.7',
        Role=iamRole,
        Handler='{}.lambda_handler'.format('lambda_build'),
        Description='Start a virtual machine',
				Code = {'S3Bucket':'name_of_your_s3_bucket', 'S3Key':'file_name_of_zipped_python_code'}
    )

LambdaFunctionName = sys.argv[1]
iamRole = sys.argv[2]

lambda_build(LambdaFunctionName, iamRole)

## python .\lambda_build.py 'name_of_your_lambda_function' 'arn_of_your_lambda_role'