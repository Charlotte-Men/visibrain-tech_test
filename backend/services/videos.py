from backend.config import TWITCH_GET_VIDEOS_INFOS_URL
from backend.services.games import get_twitch_game_id
from backend.services.twitch_api import TwitchAPI

async def get_twitch_videos_by_game(game_name: str):
    """
    Fetches videos from Twitch based on the game name.
    """

    game_id = await get_twitch_game_id(game_name)

    return TwitchAPI.make_request(TWITCH_GET_VIDEOS_INFOS_URL, {"game_id": game_id})
