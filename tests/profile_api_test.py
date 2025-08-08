"""Test suite for the ProfileAPI class."""

import os

import pytest

from gravify.profile_api import ProfileAPI


@pytest.fixture
def gravatar_api_key() -> str:
    """Fixture to provide the Gravatar API key from environment variables.

    Returns:
        str: The Gravatar API key.
    """
    if not (key := os.getenv('GRAVATAR_KEY')):
        pytest.skip('GRAVATAR_KEY environment variable not set')
    return key


@pytest.fixture
def gravatar_api(gravatar_api_key: str) -> ProfileAPI:
    """Fixture to create a GravatarAPI instance with the provided API key.

    Returns:
        ProfileAPI: An instance of the GravatarAPI class initialized with the API key.
    """
    return ProfileAPI(api_key=gravatar_api_key)


def test_get_profile(gravatar_api: ProfileAPI) -> None:
    """Test fetching a Gravatar profile."""
    email = 'hello@bsoyka.me'
    profile = gravatar_api.get_profile(email)
    assert (
        profile.hash
        == '20cd9fe5a1a6b65ea0e44e71baf6d342ffe284b3b0cacfa1538c4e5f9224c4d3'
    )
