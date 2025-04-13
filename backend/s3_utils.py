import os
import boto3
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)

BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

def upload_file(file_path, s3_key):
    s3.upload_file(file_path, BUCKET_NAME, s3_key)
    print(f"Uploaded {file_path} to s3://{BUCKET_NAME}/{s3_key}")

def download_file(s3_key, destination_path):
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    s3.download_file(BUCKET_NAME, s3_key, destination_path)
    print(f"Downloaded s3://{BUCKET_NAME}/{s3_key} to {destination_path}")
