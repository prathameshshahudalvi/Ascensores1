import os

creds_json = os.getenv("TEST_1")
creds_json_1 = os.getenv("TEST_2")

if creds_json is None:
    raise SystemExit("Secret not available")

