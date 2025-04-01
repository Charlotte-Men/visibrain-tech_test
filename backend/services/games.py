import logging
from fastapi import HTTPException

from backend.models.game import Game
from backend.config import TWITCH_GET_GAME_INFOS_URL
from backend.services.twitch_api import TwitchAPI

from backend.db.database import games_collection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def get_twitch_game_id(game_name: str):
    """
    Fetches the Twitch Game ID based on the game name.
    If multiple results : get the first one.
    """

    # Check if the game is already cached
    logger.info(f"Checking database for cached game ID: {game_name}")
    cached_game = await games_collection.find_one({"name": game_name.lower()})

    if cached_game:
        logger.info(f"Game ID found in cache: {cached_game['id']}")
        return Game(**cached_game).id
    
    # If not cached, fetch from Twitch API
    logger.info(f"Fetching game ID from Twitch API for: {game_name}")
    data = TwitchAPI.make_request(TWITCH_GET_GAME_INFOS_URL, {"name": game_name})

    if data:
        game_id = data[0]["id"]
        logger.info(f"Game ID fetched: {game_id}, saving to database")

        game = Game(name=game_name.lower(), id=game_id)

        # Save game_id in MongoDB for future use
        await games_collection.insert_one(game.model_dump())
        
        return game.id

    logger.warning(f"Game not found: {game_name}")
    raise HTTPException(status_code=404, detail="Game not found")
