import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# AWS Cognito configuration
COGNITO_USER_POOL_ID = os.getenv("COGNITO_USER_POOL_ID")
COGNITO_APP_CLIENT_ID = os.getenv("COGNITO_CLIENT_ID")
COGNITO_APP_CLIENT_SECRET = os.getenv("COGNITO_CLIENT_SECRET")
COGNITO_USER_POOL_DOMAIN = os.getenv("COGNITO_USER_POOL_DOMAIN")
COGNITO_REDIRECT_URI = os.getenv("COGNITO_REDIRECT_URI")

# Flask session secret
SESSION_SECRET = os.getenv("SESSION_SECRET")
