import pytest
from unittest.mock import AsyncMock, patch

from backend.services.games import get_twitch_game_id
from backend.models.game import Game

@pytest.mark.asyncio
async def test_get_twitch_game_id_returns_cached_game_id():
    # Mock MongoDB collection
    mock_db = AsyncMock()
    mock_db.find_one.return_value = {"name": "valorant", "id": "12345"}

    with patch("backend.services.games.games_collection", mock_db):
        game_id = await get_twitch_game_id("Valorant")

    assert game_id == "12345"
    mock_db.find_one.assert_called_once_with({"name": "valorant"})


@pytest.mark.asyncio
async def test_get_twitch_game_id_fetches_from_twitch_when_not_cached():
    # Mock MongoDB collection (no cache)
    mock_db = AsyncMock()
    mock_db.find_one.return_value = None

    # Mock Twitch API response
    mock_twitch_response = [{"id": "67890", "name": "Valorant"}]

    with patch("backend.services.games.games_collection", mock_db), \
         patch("backend.services.twitch_api.TwitchAPI.make_request", return_value=mock_twitch_response):
        
        game_id = await get_twitch_game_id("Valorant")

    assert game_id == "67890"

    # Ensure MongoDB insert is called with correct data
    mock_db.insert_one.assert_called_once_with(Game(name="valorant", id="67890").model_dump())


@pytest.mark.asyncio
async def test_get_twitch_game_returns_httpexception_when_game_not_found():
    # Mock MongoDB collection (no cache)
    mock_db = AsyncMock()
    mock_db.find_one.return_value = None

    with patch("backend.services.games.games_collection", mock_db), \
         patch("backend.services.twitch_api.TwitchAPI.make_request", return_value=[]):
        
        with pytest.raises(Exception) as exc_info:
            await get_twitch_game_id("UnknownGame")

    assert exc_info.value.status_code == 404
    assert "Game not found" in str(exc_info.value)
