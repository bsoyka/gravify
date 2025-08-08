"""Avatar URL generator for Gravify."""

from typing import cast
from urllib.parse import urlencode

from gravify.avatars.exceptions import (
    InitialsAndNameError,
    InitialsDefaultImageNotSetError,
)
from gravify.avatars.options import DefaultImage, Rating
from gravify.utils import hash_email

_DEFAULT_AVATAR_SIZE = 80
_DEFAULT_RATING = Rating.G


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

        Raises:
            InitialsAndNameError: If both initials and name are provided.
        """
        self.size = size
        self.default_image = default_image
        self.force_default = force_default
        self.rating = rating

        if initials is not None and name is not None:
            raise InitialsAndNameError
        self.initials = initials
        self.name = name

    @property
    def initials(self) -> str | None:
        """Get the initials used for the "initials" default avatar."""
        return self._initials

    @initials.setter
    def initials(self, value: str | None) -> None:
        """Set the initials used for the "initials" default avatar.

        Raises:
            InitialsDefaultImageNotSetError: If initials are set but the default image
                is not set to INITIALS.
        """
        if value is not None and self.default_image != DefaultImage.INITIALS:
            raise InitialsDefaultImageNotSetError
        self._initials: str | None = value
        self._name: str | None = None

    @property
    def name(self) -> str | None:
        """Get the name used for the "initials" default avatar."""
        return self._name

    @name.setter
    def name(self, value: str | None) -> None:
        """Set the name used for the "initials" default avatar.

        Raises:
            InitialsDefaultImageNotSetError: If a name is set but the default image is
                not set to INITIALS.
        """
        if value is not None and self.default_image != DefaultImage.INITIALS:
            raise InitialsDefaultImageNotSetError
        self._name = value
        self._initials = None

    def _generate_parameters(self) -> dict[str, str | int]:
        """Generate the parameters for the avatar URL.

        This method will not include parameters that are set to their default values, as
        defined by the Gravatar API specifications.

        Returns:
            A dictionary of parameters to be included in the avatar URL query string.
        """
        params: dict[str, str | int] = {}
        if self.size is not None and self.size != _DEFAULT_AVATAR_SIZE:
            params['s'] = self.size
        if self.default_image is not None:
            params['d'] = (
                self.default_image.value
                if isinstance(self.default_image, DefaultImage)
                else self.default_image
            )
        if self.force_default:
            params['f'] = 'y'
        if self.rating is not None and self.rating != _DEFAULT_RATING:
            params['r'] = cast('str', self.rating.value)  # type: ignore[redundant-cast]

        if self.initials is not None:
            params['initials'] = self.initials
        if self.name is not None:
            params['name'] = self.name

        return params

    def generate_url(self, email: str) -> str:
        """Generate the avatar URL for the given email.

        Args:
            email: The email address to generate the avatar for.

        Returns:
            The generated avatar URL.
        """
        email_hash = hash_email(email)
        url = f'https://gravatar.com/avatar/{email_hash}'
        if query_string := urlencode(self._generate_parameters()):
            url += f'?{query_string}'
        return url
