
# Cloud Craft - Full Stack Authentication with AWS Cognito & S3

This is a full-stack web application project built with **Node.js** and **Python**, using **AWS Cognito** for user authentication and **AWS S3** for file storage. The application has a **frontend** built using **Express.js** with **EJS** templates, and a **backend** that utilizes **Python** to interact with AWS services.

## Description

Cloud Craft is a full-stack web application that integrates AWS Cognito for authentication and AWS S3 for file storage. The user is able to sign up, log in, and log out using their Cognito credentials, and the backend can handle file uploads and downloads using S3.

### Key Features:
- **User Authentication**: Using AWS Cognito to handle user login and registration.
- **Frontend**: Built with Node.js and Express, rendered using EJS templates.
- **Backend**: Python (Flask) for interacting with AWS services like **S3** for file uploads and downloads.
- **Session Management**: Using `express-session` to store user session information after successful authentication.
- **Secure Login Flow**: OAuth 2.0 and OpenID Connect integration with AWS Cognito for secure user authentication.
- **AWS S3 File Storage**: Upload and download files to/from AWS S3 using the backend.

## Prerequisites

Before running the application, ensure you have the following installed on your system:

- **Node.js** (>= 16.x.x)
- **npm** or **yarn**
- **Python** (for backend code)
- **Flask** (for backend)
- AWS account with **Cognito** and **S3** setup
- **AWS CLI** configured (optional, for backend development)

## Setup and Installation

### Frontend Setup (Node.js)

1. Clone the repository:
    ```bash
    git clone https://github.com/RalitsaTerzieva/cloud-craft
    cd cloud-craft
    ```

2. Navigate to the `frontend/js` directory:
    ```bash
    cd frontend/js
    ```

3. Install required npm packages:
    ```bash
    npm install
    ```

4. Create a `.env` file in `frontend/js/` directory to store your environment variables:
    ```bash
    COGNITO_USER_POOL_DOMAIN=<your_cognito_domain>
    COGNITO_CLIENT_ID=<your_cognito_client_id>
    COGNITO_CLIENT_SECRET=<your_cognito_client_secret>
    COGNITO_REDIRECT_URI=<your_redirect_uri>
    COGNITO_LOGOUT_URI=<your_logout_uri>
    SESSION_SECRET=<your_session_secret>
    PORT=3000
    ```

5. Run the frontend server:
    ```bash
    node auth-server.js
    ```

6. Open the browser and go to `http://localhost:3000` to test the login flow.

### Backend Setup (Python)

To interact with AWS S3 using Python, you will need to set up a Python environment with the required dependencies:

1. Navigate to the `backend` folder:
    ```bash
    cd backend
    ```

2. Create a Python virtual environment:
    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```

4. Install required dependencies:
    ```bash
    pip install boto3 flask python-dotenv
    ```

5. Create a `.env` file in the `backend/` directory to store your AWS credentials and S3 settings:
    ```bash
    AWS_ACCESS_KEY_ID=<your_aws_access_key>
    AWS_SECRET_ACCESS_KEY=<your_aws_secret_key>
    AWS_REGION=<your_aws_region>
    S3_BUCKET_NAME=<your_s3_bucket_name>
    ```

6. Run the backend server (Flask):
    ```bash
    python app.py
    ```

### Testing S3 File Upload and Download

Once the backend is set up, you can test file upload and download functionality with AWS S3.

1. In the `backend` directory, create a file `sample_upload.txt` for testing file upload:
    ```bash
    echo "Hello from CloudCraft backend! 👋" > sample_upload.txt
    ```

2. Run the script to upload the file:
    ```bash
    python s3_utils.py upload_file sample_upload.txt myfile.txt
    ```

3. To download the file from S3:
    ```bash
    python s3_utils.py download_file myfile.txt downloaded_file.txt
    ```

## How it Works

### Authentication Flow:
1. User visits the `/login` route in the frontend.
2. The Express server (frontend) redirects the user to the AWS Cognito login page.
3. After the user logs in, Cognito redirects back to the configured **redirect URI** with an authorization code.
4. The server exchanges the authorization code for an access token and retrieves user information.
5. The user info is saved in the session, and the user is redirected to the homepage with their details displayed.
6. On logout, the session is destroyed, and the user is logged out of Cognito.

### File Upload and Download Flow (Backend):
1. The backend (Python) is responsible for handling file uploads and downloads using AWS S3.
2. When a file is uploaded, the backend will use the `upload_file` function from `s3_utils.py` to upload files to S3.
3. When a file is downloaded, the backend will use the `download_file` function from `s3_utils.py` to fetch files from S3.

## AWS Cognito Configuration

You will need to configure AWS Cognito as follows:

1. **Create a User Pool**:
   - Go to the Cognito Dashboard in the AWS Console.
   - Create a User Pool with **email-based sign-up** or **username-based sign-up** as per your requirements.

2. **Create a Cognito App Client**:
   - In the User Pool settings, create an App Client.
   - Save the **App Client ID** and **App Client Secret**.
   - Make sure to **enable OAuth2.0** flows (Code Flow) and provide the **redirect URI**.

3. **Set up Allowed Callback URLs**:
   - In the User Pool settings, configure the **Allowed Callback URLs** and **Allowed Logout URLs**.

## AWS S3 Configuration

You will need to configure AWS S3 to use it for file storage:

1. **Create an S3 Bucket**:
   - Go to the S3 Dashboard in the AWS Console.
   - Create a bucket and make sure it’s publicly accessible (if required for your use case).

2. **Set Bucket Policies**:
   - Set up your S3 bucket policies to allow appropriate permissions for uploading and downloading files.

## Troubleshooting

### Common Errors:

1. **Error: "Invalid URL"**: 
   - Make sure that the **redirect URI** is correctly configured both in the `.env` file and the **AWS Cognito Dashboard**.

2. **Session not working**: 
   - Double-check that **session cookies** are enabled and that the session secret is correctly set in the `.env` file.

3. **S3 Upload/Download issues**:
   - Verify that your **AWS_ACCESS_KEY_ID** and **AWS_SECRET_ACCESS_KEY** are correct and have the necessary permissions to access S3.

### Debugging Tips:
- Check the console for any errors in the Node.js server.
- Make sure all environment variables are set correctly in the `.env` file.
- Verify AWS IAM policies if you encounter permission issues with S3.

---

This README should help guide you through setting up both the frontend and backend of your project while using AWS Cognito for authentication and AWS S3 for file storage. Let me know if you need more assistance!
