import inspect
import traceback
from pathlib import Path
import importlib
from utils.logger import Logger


class _PluginRepository:
    def __init__(self):
        self._initialized = False
        self._inbound_filters = []
        self._outbound_filters = []
        self._log = Logger("PluginRepository")

    def filter(self, payload, inbound):
        if not self._initialized:
            self._log.error("Plugins Repository was not initialized")
            return True

        fl_list = self._inbound_filters if inbound else self._outbound_filters
        for fil in fl_list:
            if not fil.check(payload):
                return False
        return True

    def load_filters(self, path):
        if self._initialized:
            return
        p = Path(path)
        for fil in p.glob("*.py"):
            module_name = str(fil).strip(".py")
            try:
                importlib.import_module('.' + module_name, package=__name__)
                self._log.debug(f'Loaded module {module_name}')
                for m in inspect.getmembers(module_name, inspect.isclass):
                    if hasattr(m[1], 'is_inbound') and hasattr(m[1], "check"):
                        if m[1].is_inbound:
                            self._inbound_filters.append(m[1])
                            self._log.debug(f"Class {m[0]} appended to inbound filters")
                        else:
                            self._outbound_filters.append(m[1])
                            self._log.debug(f"Class {m[0]} appended to outbound filters")
                    else:
                        self._log.warn(f"{m[0]} in {module_name} is not a valid filter class.")

            except (NameError, SyntaxError):
                self._log.error(f'Module {module_name} cannot be loaded!')
                self._log.error(traceback.format_exc())
        self._initialized = True


class PluginManager:
    def __init__(self):
        self._repo = plugin_repository

    def filter(self, payload, inbound=True):
        self._repo.filter(payload, inbound)

    def config(self):
        # TODO: implement configuration
        pass


plugin_repository = _PluginRepository()
