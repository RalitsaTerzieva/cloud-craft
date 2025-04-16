import boto3
from datetime import datetime, timezone

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("cloud-craft-app")

def save_file_metadata(filename, s3_key, user_email=None):
    table.put_item(
        Item={
            'filename': filename,
            's3_key': s3_key,
            'uploaded_at': datetime.now(timezone.utc).isoformat()
,
            'user_email': user_email or "anonymous"
        }
    )
    print(f"Metadata saved for: {filename}")
