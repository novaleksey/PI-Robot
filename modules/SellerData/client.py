from modules.utils.Client import Client


class DataClient:

    def __init__(self):
        self._client = Client()

    def get_seller_page(self, url):
        return self._client.get_page(url=url)
