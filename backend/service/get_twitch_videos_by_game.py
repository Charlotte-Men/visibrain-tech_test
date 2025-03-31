import requests
from fastapi import HTTPException

from backend.config import TWITCH_GET_VIDEOS_INFOS_URL, TWITCH_CLIENT_ID
from backend.service.get_twitch_access_token import get_twitch_access_token
from backend.service.get_twitch_game_id import get_twitch_game_id


def get_twitch_videos_by_game(game_name: str):
    """
    Gets Twitch videos related to a specified game.
    """

    access_token = get_twitch_access_token()
    game_id = get_twitch_game_id(game_name)

    headers = {
        "Client-ID": TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {access_token}"
    }
    params = {"game_id": game_id}

    response = requests.get(TWITCH_GET_VIDEOS_INFOS_URL, headers=headers, params=params)

    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)
