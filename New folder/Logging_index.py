import logging
from logging.handlers import RotatingFileHandler

# logging.basicConfig(level=logging.INFO, format="%(asctime)s->%(levelname)s->%(message)s,",filename="test.log")
#
# logging.info("Hello World!!!")
# logging.critical("This is a critical log ......")

logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler()
consoleFormatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s",datefmt="%Y/%m/%d %H:%M:%S")
consoleHandler.setFormatter(consoleFormatter)

fileHandler = RotatingFileHandler("test.log",maxBytes=1,backupCount=100)
fileHandler.setFormatter(consoleFormatter)

logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

logger.info("info log")
logger.warning("this is warning log")

try:
    x = 1/0
except Exception as e :
    logger.error("Some error occured", exc_info=e)
