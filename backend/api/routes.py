from fastapi import APIRouter

from backend.service.get_twitch_game_id import get_twitch_game_id
 
router = APIRouter()

@router.get("/")
async def root():
    game_id = get_twitch_game_id("civilization")

    return {f"game id: {game_id}"}
