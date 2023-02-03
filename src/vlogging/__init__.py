from logging.config import dictConfig as _dictConfig
from logging import (
    getLogger as _getLogger,
    Logger
)

from vlogging.formatters import VFormatter

__version__ = "0.0.1"

__all__ = ["VFormatter"]

DEFAUT_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "class": "vlogging.VFormatter",
            "format": "%(asctime)s %(levelname)-8s %(message)s",
        },
        "basic": {
            "class": "vlogging.VFormatter",
            "format": "%(asctime)s %(levelname)-8s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S.%f"
        }
    },
    "handlers": {
        "consoleHandler": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
    },
    "loggers": {
        "vlogger": {
            "level": "DEBUG",
            "handlers": [
                "consoleHandler"
            ]
        }
    },
    "root": {
        "level": "ERROR"
    }
}

def getLogger(name: str=None, config: dict=None) -> Logger:
    """
    Return a logger with the specified name, creating it if necessary.

    If no name is specified, return the root logger.

    Parameters
    ----------
    name : str, optional
        logger name, by default None
    config : dict, optional
        Configure logging using a dictionary, by default None

    Returns
    -------
    Logger
        logger
    """
    if config is not None:
        _dictConfig(config)
    return _getLogger(name)

logger = getLogger("vlogger", DEFAUT_CONFIG)
