from sqlalchemy import Table, Column, Integer, Text, select

from . import DBConnector


class Forumdata:
    TABLE = 'Forumdata'
    PK = '@' + TABLE
    ForumdataTable = None

    def __init__(self):

        dbc = DBConnector.DBConnector()
        self.connect, meta = dbc.connect()
        self.ForumdataTable = Table(
            self.TABLE,
            meta,
            Column(self.PK, Integer, primary_key=True),
            Column('raw_content', Integer),
            Column('media', Integer),
            Column('seller_id', Text),
            Column('forumtheme_id', Text),
        )

    def save(self, **fields):
        s = select([self.ForumdataTable]).\
            where(self.ForumdataTable.c.seller_id == fields['seller_id']).\
            where(self.ForumdataTable.c.forumtheme_id == fields['forumtheme_id'])
        res = self.connect.execute(s).fetchone()
        if res:
            return res[self.PK]
        else:
            q = self.ForumdataTable.insert(). \
                returning(
                self.ForumdataTable.c.get(self.PK)
            ).values(
                media=fields['media'],
                seller_id=fields['seller_id'],
                forumtheme_id=fields['forumtheme_id'],
                raw_content=fields['raw_content']
            )
            res = self.connect.execute(q).fetchone()
            if res:
                return res[self.PK]
            else:
                return None
