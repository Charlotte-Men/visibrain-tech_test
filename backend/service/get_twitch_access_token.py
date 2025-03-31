import requests
import os
from backend.config import TWITCH_GET_TOKEN_URL

TWITCH_CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
TWITCH_CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")

def get_twitch_access_token():
    """
    Requests an access token from Twitch API using Client Credentials Flow.
    """

    payload = {
        "client_id": TWITCH_CLIENT_ID,
        "client_secret": TWITCH_CLIENT_SECRET,
        "grant_type": "client_credentials"
    }

    response = requests.post(TWITCH_GET_TOKEN_URL, data=payload)
    token_data = response.json()

    if "access_token" in token_data:
        return token_data["access_token"]
    else:
        raise Exception(f"Failed to get Twitch token: {token_data}")
