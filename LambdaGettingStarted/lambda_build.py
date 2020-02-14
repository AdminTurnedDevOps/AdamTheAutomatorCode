import boto3
import log
import sys

client = boto3.client('lambda')

create_lambda_function = client.create_function(
    FunctionName=LambdafunctionName,
    Runtime='python3.7',
    # The role is the IAM role you created that has access to kick off the Lambda Function. You need to put in the ARN
    Role=iamRole,
    Handler='{}.lambda_handler'.format(PythonfunctionName),
    # The code below is some sample code. This will pull all of your S3 bucket names
    Description='Print out all S3 bucket names'
)
