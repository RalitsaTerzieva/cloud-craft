const express = require('express');
const session = require('express-session');
const { Issuer, generators } = require('openid-client');
require('dotenv').config();
const path = require('path');
const app = express();

app.set('views', path.join(__dirname, "..", 'views')); 
app.set('view engine', 'ejs');

let client;
// Initialize OpenID Client
async function initializeClient() {
    const issuer = await Issuer.discover(`https://${process.env.COGNITO_USER_POOL_DOMAIN}`);
    client = new issuer.Client({
        client_id: process.env.COGNITO_CLIENT_ID,            
        client_secret: process.env.COGNITO_CLIENT_SECRET,    
        redirect_uris: [process.env.COGNITO_REDIRECT_URI],   
        response_types: ['code']
    });
};
initializeClient().catch(console.error);

app.use(session({
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: false
}));

// routes
const checkAuth = (req, res, next) => {
    if (!req.session.userInfo) {
        req.isAuthenticated = false;
    } else {
        req.isAuthenticated = true;
    }
    next();
};

app.get('/', checkAuth, (req, res) => {
    res.render('home', {
        isAuthenticated: req.isAuthenticated,
        userInfo: req.session.userInfo
    });
});

app.get('/login', (req, res) => {
    const nonce = generators.nonce();
    const state = generators.state();

    req.session.nonce = nonce;
    req.session.state = state;

    const authUrl = client.authorizationUrl({
        scope: 'phone openid email',
        state: state,
        nonce: nonce,
    });

    res.redirect(authUrl);
});

// Helper function to get the path from the URL. Example: "http://localhost/hello" returns "/hello"
function getPathFromURL(urlString) {
    try {
        const url = new URL(urlString);
        return url.pathname;
    } catch (error) {
        console.error('Invalid URL:', error);
        return null;
    }
}


app.get(getPathFromURL(process.env.COGNITO_REDIRECT_URI), async (req, res) => {
    try {
        const params = client.callbackParams(req);
        const tokenSet = await client.callback(
            process.env.COGNITO_REDIRECT_URI,
            params,
            {
                nonce: req.session.nonce,
                state: req.session.state
            }
        );

        const userInfo = await client.userinfo(tokenSet.access_token);
        req.session.userInfo = userInfo;

        res.redirect('/');
    } catch (err) {
        console.error('Callback error:', err);
        res.redirect('/');
    }
});

// Logout route
app.get('/logout', (req, res) => {
    req.session.destroy();
    const logoutUrl = `https://${process.env.COGNITO_USER_POOL_DOMAIN}/logout?client_id=${process.env.COGNITO_CLIENT_ID}&logout_uri=${process.env.COGNITO_LOGOUT_URI}`;
    res.redirect(logoutUrl);
});

app.listen(process.env.PORT, () => {
    console.log(`Server is running on http://localhost:${process.env.PORT}`);
});
