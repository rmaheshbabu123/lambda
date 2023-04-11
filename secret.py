import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    # Create a client for AWS Secret Manager
    client = boto3.client('secretsmanager', region_name='us-east-1')

    # Retrieve the secret value from Secret Manager
    response = client.get_secret_value(SecretId='my_secret')

    # Extract the secret value from the response
    secret_value = response['SecretString']

    # Do something with the secret value
    print(secret_value)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
