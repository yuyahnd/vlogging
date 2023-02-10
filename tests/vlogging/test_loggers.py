from logging import FileHandler
from vlogging import (
    Formatter,
    getLogger,
    DEFAUT_CONFIG,
    DEBUG,
)
logger = getLogger("vlogger", DEFAUT_CONFIG)

def test_handler():
    fileHandler = FileHandler("test.log")
    fileHandler.setLevel(DEBUG)
    fileHandler.setFormatter(Formatter("%(asctime)s %(levelname)-8s %(filename)s:%(lineno)d: %(message)s"))
    logger.addHandler(fileHandler)
    logger.info(logger.handlers)
    for handler in logger.handlers:
        logger.info(handler.formatter)
