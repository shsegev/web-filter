from utils.logger import Logger


class ResponseKeywords:
    @classmethod
    def is_inbound(cls):
        return True

    def __init__(self):
        self._log = Logger('ResponseKeywords')

    def check(self, payload):
        self._log.debug("checking blocked sites list.")

    def add_config(self, prop, value):
        self._log.debug(f"Adding {prop} to config, value={value}.")

    def del_config(self, prop):
        self._log.debug(f"Removing {prop} from config")

