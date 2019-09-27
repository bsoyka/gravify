import urllib, hashlib
from validate_email import validate_email
is_valid = validate_email('example@example.com')

class Gravatar():
    
    def __init__(self, email, verify_email=True):
        if verify_email:
            if not validate_email(email):
                raise Exception("Invalid email address")
        self.email = email

    @property
    def url(self):
        return "https://www.gravatar.com/avatar/" + hashlib.md5(self.email.encode("utf-8").lower()).hexdigest()
    
    @property
    def unsecure_url(self):
        return self.url.replace("https://", "http://")
