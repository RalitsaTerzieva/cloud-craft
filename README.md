# Cloud Craft - Full Stack Authentication with AWS Cognito

This is a full-stack web application project built with **Node.js** and **Python**, using **AWS Cognito** for user authentication. The application has a **frontend** built using **Express.js** with **EJS** templates, and a **backend** that utilizes **Python** to interact with AWS services.


## Description

Cloud Craft is a full-stack web application that integrates AWS Cognito for authentication. The user is able to sign up, log in, and log out using their Cognito credentials.

### Key Features:
- **User Authentication**: Using AWS Cognito to handle user login and registration.
- **Frontend**: Built with Node.js and Express, and rendered using EJS templates.
- **Backend**: Python (to be added later) for interacting with other AWS services like S3, DynamoDB, etc.
- **Session Management**: Using `express-session` to store user session information after successful authentication.
- **Secure Login Flow**: OAuth 2.0 and OpenID Connect integration with AWS Cognito for secure user authentication.

## Prerequisites

Before running the application, ensure you have the following installed on your system:

- **Node.js** (>= 16.x.x)
- **npm** or **yarn**
- **Python** (for backend code)
- AWS account with **Cognito** setup
- **AWS CLI** configured (optional, for backend development)

## Setup and Installation

### Frontend Setup (Node.js)

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/cloud-craft.git
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

To be added later.

## How it Works

### Authentication Flow:
1. User visits the `/login` route in the frontend.
2. The Express server (frontend) redirects the user to the AWS Cognito login page.
3. After the user logs in, Cognito redirects back to the configured **redirect URI** with an authorization code.
4. The server exchanges the authorization code for an access token and retrieves user information.
5. The user info is saved in the session, and the user is redirected to the homepage with their details displayed.
6. On logout, the session is destroyed, and the user is logged out of Cognito.

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

## Troubleshooting

### Common Errors:

1. **Error: "Invalid URL"**: 
   - Make sure that the **redirect URI** is correctly configured both in the `.env` file and the **AWS Cognito Dashboard**.
   
2. **Session not working**: 
   - Double-check that **session cookies** are enabled and that the session secret is correctly set in the `.env` file.

### Debugging Tips:
- Check the console for any errors in the Node.js server.
- Make sure all environment variables are set correctly.
