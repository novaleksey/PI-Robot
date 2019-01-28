from sqlalchemy import Table, Column, Integer, Text, TIMESTAMP, select

from . import DBConnector


class Profile:
    TABLE = 'Profile'
    PK = '@' + TABLE
    ProfileTable = None

    def __init__(self):

        dbc = DBConnector.DBConnector()
        self.connect, meta = dbc.connect()
        self.ProfileTable = Table(
            self.TABLE,
            meta,
            Column(self.PK, Integer, primary_key=True),
            Column('deposit', Integer),
            Column('platform', Integer),
            Column('register_at', TIMESTAMP),
            Column('seller', Integer),
            Column('status', Text),
            Column('success_deal', Integer),
            Column('url', Text),
        )

    def save(self, **fields):
        s = select([self.ProfileTable]).where(self.ProfileTable.c.seller == fields['seller_id']).\
            where(self.ProfileTable.c.platform == fields['tp_id'])
        res = self.connect.execute(s).fetchone()
        if res:
            upd = self.ProfileTable.update().values(
                deposit=fields['deposit'],
                status=fields['status'],
                success_deal=fields['success_deal']
            ).where(
                self.ProfileTable.c.get(self.PK) == res[self.PK]
            )
            self.connect.execute(upd)
            return res[self.PK]
        else:
            q = self.ProfileTable.insert(). \
                returning(
                self.ProfileTable.c.get(self.PK)
            ).values(
                deposit=fields['deposit'],
                platform=fields['tp_id'],
                register_at=fields['register_at'],
                seller=fields['seller_id'],
                status=fields['status'],
                success_deal=fields['success_deal'],
                url=fields['url']
            )

            res = self.connect.execute(q).fetchone()
            if res:
                return res[self.PK]
            else:
                return None
