from flask import Flask, request, jsonify
from s3_utils import upload_file, download_file
from send_message import send_message_to_queue

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    s3_key = file.filename
    file_path = f"/tmp/{s3_key}"
    file.save(file_path)

    upload_file(file_path, s3_key)
    return jsonify({"message": "Upload successful", "file": s3_key})

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    local_path = f"./downloads/{filename}"
    download_file(filename, local_path)
    return jsonify({"message": "Download complete", "saved_to": local_path})

@app.route('/send-to-queue', methods=['POST'])
def send_to_queue():
    data = request.json
    file_name = data['file_name']
    user_email = data['user_email']
    
    send_message_to_queue(file_name, user_email)
    
    return jsonify({"message": "Sent to SQS!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
