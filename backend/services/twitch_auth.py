import requests
import time
import logging

from backend.config import TWITCH_GET_TOKEN_URL, TWITCH_CLIENT_ID, TWITCH_CLIENT_SECRET

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TwitchAuth:
    _cached_token = {"access_token": None, "expires_at": 0}

    @classmethod
    def get_access_token(cls):
        """
        Retrieves a Twitch access token using the Client Credentials Flow.
        Uses a cached token if still valid.
        """

        current_time = time.time()

        if cls._cached_token["access_token"] and current_time < cls._cached_token["expires_at"]:
            logger.info("Using cached Twitch access token")

            return cls._cached_token["access_token"]

        logger.info("Fetching new Twitch access token")

        payload = {
            "client_id": TWITCH_CLIENT_ID,
            "client_secret": TWITCH_CLIENT_SECRET,
            "grant_type": "client_credentials"
        }

        response = requests.post(TWITCH_GET_TOKEN_URL, data=payload)
        token_data = response.json()

        if "access_token" in token_data and "expires_in" in token_data:
            cls._cached_token["access_token"] = token_data["access_token"]
            cls._cached_token["expires_at"] = current_time + token_data["expires_in"]
            logger.info("New Twitch token acquired successfully")

            return cls._cached_token["access_token"]

        logger.error(f"Failed to get Twitch token: {token_data}")
        raise Exception(f"Failed to get Twitch token: {token_data}")
