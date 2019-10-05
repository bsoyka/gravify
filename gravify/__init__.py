import hashlib
import urllib.parse
import urllib.request

import sentry_sdk
from validate_email import validate_email

sentry_sdk.init("https://d1a3441649e64a96b52c441233c47f26@sentry.io/1763873")  # Automatic bug reporting


class Gravatar():
    def __init__(self, email, verify_email=True, default_image=None, size=None, force_default=False):
        if verify_email:
            if not validate_email(email):
                raise Exception("Invalid email address")

        self.email = email.strip().lower()
        self.default_image = default_image
        self.size = size
        self.force_default = force_default

    @property
    def url(self):
        params = {
            "s": self.size,
            "d": self.default_image,
            "f": "y" if self.force_default else None
        }

        url_params = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})

        _url = f"https://www.gravatar.com/avatar/{self.hash}"

        return f"{_url}?{url_params}" if url_params else _url

    @property
    def unsecure_url(self):
        return self.url.replace("https://", "http://")

    @property
    def hash(self):
        return hashlib.md5(self.email.encode("utf-8")).hexdigest()

    @property
    def file(self):
        return urllib.request.urlopen(self.url)

DEFAULT_AVATARS = {
        '404': '404',
        'blank': 'blank',
        'identicon': 'identicon',
        'monsterid': 'monsterid',
        'mystery_person': 'mp',
        'retro': 'retro',
        'robohash': 'robohash',
        'wavatar': 'wavatar',
    }
