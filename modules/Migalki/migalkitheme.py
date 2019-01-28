from .parser import MigalkiParser


class MigalkiTheme:

    def __init__(self):
        self._parser = MigalkiParser()

    def do_request(self, request):
        try:
            self._do_request(request)
        except Exception:
            raise

    def _do_request(self, request):
        self._parser.theme_process(request)
