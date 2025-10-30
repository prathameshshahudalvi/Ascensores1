import json
import os
import main

# Parse credentials from environment variable, default to empty dict if not found
creds = json.loads(os.getenv("MY_APP_CRED", "{}"))
main.setCredentials(creds)
