from .parser import DublikatParser


class DublikatTheme:

    def __init__(self):
        self._parser = DublikatParser()

    def do_request(self, request):
        try:
            self._do_request(request)
        except Exception:
            raise

    def _do_request(self, request):
        self._parser.theme_process(request)
