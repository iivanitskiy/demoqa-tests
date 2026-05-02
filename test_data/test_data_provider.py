import json


class TestDataProvider:

    def __init__(self, filename: str) -> None:
        with open(filename) as f:
            self.data = json.load(f)

    def get(self, key):
        return self.data.get(key)
