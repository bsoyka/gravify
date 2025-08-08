"""Utility functions for the Gravify package."""

from hashlib import sha256


def hash_email(email: str) -> str:
    """Normalize and hash an email address for use with the Gravatar API.

    The Gravatar API requires trimming whitespace, converting to lowercase, and hashing
    the email address using SHA256. The resulting hash is returned in lowercase
    hexadecimal format.

    Args:
        email: The email address to hash.

    Returns:
        The hash of the email address in lowercase hexadecimal format.
    """
    email_encoded = email.strip().lower().encode('utf-8')
    return sha256(email_encoded).hexdigest()
