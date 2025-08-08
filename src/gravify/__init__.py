"""A library to interface with Gravatar profiles and avatars."""

import importlib.metadata

from gravify.profiles import ProfileAPI

__version__ = importlib.metadata.version('gravify')

__all__ = [
    'ProfileAPI',
    '__version__',
]
