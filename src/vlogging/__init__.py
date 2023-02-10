import logging
import logging.config

from vlogging import (
    formatters,
    handlers,
    loggers,
)
from vlogging.loggers import Logger

from logging import (
    CRITICAL,
    FATAL,
    ERROR,
    WARNING,
    WARN,
    INFO,
    DEBUG,
    NOTSET,
)

__version__ = "0.0.1.2"

__all__ = ["Logger"]

class Config(object):

    DEFAUT_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "defaut_format": formatters.getFormatConfig(formatters.SIMPLE_FORMAT),
        },
        "filters": {},
        "handlers": {
            "defaut_handler": handlers.getConsleHandlerConfig("DEBUG", "defaut_format"),
        },
        "loggers": {
            "vlogging": loggers.getLoggerConfig("DEBUG", ["defaut_handler"]),
        },
    }

    def __init__(self):
       self.config = self.DEFAUT_CONFIG.copy()

    def configure(self, config: dict=None) -> None:
        if config is not None:
            self.config["formatters"] = self.configureFormatters(config)
            self.config["filters"] = self.configureFilters(config)
            self.config["handlers"] = self.configureHandlers(config)
            self.config["loggers"] = self.configureLoggers(config)
        logging.config.dictConfig(self.config)

    def configureFormatters(self, config: dict) -> dict:
        return self.configureItems(config, "formatters", "defaut_format")

    def configureFilters(self, config: dict) -> dict:
        return self.configureItems(config, "filters", None)

    def configureHandlers(self, config: dict) -> dict:
        return self.configureItems(config, "handlers", "defaut_handler")

    def configureLoggers(self, config: dict) -> dict:
        return self.configureItems(config, "loggers", "vlogging")

    def configureItems(self, config: dict, key: str, defaut: str) -> dict:
        cfg = config.get(key, {})
        result = {}
        if defaut is not None:
            if cfg.get(defaut, None) is None:
                cfg.pop(defaut, None)
            result[defaut] = self.DEFAUT_CONFIG[key][defaut].copy()
        for name in cfg:
            result[name] = cfg[name]
        return result

    def prepare(self, name) -> None:
        if name is None:
            return
        loggers = self.config.get("loggers")
        if name not in loggers.keys():
            loggers[name] = loggers.get("vlogging").copy()
            self.configure()

logging.setLoggerClass(Logger)
_config: Config = Config()
_config.configure()

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
        _config.configure(config)
    if name is not None:
        _config.prepare(name)
    return logging.getLogger(name)
