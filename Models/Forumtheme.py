from sqlalchemy import Table, Column, Integer, Text, select

from . import DBConnector


class Forumtheme:
    TABLE = 'Forumtheme'
    PK = '@' + TABLE
    ForumthemeTable = None

    def __init__(self):

        dbc = DBConnector.DBConnector()
        self.connect, meta = dbc.connect()
        self.ForumthemeTable = Table(
            self.TABLE,
            meta,
            Column(self.PK, Integer, primary_key=True),
            Column('seller', Integer),
            Column('tradingplatform', Integer),
            Column('url', Text),
            Column('title', Text),
        )

    def get_title_by_pk(self, pk):
        s = select([self.ForumthemeTable]). \
            where(self.ForumthemeTable.c.get(self.PK) == pk)
        res = self.connect.execute(s).fetchone()
        if res:
            return res['title']
        else:
            return None

    def save(self, **fields):
        s = select([self.ForumthemeTable]).\
            where(self.ForumthemeTable.c.url == fields['url']).\
            where(self.ForumthemeTable.c.seller == fields['seller_id']).\
            where(self.ForumthemeTable.c.tradingplatform == fields['tp_id'])
        res = self.connect.execute(s).fetchone()
        if res:
            return res[self.PK]
        else:
            q = self.ForumthemeTable.insert(). \
                returning(
                self.ForumthemeTable.c.get(self.PK)
            ).values(
                url=fields['url'],
                seller=fields['seller_id'],
                tradingplatform=fields['tp_id'],
                title=fields['title']
            )
            res = self.connect.execute(q).fetchone()
            if res:
                return res[self.PK]
            else:
                return None
