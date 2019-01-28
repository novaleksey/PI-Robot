import datetime

import bs4
import json
from requests.exceptions import Timeout

from .client import DataClient
from Models.Seller import Seller
from Models.Profile import Profile
from Models.Tradingplatform import Tradingplatform
from Models.Forumtheme import Forumtheme

from modules.utils import parse




class SellerDataLoaderParser:

    def __init__(self):
        self.dclient = DataClient()
        self.bstree = None
        self.extra = None
        self.task = None

    def process(self, task):
        self.extra = json.loads(task.extra)
        self.task = task
        if task.params:
            try:
                page = self.dclient.get_seller_page(task.params)
            except Timeout:
                task.delay_for(datetime.timedelta(minutes=10))
            if page is not None:
                self.bstree = bs4.BeautifulSoup(page.content, 'html.parser')
                self.save_seller()
            else:
                task.done()

    def save_seller(self):
        blocks = self.bstree.select('.single_contacts div')
        contacts = {}
        for block in blocks:
            contact_key = block.select_one('.thin').text
            block.span.clear()
            contact_val = parse.normalize_string(block.text)

            contacts.update({
                contact_key: contact_val
            })

        views = parse.normalize_string(
            self.bstree.select_one('.views_count').text
        )
        if views:
            contacts['views'] = views
        seller_id = Seller().save(
            nickname=self.extra['nickname'],
            status=self.extra['status'],
            worktype=self.extra['worktype'],
            contacts=json.dumps(contacts, ensure_ascii=False)
        )
        if seller_id:
            self.save_profile(seller_id)

    def save_profile(self, seller_id):

        profiles = self.bstree.select('.forum_info')
        for profile in profiles:
            profile_info = {}
            infos = profile.select('.forum_col')
            for info in infos:
                key = info.select_one('span').text
                link_block = info.select('a')
                if link_block:
                    if len(link_block) > 1:
                        val = [item.get('href') for item in link_block]
                    else:
                        val = link_block[0].get('href')
                else:
                    info.span.clear()
                    val = parse.normalize_string(info.text)
                profile_info.update({key: val})

            trading_platform = parse.parse_url(profile_info['Ссылка на профиль:'])
            tp_id = Tradingplatform().save(trading_platform)
            date_mask = '%d.%m.%Y' if len(profile_info['Дата регистрации:']) > 8 else '%d.%m.%y'

            try:
                register_at = datetime.datetime.strptime(profile_info['Дата регистрации:'], date_mask)
            except ValueError:
                register_at = None

            Profile().save(
                deposit=parse.parse_deposit(profile_info['Депозит:']),
                tp_id=tp_id,
                register_at=register_at,
                seller_id=seller_id,
                status=profile_info['Статус:'],
                success_deal=profile_info['Продажи через гарант:'] if profile_info['Продажи через гарант:'] else 0,
                url=profile_info['Ссылка на профиль:']
            )
            urls = profile_info['Темы на форуме'] if isinstance(profile_info['Темы на форуме'], list) else [profile_info['Темы на форуме']]
            self.save_forum_theme(
                seller_id=seller_id,
                tp_id=tp_id,
                urls=urls
            )
        self.task.delay_for(datetime.timedelta(days=1))

    def save_forum_theme(self, **fields):
        for url in fields['urls']:
            Forumtheme().save(
                seller_id=fields['seller_id'],
                tp_id=fields['tp_id'],
                url=url,
                title=None
            )




