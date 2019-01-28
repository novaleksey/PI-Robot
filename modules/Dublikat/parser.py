import os
import shutil
import datetime

import bs4
import json
from urllib.parse import urljoin

from .client import DataClient
from modules.utils import parse
from Models.Seller import Seller
from Models.Forumdata import Forumdata
from Models.Forumtheme import Forumtheme
from modules.utils.tasks import DublikatThemeTask
from Models.Tradingplatform import Tradingplatform


class DublikatParser:
    _DOMAIN = r'https://dublik.at'

    def __init__(self):
        self._client = DataClient()

    def collect_process(self, task):
        tradingplatformid = Tradingplatform().get_id_by_url(self._DOMAIN)

        for page in self._client.search():
            bstree = bs4.BeautifulSoup(page.content, 'html.parser')
            themes_block = bstree.select('.structItem.structItem--thread')

            for theme in themes_block:
                row = theme.find('div', {'class': 'structItem-title'})
                title = parse.normalize_string(row.text)
                link = urljoin(self._DOMAIN, row.find_all('a', href=True)[-1]['href'])
                seller_nickname = parse.normalize_string(theme.select_one('.username').text)
                seller_id = Seller().get_id_by_nickname(seller_nickname)
                if seller_id is None:
                    seller_id = Seller().save(
                            nickname=seller_nickname,
                            worktype="Базы данных",
                        )
                forumtheme_id = Forumtheme().save(
                    url=link,
                    seller_id=seller_id,
                    tp_id=tradingplatformid,
                    title=title
                )
                DublikatThemeTask.create(
                    extra=json.dumps({'seller_id': seller_id, 'forumtheme_id': forumtheme_id}),
                    params=link,
                    priority=50,
                    delayed_to=datetime.datetime.now() + datetime.timedelta(hours=2)
                )

            task.delay_for(datetime.timedelta(days=1))

    def theme_process(self, task):
        self._task = task

        bstree = bs4.BeautifulSoup(
            self._client.get_theme_page(url=task.params).text,
            'html.parser'
        )
        self.save_theme_info(bstree)
        pages_count = int(bstree.select('.pageNav-page')[-1].text) if len(bstree.select('.pageNav-page')) else 1
        if pages_count > 1:
            for page_num in range(2, pages_count):
                bstree = bs4.BeautifulSoup(
                    self._client.get_theme_page(url=task.params, page=page_num).text,
                    'html.parser'
                )
                self.save_theme_info(bstree)

        task.delay_for(datetime.timedelta(days=1))

    def save_theme_info(self, bs):
        messages = bs.select('.message-inner')
        seller_name = Seller().get_nickname_by_id(
            json.loads(self._task.extra)['seller_id']
        )
        messages_raw_data = []
        title = ''
        for message in messages:
            if parse.normalize_string(message.select_one('.message-name').text) == seller_name:
                messages_raw_data.append(
                    {
                        'message': message.select_one('.bbWrapper').text,
                        'date': message.select_one('.u-dt').get('datetime')
                    }
                )
                medias = message.select('img.bbImage')
                if medias:
                    title = Forumtheme().get_title_by_pk(
                        json.loads(self._task.extra)['forumtheme_id']
                    )

                    for media in medias:
                        filename = media.get('src').split('/')[-1]
                        if not filename:
                            filename = media.get('src').split('/')[-2]
                        path = 'Media/{}/{}'.format(title, filename)
                        if os.path.isfile(path):
                            continue
                        if not os.path.exists(os.path.dirname(path)):
                            os.makedirs(os.path.dirname(path))
                        img = self._client.get_media(media.get('src'))
                        if img is None:
                            continue
                        with open(path, 'wb') as f:
                            shutil.copyfileobj(img.raw, f)

        Forumdata().save(
            seller_id=json.loads(self._task.extra)['seller_id'],
            forumtheme_id=json.loads(self._task.extra)['forumtheme_id'],
            media='Media/{}'.format(title) if title else None,
            raw_content=json.dumps(messages_raw_data, ensure_ascii=False)
        )









