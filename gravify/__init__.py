"""Simple package to generate Gravatar URLs"""

from hashlib import md5

from six import PY3
from validate_email import validate_email

if PY3:
    from urllib.parse import urlencode
    from urllib.request import urlopen
else:
    from urllib import urlencode, urlopen  # pylint: disable=no-name-in-module

__version__ = '1.0.0'


class Gravatar:
    """A class to represent a Gravatar user

    Args:
        email (str): The user's email address
        verify_email (bool): Whether to verify that the email address is
            valid
        default_image (str): The default image code to use if the user
            isn't found (one of: 404, mp, identicon, monsterid, wavatar,
            retro, robohash, blank)
        size (int): A single dimension determining the size of the image
            (between 1 and 2048)
        force_default (bool): Whether to always force the default image
        max_rating (str): The maximum rating to be shown (one of: g, pg,
            r, x)

    Raises:
        ValueError: The email address is invalid
    """

    def __init__(
        self,
        email,
        verify_email=True,
        default_image=None,
        size=None,
        force_default=False,
        max_rating=None,
    ):
        if verify_email and not validate_email(email):
            raise ValueError('Invalid email address')

        self.email = email.strip().lower()
        self.default_image = default_image
        self.size = size
        self.force_default = force_default
        self.max_rating = max_rating

    @property
    def url(self):
        """The generated secure (https) Gravatar URL

        Returns:
            str
        """

        params = {
            's': self.size,
            'd': self.default_image,
            'f': 'y' if self.force_default else None,
            'r': self.max_rating
            if self.max_rating in ['g', 'pg', 'r', 'x']
            else None,
        }

        url_params = urlencode(
            sorted({k: v for k, v in params.items() if v is not None}.items())
        )

        _url = 'https://www.gravatar.com/avatar/' + self.hash

        return _url + '?' + url_params if url_params else _url

    @property
    def unsecure_url(self):
        """The generated unsecure (http) Gravatar URL

        Returns:
            str
        """

        return self.url.replace('https://', 'http://', 1)

    @property
    def hash(self):
        """The MD5-hashed email address

        Returns:
            str
        """

        return md5(self.email.encode('utf-8')).hexdigest()

    @property
    def file(self):
        """The contents of the generated Gravatar URL

        Returns:
            str
        """

        return urlopen(self.url)
