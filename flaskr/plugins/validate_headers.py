from base_plugin import BasePlugin
from utils.logger import Logger


class HeadersValidator(BasePlugin):
    @classmethod
    def is_inbound(cls):
        return True

    def __init__(self):
        super().__init__()
        self._log = Logger('HeadersValidator')
        self._config_name = 'headers'

    def check(self, payload):
        self._log.debug("checking blocked sites list.")
        for hdr in str(payload.headers).split("\r\n"):
            if self.contains(hdr):
                self._log.debug("forbidden header, blocking request.")
                return False
        return True

