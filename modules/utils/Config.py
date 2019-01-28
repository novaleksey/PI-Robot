import os

from configparser import ConfigParser

CONFIG_PATH = './pi-robot.config.ini'


def config_checker(func):
    def wrapper(self):
        if not os.path.exists(CONFIG_PATH):
            raise Exception('Не найден файл конфигурации')
        else:
            return func(self)
    return wrapper


class Config(ConfigParser):
    @config_checker
    def get_db_config(self):
        section = 'Core.Database'
        self.read(CONFIG_PATH)

        username = self.get(section, 'user')
        password = self.get(section, 'password')
        hostname = self.get(section, 'host')
        port = self.get(section, 'port')
        db_name = self.get(section, 'dbname')

        return username, password, hostname, port, db_name

    @config_checker
    def get_worker_config(self):
        section = 'Workers'
        self.read(CONFIG_PATH)

        workers_count = int(self.get(section, 'count'))

        return workers_count

