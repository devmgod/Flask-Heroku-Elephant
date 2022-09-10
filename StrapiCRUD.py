import json
import requests

class Articles:
    def __init__(self):
        self.api_url = "http://localhost:1337/api"

    def all(self):
        r = requests.get(self.api_url + "/articles")
        return r.json()