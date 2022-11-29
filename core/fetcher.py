import requests


class FetchResult(object):
    def __init__(self, data: str) -> None:
        self.data = data


class Fetcher(object):
    def Get(url: str) -> FetchResult:
        r = requests.get(url)
        return FetchResult(r.text)
