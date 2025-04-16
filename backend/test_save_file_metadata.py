from dotenv import load_dotenv
import os
import boto3
from datetime import datetime, timezone


load_dotenv()


table_name = os.getenv("DYNAMODB_TABLE_NAME", "cloud-craft-app")
region = os.getenv("AWS_REGION", "eu-central-1")


dynamodb = boto3.resource("dynamodb", region_name=region)
table = dynamodb.Table(table_name)

def save_file_metadata(filename, s3_key, user_email=None):
    table.put_item(
        Item={
            'filename': filename,
            's3_key': s3_key,
            'uploaded_at': datetime.now(timezone.utc).isoformat(),
            'user_email': user_email or "anonymous"
        }
    )
    print(f"✅ Metadata saved for: {filename}")

def test_save_file_metadata():
    filename = "test_file.txt"
    s3_key = "test/path/test_file.txt"
    user_email = "testuser@example.com"
    save_file_metadata(filename, s3_key, user_email)

if __name__ == "__main__":
    test_save_file_metadata()
