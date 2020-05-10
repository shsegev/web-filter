import logging
import logging.handlers
import sys
import threading


def init_logger(name, output_file="", level=logging.DEBUG):
    the_logger = logging.getLogger(name)
    formatter = logging.Formatter('%(asctime)s\t %(name)-32s %(levelname)-8s %(message)s')
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(level)
    the_logger.addHandler(stream_handler)
    if output_file != "":
        file_handler = logging.handlers.RotatingFileHandler(output_file, 'a', 15 * 1024 * 1024, 100)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)
        the_logger.addHandler(file_handler)
    the_logger.setLevel(level)
    the_logger.info(f"logging started {output_file}")
    return the_logger


class Logger(object):
    WARN = logging.WARN
    ERROR = logging.ERROR
    DEBUG = logging.DEBUG
    INFO = logging.INFO

    def __init__(self, name):
        self._logger = logging.getLogger(name)

    def warn(self, messages):
        self._logger.warning(self._add_thread_id(messages))

    def debug(self, messages):
        self._logger.debug(self._add_thread_id(messages))

    def info(self, messages):
        self._logger.info(self._add_thread_id(messages))

    def error(self, messages):
        self._logger.error(self._add_thread_id(messages))

    @staticmethod
    def _add_thread_id(messages):
        thread_name = threading.currentThread().getName()
        messages = "[Th:%s] %s" % (thread_name, messages)
        return messages

    def set_level(self, level):
        self._logger.setLevel(level)
