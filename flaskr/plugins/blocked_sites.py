class BlockedSites:
    @classmethod
    def is_inbound(cls):
        return True

    def check(self, payload):
        pass

    def add_config(self, prop, value):
        pass

    def del_config(self, prop):
        pass