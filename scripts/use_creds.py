import json
import os

# Parse credentials from environment variable, default to empty dict if not found
creds = json.loads(os.getenv("MY_APP_CRED", "{}"))
print("Credentials loaded successfully:", list(creds.keys()))