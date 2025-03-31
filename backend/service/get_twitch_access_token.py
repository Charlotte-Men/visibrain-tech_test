import requests
import os
import time
from backend.config import TWITCH_GET_TOKEN_URL

TWITCH_CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
TWITCH_CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")

# Cached token storage
cached_token = {"access_token": None, "expires_at": 0}

def get_twitch_access_token():
    """
    Gets a Twitch token:
    - from cached token if still valid
    - if expired: requests a new one from Twitch API using Client Credentials Flow.
    """

    current_time = time.time()

    if cached_token["access_token"] and current_time < cached_token["expires_at"]:
        return cached_token["access_token"]
    
    payload = {
        "client_id": TWITCH_CLIENT_ID,
        "client_secret": TWITCH_CLIENT_SECRET,
        "grant_type": "client_credentials"
    }

    response = requests.post(TWITCH_GET_TOKEN_URL, data=payload)
    token_data = response.json()

    if "access_token" in token_data and "expires_in" in token_data:
        cached_token["access_token"] = token_data["access_token"]
        cached_token["expires_at"] = current_time + token_data["expires_in"]

        return cached_token["access_token"]

    else:
        raise Exception(f"Failed to get Twitch token: {token_data}")