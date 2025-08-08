"""Adapter class for interacting with the Gravatar API."""

from __future__ import annotations

import logging

import httpx


class RestAdapter:
    """Adapter for the Gravatar API."""

    def __init__(
        self,
        *,
        api_key: str | None = None,
        api_base_url: str = 'https://api.gravatar.com/v3',
        avatar_base_url: str = 'https://gravatar.com/avatar',
    ) -> None:
        """Initialize the Gravatar API adapter.

        Args:
            api_key: The API key to use for authentication.
            api_base_url: The base URL for the Gravatar API.
            avatar_base_url: The base URL for Gravatar avatars.
        """
        self.api_base_url = api_base_url
        self.avatar_base_url = avatar_base_url
        self.api_client = httpx.Client(
            base_url=api_base_url, headers={'Authorization': f'Bearer {api_key}'}
        )

        self._logger = logging.getLogger(__name__)

    def get(self, endpoint: str, params: dict | None = None) -> httpx.Response:
        """Make a GET request to the Gravatar API.

        Args:
            endpoint: The API endpoint to call, starting with a slash.
            params: Optional query parameters for the request.

        Returns:
            The response from the API.
        """
        self._logger.debug('Making GET request to %s with params %s', endpoint, params)
        return self.api_client.get(endpoint, params=params)
