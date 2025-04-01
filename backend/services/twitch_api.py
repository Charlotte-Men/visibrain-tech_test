import requests
import logging
from fastapi import HTTPException

from backend.config import TWITCH_CLIENT_ID
from backend.services.twitch_auth import TwitchAuth

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

        logger.info(f"Making request to {url} with params {params}")
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            logger.info("Request successful")
            return response.json().get("data", [])
        
        logger.error(f"Request failed: {response.status_code} - {response.text}")
        raise HTTPException(status_code=response.status_code, detail=response.text)
