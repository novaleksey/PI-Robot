from modules.utils.Client import Client
from requests.exceptions import ConnectionError, MissingSchema


class DataClient:
    _DOMAIN = 'http://migalki.pw/forum/forums/info-baza.144/page-{}'

    def __init__(self):
        self._client = Client()

    def _get_page(self, **kwargs):
        return self._client.get_page(**kwargs)

    def search(self):
        page = 1
        while True:
            if page == 1:
                res = self._get_page(url=self._DOMAIN.format(page))
            else:
                res = self._get_page(url=self._DOMAIN.format(page), allow_redirects=False)
            if res.status_code == 303:
                break
            page += 1
            yield res

    def get_theme_page(self, url, page=None):
        if page:
            url = '{}/page-{}'.format(url, page)
        return self._get_page(url=url)

    def get_media(self, url):
        try:
            r = self._get_page(url=url, stream=True)
            r.raw.decode_content = True
            return r
        except ConnectionError:
            print('Файл не доступен')
            return None
        except MissingSchema:
            print('Неверный url')
            return None

