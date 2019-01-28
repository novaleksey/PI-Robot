import datetime

import bs4
import json

from .client import DataClient
from modules.utils import parse
from modules.utils.tasks import SellerDataLoaderTask


class RawDataLoaderParser:

    def __init__(self):
        self.dclient = DataClient()
        self.bstree = None

    def process(self, task):
        for page in self.dclient.search():
            self.bstree = bs4.BeautifulSoup(page.content, 'html.parser')
            link = self.get_link_next_page()

            if not link:
                task.delay_for(datetime.timedelta(days=5))
                break
            self.dclient.url = link
            self.collect_sellers()

    def get_link_next_page(self):
        if self.bstree.select_one("link[rel=next]") is None:
            return False
        else:
            return self.bstree.select_one("link[rel=next]").get('href')

    def collect_sellers(self, ):
        sellers_blocks = self.bstree.select("div[id=main] > .seller")
        for seller_block in sellers_blocks:
            seller_short_info = {
                'nickname': seller_block.select_one('.seller_name').text,
                'worktype': parse.normalize_string(
                    seller_block.select_one('.direction').text.split(':')[-1]
                ),
                'status': parse.normalize_string(
                    seller_block.select_one('.status').text.split(':')[-1]
                )
            }
            SellerDataLoaderTask.create(
                params=seller_block.select_one("a[class=details]").get('href'),
                extra=json.dumps(seller_short_info, ensure_ascii=False),
                priority=50,
                delayed_to=datetime.datetime.now() + datetime.timedelta(hours=4)
            )


