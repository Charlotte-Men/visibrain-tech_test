from fastapi import APIRouter

from backend.service.get_twitch_access_token import get_twitch_access_token
 
router = APIRouter()

@router.get("/")
async def root():
    access_token = get_twitch_access_token()

    return {f"token: {access_token}"}
