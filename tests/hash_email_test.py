"""Test suite for the hash_email function."""

import pytest
from hypothesis import given
from hypothesis import strategies as st

from gravify.utils import hash_email


@pytest.mark.parametrize(
    ('email', 'expected_hash'),
    {
        (
            'hello@example.com',
            '1753bdb368271a785887ddbfb926164f2f7c6a88f609c07ff0401c5572955206',
        ),
        (
            'hello@bsoyka.me',
            '429f7d22515020de16db82ec31a7c9d4adae288e89d1d9bc717bba2a55f260b4',
        ),
        (
            'test@somewhere.xyz',
            'ff6a6650b1f8e52d198b89c0d4afe8114d388b854ab81760c6560c85ab0688ad',
        ),
    },
)
def test_known_email_hashes(email: str, expected_hash: str) -> None:
    """Test the hash_email function with some known expected hashes."""
    assert hash_email(email) == expected_hash


@given(st.emails())
def test_email_hash_with_whitespace(email: str) -> None:
    """Test that the hash_email function ignores leading and trailing whitespace."""
    email_with_trailing_whitespace = f'{email}   '
    email_with_leading_whitespace = f'   {email}'
    email_with_both_whitespace = f'   {email}   '

    assert (
        hash_email(email)
        == hash_email(email_with_trailing_whitespace)
        == hash_email(email_with_leading_whitespace)
        == hash_email(email_with_both_whitespace)
    )


@given(st.emails())
def test_email_hash_with_case_insensitivity(email: str) -> None:
    """Test that the hash_email function is case-insensitive."""
    email_upper = email.upper()
    email_lower = email.lower()
    email_mixed_case = email.title()

    assert (
        hash_email(email)
        == hash_email(email_upper)
        == hash_email(email_lower)
        == hash_email(email_mixed_case)
    )
