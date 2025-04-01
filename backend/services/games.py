from fastapi import HTTPException

from backend.config import TWITCH_GET_GAME_INFOS_URL
from backend.services.twitch_api import TwitchAPI

from backend.db.database import games_collection

async def get_twitch_game_id(game_name: str):
    """
    Fetches the Twitch Game ID based on the game name.
    If multiple results : get the first one.
    """

    # Check if the game is already cached
    cached_game = await games_collection.find_one({"name": game_name.lower()})

    if cached_game:
        return cached_game["id"]
    
    # If not cached, fetch from Twitch API
    data = TwitchAPI.make_request(TWITCH_GET_GAME_INFOS_URL, {"name": game_name})

    if data:
        game_id = data[0]["id"]

        # Save game_id in MongoDB for future use
        await games_collection.insert_one({"name": game_name.lower(), "id": game_id})
        
        return game_id

    raise HTTPException(status_code=404, detail="Game not found")
