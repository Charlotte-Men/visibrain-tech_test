import os

from dotenv import load_dotenv

load_dotenv()

TWITCH_CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
TWITCH_CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")

TWITCH_GET_GAME_INFOS_URL="https://api.twitch.tv/helix/games"
TWITCH_GET_TOKEN_URL="https://id.twitch.tv/oauth2/token"
TWITCH_GET_VIDEOS_INFOS_URL="https://api.twitch.tv/helix/videos"
