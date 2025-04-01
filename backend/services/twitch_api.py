import requests
from fastapi import HTTPException

from backend.config import TWITCH_CLIENT_ID
from backend.services.twitch_auth import TwitchAuth

class TwitchAPI:
    @staticmethod
    def make_request(url, params=None):
        """
        Handles Twitch API requests with proper authentication.
        """

        access_token = TwitchAuth.get_access_token()
        headers = {
            "Client-ID": TWITCH_CLIENT_ID,
            "Authorization": f"Bearer {access_token}"
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json().get("data", [])
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
