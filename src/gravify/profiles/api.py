"""Gravatar API client for fetching user profiles."""

from __future__ import annotations

from gravify.profiles.models import Profile
from gravify.rest_adapter import RestAdapter
from gravify.utils import hash_email


class ProfileAPI:
    """Client for interacting with the Gravatar API."""

    def __init__(
        self,
        *,
        api_key: str | None = None,
        api_base_url: str = 'https://api.gravatar.com/v3',
    ) -> None:
        """Initialize the Gravatar API client.

        Args:
            api_key: The API key to use for authentication.
            api_base_url: The base URL for the Gravatar API.
        """
        self._rest_adapter = RestAdapter(
            api_key=api_key,
            api_base_url=api_base_url,
        )

    def get_profile(self, email: str) -> Profile:
        """Fetch the Gravatar profile for a given email address.

        Args:
            email: The email address to fetch the profile for.

        Returns:
            A Profile object containing the Gravatar profile data.
        """
        hashed_email = hash_email(email)
        response = self._rest_adapter.get(f'/profiles/{hashed_email}')
        response.raise_for_status()
        data = response.json()
        return Profile(**data)
