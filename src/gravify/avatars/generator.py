"""Avatar URL generator for Gravify."""

from enum import StrEnum


class DefaultImage(StrEnum):
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


class Rating(StrEnum):
    """Rating options for Gravatar."""

    G = 'g'
    PG = 'pg'
    R = 'r'
    X = 'x'


class AvatarGenerator:
    """Gravatar avatar URL generator."""

    def __init__(  # noqa: PLR0913
        self,
        size: int | None = None,
        *,
        default_image: str | DefaultImage | None = None,
        force_default: bool | None = False,
        rating: Rating | None = None,
        initials: str | None = None,
        name: str | None = None,
    ) -> None:
        """Initialize the avatar generator with reusable options.

        Args:
            size: Side length of the square avatar in pixels (default is 80).
            default_image: Default image type if no avatar is found (default is the
                Gravatar logo).
            force_default: Force the default image to always return (default is False).
            rating: Rating of the avatar (default is G).
            initials: Initials to use for the avatar if no image is found.
            name: Name to use for the avatar initials if no image is found.
        """
        self.size = size
        self.default_image = default_image
        self.force_default = force_default
        self.rating = rating
        self.initials = initials
        self.name = name
