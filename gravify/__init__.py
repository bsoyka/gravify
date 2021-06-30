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
        self.verify_email = verify_email
        self.email = email
        self.default_image = default_image
        self.size = size
        self.force_default = force_default
        self.max_rating = max_rating

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        """Validate and set string data type and value for email"""
        if isinstance(value, str):
            if self.verify_email and not validate_email(value):
                raise ValueError('Invalid email address')
            self._email = value.strip().lower()
        else:
            raise TypeError('email must be string')

    @property
    def verify_email(self):
        return self._verify_email

    @verify_email.setter
    def verify_email(self, value):
        """Validate and set boolean data type for verify_email"""
        if isinstance(value, bool):
            self._verify_email = value
        else:
            raise TypeError('verify_email must be boolean')

    @property
    def default_image(self):
        return self._default_image
    
    @default_image.setter
    def default_image(self, value):
        """Validate and set string data type and for default_image"""
        if value is None:
            self._default_image = value
            return
        if isinstance(value, str):
            possible_values = ['404', 'mp', 'identicon', 'monsterid', 
            'wavatar', 'retro', 'robohash', 'blank']
            if value not in possible_values:
                raise ValueError(f'default_image must be one of: {possible_values}')
            self._default_image = value
        else:
            raise TypeError('default_image must be string')

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        """Validate and set int data type and value for size"""
        if value is None:
            self._size = value
            return
        if isinstance(value, int):
            if not (1 <= value <= 2048):
                raise ValueError('size must be an integer between 1 and 2048')
            self._size = value
        else:
            raise TypeError('size must be integer')

    @property
    def force_default(self):
        return self._force_default

    @force_default.setter
    def force_default(self, value):
        """Validate and set boolean data type for force_default"""
        if isinstance(value, bool):
            self._force_default = value
        else:
            raise TypeError('force_default must be boolean')

    @property
    def max_rating(self):
        return self._max_rating

    @max_rating.setter
    def max_rating(self, value):
        """Validate and set string data type and value for max_rating"""
        if value is None:
            self._max_rating = value
            return
        if isinstance(value, str):
            possible_values = ['g', 'pg', 'r', 'x']
            if value not in possible_values:
                raise ValueError(f'max_rating must be one of: {possible_values}')
            self._max_rating = value
        else:
            raise TypeError('max_rating must be string')

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
