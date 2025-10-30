const creds = JSON.parse(process.env.MY_APP_CRED || '{}');
console.log("Credentials loaded successfully:", Object.keys(creds));