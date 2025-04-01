import pytest
import time
from unittest.mock import patch

from backend.services.twitch_api import TwitchAPI
from backend.services.twitch_auth import TwitchAuth
from backend.config import TWITCH_CLIENT_ID

@pytest.fixture
def mock_requests_get():
    with patch("requests.get") as mock_get:
        yield mock_get


def test_make_request_sends_correct_headers(mock_requests_get):
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = {"data": []}

    TwitchAuth._cached_token = {"access_token": "fake_api_access_token", "expires_at": time.time() + 3000}

    url = "https://api.twitch.tv/helix/games"
    params = {"name": "Fortnite"}

    TwitchAPI.make_request(url, params)

    mock_requests_get.assert_called_once_with(
        url,
        headers={
            "Client-ID": TWITCH_CLIENT_ID,
            "Authorization": "Bearer fake_api_access_token"
        },
        params=params
    )


def test_make_request_returns_correct_data(mock_requests_get):
    mock_response_data = {"data": [{"id": "123", "name": "Fortnite"}]}
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = mock_response_data

    url = "https://api.twitch.tv/helix/games"
    params = {"name": "Fortnite"}

    result = TwitchAPI.make_request(url, params)

    assert result == mock_response_data["data"]