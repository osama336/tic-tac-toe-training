import logging
import os
import re
from datetime import datetime
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler


class MultipurposeLogger:

    _valid_name_pattern = re.compile("^[A-Za-z0-9_.-]+$")

    def __init__(self, name: str, path: str = 'logs', is_test: bool = False, create=False,
                 log_level=logging.INFO, max_bytes=10485760, backup_count=1000, rotate_time=None,
                 log_to_console=False):
        self.__name = None
        self.__path = None
        self.__log_file = None
        self.is_test = is_test
        self.log_level = log_level
        self.max_bytes = max_bytes
        self.backup_count = backup_count
        self.rotate_time = rotate_time
        self.log_to_console = log_to_console

        self.__set_name(name)
        self.__set_path(path, create=create)

        self.logger = logging.getLogger(self.__name)
        self.initialize_logger_handler()

    def get_name(self):
        return self.__name

    def get_log_file(self):
        return self.__log_file

    def __set_name(self, name):
        if not MultipurposeLogger._valid_name_pattern.match(name):
            raise ValueError("Name must contain only alphanumeric characters, underscores, hyphens, and periods.")
        self.__name = name

    def get_path(self):
        return self.__path

    def __set_path(self, path, create=False):
        try:
            if not os.path.exists(path) and create:
                os.makedirs(path, exist_ok=True)
            elif not os.path.exists(path):
                raise FileNotFoundError(f"The given path '{path}' does not exist.")
            self.__path = path
        except OSError as e:
            raise OSError(f"Error creating directory '{path}': {e}")

    def check_and_reinitialize_log_file(self):
        log_file_exists = os.path.exists(self.__log_file)
        if not log_file_exists:
            print("Log file was missing... Reinitializing log file and file handler.")
            self.warning("Log file was missing... Reinitializing log file and file handler.")
            self.initialize_logger_handler()

    def initialize_logger_handler(self):
        try:
            formatter = logging.Formatter('[%(asctime)s] || %(levelname)s :- %(message)s')
            self.__log_file = os.path.join(self.__path, f'{self.__name}_{datetime.now():%Y%m%d_%H%M%S%f}.log')

            if self.rotate_time:
                file_handler = TimedRotatingFileHandler(
                    filename=self.__log_file,
                    when=self.rotate_time,
                    backupCount=self.backup_count,
                    encoding='utf-8'
                )
                file_handler.suffix = "%Y%m%d_%H%M%S%f.log"
            else:
                file_handler = RotatingFileHandler(
                    filename=self.__log_file,
                    maxBytes=self.max_bytes,
                    backupCount=self.backup_count,
                    encoding='utf-8',
                )

            if self.log_to_console:
                console_handler = logging.StreamHandler()
                console_handler.setLevel(logging.INFO)
                console_handler.setFormatter(formatter)
                self.logger.addHandler(console_handler)

            file_handler.setLevel(self.log_level)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

            if self.is_test:
                self.logger.setLevel(logging.DEBUG)
            else:
                self.logger.setLevel(logging.INFO)

        except (OSError, IOError) as e:
            print(f"Error initializing file handler for logger: {e}")
            raise

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)


if __name__ == "__main__":
    logger = MultipurposeLogger(name="example_logger", path="logs", log_to_console=True)
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.debug("This is a debug message.")
