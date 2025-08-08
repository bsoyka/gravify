"""Gravatar API data models."""

from dataclasses import dataclass


@dataclass
class Profile:
    """Data model for a Gravatar profile."""

    hash: str
    display_name: str
