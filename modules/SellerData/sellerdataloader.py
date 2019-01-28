from .parser import SellerDataLoaderParser


class SellerDataLoader:

    def __init__(self):
        self.sd_parser = SellerDataLoaderParser()

    def do_request(self, request):
        try:
            self._do_request(request)
        except Exception:
            raise

    def _do_request(self, request):
        self.sd_parser.process(request)

