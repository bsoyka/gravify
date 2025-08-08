"""Test suite for the hash_email function."""

import pytest

from gravify.utils import hash_email


@pytest.mark.parametrize(
    'raw_email',
    {
        'hello@bsoyka.me',
        'HELLO@BSOYKA.ME',
        '  hello@bsoyka.me  ',
        'hello@bsoyka.me  ',
        '  hello@bsoyka.me',
        '  HELLO@BSOYKA.ME  ',
    },
)
def test_hash_email(raw_email: str) -> None:
    """Test the hash_email function.

    The result should be the same regardless of leading/trailing whitespace and
    capitalization.
    """
    assert (
        hash_email(raw_email)
        == '429f7d22515020de16db82ec31a7c9d4adae288e89d1d9bc717bba2a55f260b4'
    )
