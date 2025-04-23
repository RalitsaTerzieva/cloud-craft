import { S3Client, PutObjectCommand } from "@aws-sdk/client-s3";

const REGION = "us-east-1";
const s3 = new S3Client({
  region: REGION,
  credentials: {
    accessKeyId: process.env.AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
  },
});

window.uploadFile = async () => {
  const file = document.getElementById("fileInput").files[0];
  if (!file) return alert("No file selected!");

  const params = {
    Bucket: process.env.S3_BUCKET_NAME,
    Key: file.name,
    Body: file,
  };

  try {
    const command = new PutObjectCommand(params);
    await s3.send(command);
    alert("File uploaded!");
  } catch (err) {
    console.error("Upload failed:", err);
  }
};
