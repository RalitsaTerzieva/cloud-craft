import express from 'express';
import { SQSClient, SendMessageCommand } from '@aws-sdk/client-sqs';

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
