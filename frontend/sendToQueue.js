export async function sendToQueue(fileName, userEmail) {
    try {
      const response = await fetch('/send-to-queue', {   // assumes your backend exposes /send-to-queue
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ file_name: fileName, user_email: userEmail }),
      });
  
      const data = await response.json();
      console.log(data.message);
    } catch (error) {
      console.error('Failed to send message to queue:', error);
    }
  }
  