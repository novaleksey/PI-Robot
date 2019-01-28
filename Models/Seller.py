from sqlalchemy import Table, Column, Integer, Text, select

from . import DBConnector
from Models.Sellerstatus import Sellerstatus


class Seller:
    TABLE = 'Seller'
    PK = '@' + TABLE
    SellerTable = None

    def __init__(self):

        dbc = DBConnector.DBConnector()
        self.connect, meta = dbc.connect()
        self.SellerTable = Table(
            self.TABLE,
            meta,
            Column(self.PK, Integer, primary_key=True),
            Column('contacts', Text),
            Column('nickname', Text),
            Column('status', Integer),
            Column('worktype', Text),
        )

    def get_id_by_nickname(self, nickname):
        s = select([self.SellerTable]).where(self.SellerTable.c.nickname == nickname)

        res = self.connect.execute(s).fetchone()
        return res[self.PK] if res else None

    def get_nickname_by_id(self, pk):
        s = select([self.SellerTable]).where(self.SellerTable.c.get(self.PK) == pk)

        res = self.connect.execute(s).fetchone()
        return res['nickname'] if res else None

    def save(self, nickname, contacts=None, status=None, worktype=None):

        s = select([self.SellerTable]).where(self.SellerTable.c.nickname == nickname)
        res = self.connect.execute(s).fetchone()
        if res:
            upd = self.SellerTable.update().values(
                contacts=contacts,
                status=Sellerstatus().get_pk(status),
                worktype=worktype
            ).where(
                self.SellerTable.c.nickname == nickname
            )
            self.connect.execute(upd)
            return res[self.PK]
        else:
            q = self.SellerTable.insert().\
                returning(
                    self.SellerTable.c.get(self.PK)
                ).values(
                    contacts=contacts,
                    nickname=nickname,
                    status=Sellerstatus().get_pk(status),
                    worktype=worktype
                )

            res = self.connect.execute(q).fetchone()
            if res:
                return res[self.PK]
            else:
                return None


