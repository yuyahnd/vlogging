import pytest
from vlogging import handlers


@pytest.mark.parametrize("className, level, formatter, filters", [
    ("vlogging.handlers.ConsoleHandler", "DEBUG", "defaut_format", []),
    ("vlogging.handlers.ConsoleHandler", "INFO", "defaut_format", None),
    ("vlogging.handlers.ConsoleHandler", "INFO", None, None),
    ("vlogging.handlers.ConsoleHandler", None, None, None),
    (None, None, None, None),
])
def test_getHandlerConfig(className, level, formatter, filters):
    config = handlers.getHandlerConfig(className, level, formatter, filters)
    assert config.get("class") == className
    assert config.get("level", None) == level
    assert config.get("formatter", None) == formatter
    assert config.get("filters", None) == filters


@pytest.mark.parametrize("level, formatter, stream", [
    ("DEBUG", "defaut_format", "ext://sys.stdout"),
    ("ERROR", "defaut_format", "ext://sys.stderr"),
    ("INFO", "defaut_format", None),
    ("INFO", None, None),
    (None, None, None)
])
def test_getConsleHandlerConfig(level, formatter, stream):
    config = handlers.getConsleHandlerConfig(level, formatter, stream)
    assert config.get("level", None) == level
    assert config.get("formatter", None) == formatter
    assert config.get("stream", None) == stream
