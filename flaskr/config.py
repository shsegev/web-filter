import json
import traceback

from utils.logger import Logger


class _Config:
    def __init__(self, path="conf/filter.json"):
        self._log = Logger('config')
        self.conf_path = path
        self._ready = False
        self.params = None

    def read_config(self):
        self._log.debug(f"reading configuration from {self.conf_path}")
        try:
            self.params = json.load(open(self.conf_path, "r"))
        except (json.JSONDecodeError, FileNotFoundError):
            self._log.error("Error reading configuration file.")
            self._log.error(traceback.format_exc())
        self._ready = True

    @property
    def ready(self):
        return self._ready


config = _Config()


class Config:
    def __init__(self):
        if not config.ready:
            config.read_config()

    @property
    def params(self):
        return config.params


