from . import DBConnector

from sqlalchemy import Table, Column, Text, select


class Settings:
    TABLE = 'settings'

    def __init__(self):

        dbc = DBConnector.DBConnector()
        self.connect, meta = dbc.connect()
        self.SettingsTable = Table(
            self.TABLE,
            meta,
            Column('option_name', Text),
            Column('option_value', Text),
        )

    def get(self, option_name):
        settings = self.SettingsTable
        s = select([settings]).\
            where(settings.c.option_name == option_name).\
            limit(1)
        res = self.connect.execute(s).fetchone()
        if res:
            return res['option_value']
        return None

    def set(self, option_name, option_value):
        settings = self.SettingsTable
        q = settings.insert().values(
            option_name=option_name,
            option_value=option_value
        )
        self.connect.execute(q)
