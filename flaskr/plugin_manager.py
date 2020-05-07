from pathlib import Path


class _PluginRepository:
    def __init__(self):
        self.initialized = False
        self.inbound_filters = ()
        self.outbound_filters = ()

    def filter(self, payload, inbound=True):
        fl_list = self.inbound_filters if inbound else self.outbound_filters
        for fil in fl_list:
            if not fil.check(payload):
                return False
        return True

    def load_filters(self, path):
        p = Path(path)
        for filters in p.glob("*.py"):
            module