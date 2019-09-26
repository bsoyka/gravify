import urllib, hashlib

class Gravatar():
    
    def __init__(self, email):
        self.email = email

    @property
    def url(self):
        return "https://www.gravatar.com/avatar/" + hashlib.md5(self.email.encode("utf-8").lower()).hexdigest()
    
    @property
    def unsecure_url(self):
        return self.url.replace("https://", "http://")
