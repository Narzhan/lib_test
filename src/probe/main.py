import requests


class SuperProbe:
    def __init__(self, url: str):
        self.url = url

    def get_page(self) -> int:
        try:
            req = requests.get(self.url)
        except Exception as e:
            return 0
        else:
            return req.status_code
        
