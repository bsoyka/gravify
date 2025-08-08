"""A library to interface with Gravatar profiles and avatars."""

import importlib.metadata

from gravify.gravatar_api import GravatarAPI

__version__ = importlib.metadata.version('gravify')

__all__ = [
    'GravatarAPI',
    '__version__',
]
