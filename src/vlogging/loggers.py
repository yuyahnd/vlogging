import logging

def getLoggerConfig(level: str, handlers: list[str]) -> dict:
    config = {
        "level": level,
        "handlers": handlers,
    }
    return config

class Logger(logging.Logger):
    pass
