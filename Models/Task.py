from sqlalchemy import Table, Column, Integer, Text, TIMESTAMP, SMALLINT

from . import DBConnector


class Task:
    TABLE = 'Qtask'
    PK = '@' + TABLE

    def __init__(self):

        dbc = DBConnector.DBConnector()
        self.connect, meta = dbc.connect()
        self.TaskTable = Table(
            self.TABLE,
            meta,
            Column(self.PK, Integer, primary_key=True),
            Column('kind', Text),
            Column('priority', SMALLINT),
            Column('params', Text),
            Column('created_at', TIMESTAMP),
            Column('delayed_to', TIMESTAMP),
            Column('extra', Text),
            Column('retries', SMALLINT)
        )

