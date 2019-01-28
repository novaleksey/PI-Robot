from . import DBConnector
from sqlalchemy import Table, Column, Integer, Text, select


class Tradingplatform:
    TABLE = 'Tradingplatform'
    PK = '@' + TABLE
    TradingplatformTable = None

    def __init__(self):

        dbc = DBConnector.DBConnector()
        self.connect, meta = dbc.connect()
        self.TradingplatformTable = Table(
            self.TABLE,
            meta,
            Column(self.PK, Integer, primary_key=True),
            Column('url', Text),
        )

    def get_id_by_url(self, url):
        s = select([self.TradingplatformTable]).where(self.TradingplatformTable.c.url == url)
        res = self.connect.execute(s).fetchone()
        return res[self.PK] if res else None

    def save(self, url):
        s = select([self.TradingplatformTable]).where(self.TradingplatformTable.c.url == url)
        res = self.connect.execute(s).fetchone()
        if res:
            return res[self.PK]
        else:
            q = self.TradingplatformTable.insert(). \
                returning(
                self.TradingplatformTable.c.get(self.PK)
            ).values(
                url=url,
            )
            res = self.connect.execute(q).fetchone()
            if res:
                return res[self.PK]
            else:
                return None
