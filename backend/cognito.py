import boto3
from botocore.exceptions import ClientError
from config import COGNITO_APP_CLIENT_ID, COGNITO_USER_POOL_ID, COGNITO_USER_POOL_DOMAIN, COGNITO_REDIRECT_URI

# Initialize the Cognito client
cognito_client = boto3.client('cognito-idp')

def sign_up_user(email, password):
    """Sign up a new user"""
    try:
        response = cognito_client.sign_up(
            ClientId=COGNITO_APP_CLIENT_ID,
            Username=email,
            Password=password,
            UserAttributes=[{
                'Name': 'email',
                'Value': email
            }]
        )
        return response
    except ClientError as e:
        print(f"Error signing up: {e}")
        return None

def authenticate_user(email, password):
    """Authenticate user using email and password"""
    try:
        response = cognito_client.initiate_auth(
            ClientId=COGNITO_APP_CLIENT_ID,
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': email,
                'PASSWORD': password
            }
        )
        return response['AuthenticationResult']
    except ClientError as e:
        print(f"Error during authentication: {e}")
        return None

def get_user_info(access_token):
    """Retrieve user information from Cognito using the access token"""
    try:
        response = cognito_client.get_user(
            AccessToken=access_token
        )
        return response
    except ClientError as e:
        print(f"Error fetching user info: {e}")
        return None
