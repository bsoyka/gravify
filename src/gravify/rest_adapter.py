"""Adapter class for interacting with the Gravatar API."""

from __future__ import annotations

import logging
from collections.abc import Mapping, Sequence

import httpx

PARAMS_TYPE = (
    httpx.QueryParams
    | Mapping[
        str,
        str | int | float | bool | Sequence[str | int | float | bool | None] | None,
    ]
    | list[tuple[str, str | int | float | bool | None]]
    | tuple[tuple[str, str | int | float | bool | None], ...]
    | str
    | bytes
    | None
)


class RestAdapter:
    """Adapter for the Gravatar API."""

    def __init__(self, *, api_base_url: str, api_key: str | None = None) -> None:
        """Initialize the Gravatar API adapter.

        Args:
            api_base_url: The base URL for the Gravatar API.
            api_key: The API key to use for authentication.
        """
        self.api_base_url = api_base_url
        self.api_client = httpx.Client(
            base_url=api_base_url,
            headers={'Authorization': f'Bearer {api_key}'} if api_key else {},
        )

        self._logger = logging.getLogger(__name__)

    def get(self, endpoint: str, params: PARAMS_TYPE = None) -> httpx.Response:
        """Make a GET request to the Gravatar API.

        Args:
            endpoint: The API endpoint to call, starting with a slash.
            params: Optional query parameters for the request.

        Returns:
            The response from the API.
        """
        self._logger.debug('Making GET request to %s with params %s', endpoint, params)
        return self.api_client.get(endpoint, params=params)
