import os
import boto3
from dotenv import load_dotenv

load_dotenv()

sqs = boto3.client(
    'sqs',
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

QUEUE_URL = os.getenv("AWS_SQS_QUEUE_URL")

def send_message_to_queue(file_name, user_email):
    message = {
        'file_name': file_name,
        'user_email': user_email
    }
    
    response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=str(message)
    )
    
    print("Message sent to SQS:", response['MessageId'])
