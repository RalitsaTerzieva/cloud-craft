import express from 'express';
import { ReceiveMessageCommand, DeleteMessageCommand, SQSClient, SendMessageCommand } from '@aws-sdk/client-sqs';

const app = express();
app.use(express.json());

const sqs = new SQSClient({ region: 'us-east-1' });

app.post('/send-to-queue', async (req, res) => {
  const { file_name, user_email } = req.body;
  const params = {
    QueueUrl: process.env.SQS_QUEUE_URL,
    MessageBody: JSON.stringify({ file_name, user_email }),
  };

  try {
    const command = new SendMessageCommand(params);
    await sqs.send(command);
    res.json({ message: 'Message sent to SQS' });
  } catch (err) {
    console.error('SQS error:', err);
    res.status(500).json({ error: 'Failed to send to SQS' });
  }
});

app.get('/receive-from-queue', async (req, res) => {
    const params = {
      QueueUrl: process.env.SQS_QUEUE_URL,
      MaxNumberOfMessages: 1,
      WaitTimeSeconds: 5
    };
  
    try {
      const command = new ReceiveMessageCommand(params);
      const response = await sqs.send(command);
  
      if (response.Messages) {
        const message = response.Messages[0];
        console.log('Received message:', message.Body);
  
        // Optionally delete the message after reading
        await sqs.send(new DeleteMessageCommand({
          QueueUrl: process.env.SQS_QUEUE_URL,
          ReceiptHandle: message.ReceiptHandle
        }));
  
        res.json({ message: message.Body });
      } else {
        res.json({ message: 'No messages in queue' });
      }
    } catch (err) {
      console.error('Error receiving from SQS:', err);
      res.status(500).json({ error: 'Failed to receive message' });
    }
  });
