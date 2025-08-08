"""Avatar options for Gravatar."""

from enum import Enum


class DefaultImage(Enum):
    """Default image options for Gravatar."""

    INITIALS = 'initials'
    COLOR = 'color'
    NOT_FOUND = '404'
    MYSTERY_PERSON = 'mp'
    IDENTICON = 'identicon'
    MONSTER_ID = 'monsterid'
    WAVATAR = 'wavatar'
    RETRO = 'retro'
    ROBOHASH = 'robohash'
    BLANK = 'blank'


class Rating(Enum):
    """Rating options for Gravatar."""

    G = 'g'
    PG = 'pg'
    R = 'r'
    X = 'x'
