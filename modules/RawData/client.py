from urllib.parse import urljoin

from modules.utils.Client import Client


class DataClient:
    _DOMAIN = 'http://darkseller.org'
    url = urljoin(_DOMAIN, '?sf_paged=1')

    def __init__(self):
        self._client = Client()

    def search(self):
        while True:
            res = self._client.get_page(url=self.url)
            yield res
