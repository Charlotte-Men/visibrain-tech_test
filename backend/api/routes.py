from fastapi import APIRouter

from backend.service.get_twitch_videos_by_game import get_twitch_videos_by_game
 
router = APIRouter()

@router.get("/")
async def root():
    videos = get_twitch_videos_by_game("civilization")

    return {f"Videos: {videos}"}
