import requests

class Service_Api:
    def __init__(self, url: str) -> None:
        self.URL = url + "/"
        self.AUTH_URL = url + "/auth/login"
