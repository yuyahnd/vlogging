import logging

def getHandlerConfig(level: str, formatter: str,
                className: str,
                **kwargs) -> dict:
    config = {
        "class": className,
        "level": level,
        "formatter": formatter,
    }
    config.update(kwargs)
    return config

def getConsleHandlerConfig(level: str, formatter: str,
                        stream: str = "ext://sys.stdout") -> dict:
    return getHandlerConfig(
        level,
        formatter,
        "vlogging.handlers.ConsoleHandler",
        stream = stream)

class ConsoleHandler(logging.StreamHandler):
    pass
