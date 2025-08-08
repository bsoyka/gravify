"""A library to interface with Gravatar profiles and avatars."""

import importlib.metadata

from gravify.profile_api import ProfileAPI

__version__ = importlib.metadata.version('gravify')

__all__ = [
    'ProfileAPI',
    '__version__',
]
