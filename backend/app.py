from flask import Flask, request, jsonify
from s3_utils import upload_file, download_file

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

if __name__ == '__main__':
    app.run(debug=True)
