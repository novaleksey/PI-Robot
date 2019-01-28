import sqlalchemy

from modules.utils.Config import Config


class DBConnector:
    def __init__(self):
        self.config = Config()

    def connect(self):
        username, password, hostname, port, db_name = self.config.get_db_config()
        conn_string = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}'.format(
            user=username,
            password=password,
            host=hostname,
            port=port,
            db_name=db_name,
        )

        connect = sqlalchemy.create_engine(conn_string)
        meta = sqlalchemy.MetaData(connect)

        return connect, meta
