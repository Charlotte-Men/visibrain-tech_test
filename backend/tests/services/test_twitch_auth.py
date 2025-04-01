import pytest
from unittest.mock import patch

from backend.services.twitch_auth import TwitchAuth

@pytest.fixture(autouse=True)
def reset_twitch_auth_cache():
    TwitchAuth._cached_token = {"access_token": None, "expires_at": 0}

@patch("requests.post")
def test_get_access_token_caches_token(mock_requests_post):
    mock_response_data = {"access_token": "fake_auth_access_token", "expires_in": 3600}
    mock_requests_post.return_value.status_code = 200
    mock_requests_post.return_value.json.return_value = mock_response_data

    token1 = TwitchAuth.get_access_token()
    assert token1 == "fake_auth_access_token"

    # Ensure cache is used on second call
    token2 = TwitchAuth.get_access_token()
    assert token2 == "fake_auth_access_token"

    # Ensure twitch api is called only once - no extra call
    mock_requests_post.assert_called_once()
