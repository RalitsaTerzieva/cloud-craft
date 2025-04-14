from s3_utils import upload_file, download_file

# Test upload
upload_file('sample_upload.txt', 'uploads/sample_upload.txt')

# Test download (you can choose a different location locally)
download_file('uploads/sample_upload.txt', 'downloaded/sample_download.txt')
