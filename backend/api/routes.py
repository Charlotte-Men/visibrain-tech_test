from fastapi import APIRouter

from backend.service.videos import get_twitch_videos_by_game
 
router = APIRouter()

@router.get("/videos/")
async def get_videos(game_name: str):
    videos = await get_twitch_videos_by_game(game_name)
    
    return {"Videos": videos}