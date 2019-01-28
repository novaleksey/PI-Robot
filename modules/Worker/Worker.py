from modules.utils.Config import Config
from modules.utils import tasks
from Models.Settings import Settings

import logging
import inspect
import datetime

from .PyThread import PyThread


class Worker:
    _TASKS = []
    # LOG_FILENAME = 'Logs/{}.txt'.format(datetime.datetime.strftime(datetime.datetime.now(), '%d.%m.%Y %H:%M'))

    def __init__(self):
        self.config = Config()
        self.threads_count = self.config.get_worker_config()
        s = Settings()
        logging.basicConfig(
            level=logging.DEBUG,
            format='[%(levelname)s] (%(threadName)-10s) %(message)s'
        )
        logging.getLogger('chardet.charsetprober').setLevel(logging.INFO)
        is_first_run = s.get('FirstRun')
        if is_first_run is None:
            tasks.RawDataLoaderTask.create(priority=1000)
            tasks.MigalkiCollectTask.create(priority=1000)
            tasks.DublikatCollectTask.create(priority=1000)
            s.set('FirstRun', datetime.datetime.now().strftime('%d.%m.%Y %H:%M'))
        for name, obj in inspect.getmembers(tasks):
            if inspect.isclass(obj):
                enabled = s.get(f'{obj.kind}.Включено')
                if enabled is None:
                    enabled = 0
                enabled = int(enabled)
                if enabled:
                    self._TASKS.append(obj)

    def run(self):
        threads = []
        for task in self._TASKS:
            for i in range(self.threads_count):
                thread_name = f'{task.__name__}-{i}'
                threads.append(PyThread(thread_name, task))

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

