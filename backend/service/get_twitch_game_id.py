import requests
from fastapi import HTTPException

from backend.config import TWITCH_GET_GAME_INFOS_URL, TWITCH_CLIENT_ID
from backend.service.get_twitch_access_token import get_twitch_access_token

def get_twitch_game_id(game_name: str):
    """
    Gets Twitch information about specified game.
    Used to get a game id by its name.
    """

    access_token = get_twitch_access_token()

    headers = {
        "Client-ID": TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {access_token}"
    }
    params = {"name": game_name}

    response = requests.get(TWITCH_GET_GAME_INFOS_URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if "data" in data and data["data"]:
            return data["data"][0]["id"]
        else:
            raise HTTPException(status_code=404, detail="Game not found")
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)