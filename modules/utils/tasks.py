from modules.Qtask.qtask import QtaskCore


class RawDataLoaderTask(QtaskCore):
    kind = 'RawData.Loader'


class SellerDataLoaderTask(QtaskCore):
    kind = 'SellerData.Loader'


class MigalkiCollectTask(QtaskCore):
    kind = 'Migalki.Collect'


class MigalkiThemeTask(QtaskCore):
    kind = 'Migalki.Theme'


class DublikatCollectTask(QtaskCore):
    kind = 'Dublikat.Collect'


class DublikatThemeTask(QtaskCore):
    kind = 'Dublikat.Theme'
