from base_plugin import BasePlugin
from utils.logger import Logger


class ResponseKeywords(BasePlugin):
    @classmethod
    def is_inbound(cls):
        return True

    def __init__(self):
        super().__init__()
        self._log = Logger('ResponseKeywords')

    def check(self, payload):
        self._log.debug("checking blocked sites list.")

