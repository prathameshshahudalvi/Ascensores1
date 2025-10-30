import json
import os
import streamlit as st

# Parse credentials from environment variable, default to empty dict if not found
creds = json.loads(os.getenv("MY_APP_CRED", "{}"))
st.warning("Credentials loaded successfully:", list(creds.keys()))