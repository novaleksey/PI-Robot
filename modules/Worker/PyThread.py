import threading
import datetime
import logging
import time


class PyThread(threading.Thread):
    def __init__(self, name, obj):
        super().__init__()
        self.threadID = name
        self.obj = obj
        self.lock = threading.Lock()

    def run(self):
        print('Start Thread-' + self.threadID)
        # self.lock.acquire()
        self._get_task()
        # self.lock.release()
        print('Finish Thread-' + self.threadID)

    def _get_task(self):
        task_cls = self.obj
        consumer_cls_name = task_cls.kind.replace('.', '')
        fr = 'modules.{}.{}'.format(task_cls.kind.split('.')[0], consumer_cls_name.lower())
        module = __import__(fr, fromlist=[consumer_cls_name])
        consumer_cls = getattr(module, consumer_cls_name)
        consumer_obj = consumer_cls()
        while True:
            try:
                task = self.obj.get_task()
                if task is None:
                    time.sleep(3)
                else:
                    consumer_obj.do_request(request=task)
            except Exception as e:
                logging.exception(str(e))
                task.delay_for(datetime.timedelta(hours=5))
                time.sleep(5)
                continue




