from .parser import RawDataLoaderParser


class RawDataLoader:

    def __init__(self):
        self.rd_parser = RawDataLoaderParser()

    def do_request(self, request):
        try:
            self._do_request(request)
        except Exception:
            raise

    def _do_request(self, request):
        self.rd_parser.process(request)

