import re

from config import Config
from utils.logger import Logger


class BasePlugin:

    def __init__(self):
        self._log = Logger('baseplugin')
        self._config_name = ""
        self._pattern = None
        self._enabled = True
        self._re = None

    def contains(self, obj: str):
        result = self._re.search(obj)
        if result:
            self._log.debug(f"found {result} in stream.")
            return True
        else:
            return False

    def load_config(self):
        # for all current plugins, the implemention is based on the same concept.
        # Check for existing text in a section
        conf = Config()
        try:
            self._enabled = conf.params[self._config_name]['enabled'] == "1"
            self._pattern = "|".join(conf.params[self._config_name]["values"])
        except KeyError:
            self._log.error(f"configuration values 'enabled' or value not found in {self._config_name}")
        try:
            self._re = re.compile(self._pattern)
        except re.error:
            self._log.error(f"unable to compile regexp {self._pattern}")

    def add_config(self, prop, value):
        self._log.debug(f"Adding {prop} to config, value={value}.")
        self._log.warn("Not implemented!!")

    def del_config(self, prop):
        self._log.debug(f"Removing {prop} from config")
        self._log.warn("Not implemented!!")
