"""Exception classes for the gravify.avatars module."""

from gravify.exceptions import GravifyError


class GravifyAvatarError(GravifyError):
    """Base exception class for Gravify avatar errors."""


class InitialsAndNameError(GravifyAvatarError):
    """Exception raised when both initials and name are specified."""

    def __init__(self) -> None:
        """Initialize the error."""
        super().__init__('Initials and name cannot be specified at the same time.')


class InitialsDefaultImageNotSetError(GravifyAvatarError):
    """Exception raised when the default image is not properly set to INITIALS."""

    def __init__(self) -> None:
        """Initialize the error."""
        super().__init__('Default image must be set to initials.')
