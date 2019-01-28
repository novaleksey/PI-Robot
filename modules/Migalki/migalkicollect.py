from .parser import MigalkiParser


class MigalkiCollect:

    def __init__(self):
        self._parser = MigalkiParser()

    def do_request(self, request):
        try:
            self._do_request(request)
        except Exception:
            raise

    def _do_request(self, request):
        self._parser.collect_process(request)
