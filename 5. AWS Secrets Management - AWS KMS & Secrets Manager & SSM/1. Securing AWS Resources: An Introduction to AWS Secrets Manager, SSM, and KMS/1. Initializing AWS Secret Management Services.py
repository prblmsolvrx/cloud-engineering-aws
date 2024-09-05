"""
AWS offers multiple services for managing secrets, such as AWS Secrets Manager,
AWS Systems Manager Parameter Store (SSM), and AWS Key Management Service (KMS).
These services can be utilized via the Boto3 SDK. They must first be initialized
as clients before you can start using them. Your task is to run a Python script
that initializes these clients both in their default manner and through a custom session.
Simply run the code, verify that it initializes the services by observing the
print statements, and ensure that you are getting no errors.
"""

import boto3

# Create default Secrets Manager client
secrets_manager_default = boto3.client('secretsmanager')
print("Default Secrets Manager client initialized.")

# Create default Parameter Store (SSM) client
ssm_default = boto3.client('ssm')
print("Default Parameter Store (SSM) client initialized.")

# Create default KMS client
kms_default = boto3.client('kms')
print("Default KMS client initialized.")

# Create custom session
my_session = boto3.Session(
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-west-2'
)

# Create Secrets Manager client based on this session
secrets_manager_custom = my_session.client('secretsmanager')
print("Custom Secrets Manager client initialized.")

# Create Parameter Store (SSM) client based on this session
ssm_custom = my_session.client('ssm')
print("Custom Parameter Store (SSM) client initialized.")

# Create KMS client based on this session
kms_custom = my_session.client('kms')
print("Custom KMS client initialized.")