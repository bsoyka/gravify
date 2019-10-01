import hashlib
import urllib.parse
import urllib.request

import sentry_sdk
from validate_email import validate_email

sentry_sdk.init("https://d1a3441649e64a96b52c441233c47f26@sentry.io/1763873")  # Automatic bug reporting


class Gravatar():

    def __init__(self, email, verify_email=True, default_image=None):
        if verify_email:
            if not validate_email(email):
                raise Exception("Invalid email address")

        self.email = email
        self.default_image = default_image

    @property
    def url(self):
        params = {}

        if self.default_image is not None:
            params["d"] = self.default_image

        _url = "https://www.gravatar.com/avatar/" + self.hash
        if params:
            return _url + "?{}".format(urllib.parse.urlencode(params))
        return _url

    @property
    def unsecure_url(self):
        return self.url.replace("https://", "http://")

    @property
    def hash(self):
        return hashlib.md5(self.email.encode("utf-8").lower()).hexdigest()

    @property
    def file(self):
        return urllib.request.urlopen(self.url)
