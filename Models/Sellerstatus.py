from . import DBConnector

from sqlalchemy import Table, Column, Integer, Text, select


class Sellerstatus:
    TABLE = 'Sellerstatus'
    PK = '@' + TABLE
    SellerstatusTable = None

    def __init__(self):

        dbc = DBConnector.DBConnector()
        self.connect, meta = dbc.connect()
        self.SellerstatusTable = Table(
            self.TABLE,
            meta,
            Column(self.PK, Integer, primary_key=True),
            Column('value', Text),
        )

    def get_pk(self, value):
        if value is None:
            return value
        s = select([self.SellerstatusTable]).\
            where(self.SellerstatusTable.c.value == value).\
            limit(1)
        res = self.connect.execute(s).fetchone()

        if res:
            return res[self.PK]
        else:
            q = self.SellerstatusTable.insert().returning(
                self.SellerstatusTable.c.get(self.PK),
            ).values(
                value=value
            )

            res = self.connect.execute(q).fetchone()
            return res[self.PK]
