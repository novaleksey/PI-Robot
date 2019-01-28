import requests


class Client:
    _PROXIES = {
        'http': 'socks5://198.50.217.202:1080'
    }

    @staticmethod
    def get_page(**kwargs):
        try:
            response = requests.get(**kwargs)
            return response
        except Exception:
            raise
