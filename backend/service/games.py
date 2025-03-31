from fastapi import HTTPException

from backend.config import TWITCH_GET_GAME_INFOS_URL
from backend.service.twitch_api import TwitchAPI

def get_twitch_game_id(game_name: str):
    """
    Fetches the Twitch Game ID based on the game name.
    If multiple results : get the first one.
    """

    data = TwitchAPI.make_request(TWITCH_GET_GAME_INFOS_URL, {"name": game_name})

    if data:
        return data[0]["id"]

    raise HTTPException(status_code=404, detail="Game not found")
