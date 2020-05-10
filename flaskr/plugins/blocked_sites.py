from urllib.parse import urlparse

from base_plugin import BasePlugin
from utils.logger import Logger


class BlockedSites(BasePlugin):
    @classmethod
    def is_inbound(cls):
        return True

    def __init__(self):
        super().__init__()
        self._log = Logger('BlockedSites')
        self._config_name = 'sites'

    def check(self, payload):
        self._log.debug("checking blocked sites list.")
        if self.contains(urlparse(payload.base_url).hostname):
            self._log.debug("Blocked site found, returning error page.")
            return False
        else:
            return True

