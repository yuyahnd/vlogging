import pytest
from vlogging import handlers
from vlogging import DEFAUT_FORMAT

@pytest.mark.parametrize("className, level, formatter, filters", [
    ("vlogging.handlers.ConsoleHandler", "DEBUG", DEFAUT_FORMAT, []),
    ("vlogging.handlers.ConsoleHandler", "INFO", DEFAUT_FORMAT, None),
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
    ("DEBUG", DEFAUT_FORMAT, "ext://sys.stdout"),
    ("ERROR", DEFAUT_FORMAT, "ext://sys.stderr"),
    ("INFO", DEFAUT_FORMAT, None),
    ("INFO", None, None),
    (None, None, None)
])
def test_getConsleHandlerConfig(level, formatter, stream):
    config = handlers.getConsleHandlerConfig(level, formatter, stream)
    assert config.get("level", None) == level
    assert config.get("formatter", None) == formatter
    assert config.get("stream", None) == stream


@pytest.mark.parametrize("mode", ["a", "a+"])
@pytest.mark.parametrize("encoding", [None, "utf-8"])
@pytest.mark.parametrize("delay", [True, False])
def test_FileHandler(log_file, mode, encoding, delay):
    print(log_file)
    handler = handlers.FileHandler(log_file, mode, encoding, delay)
    assert handler.baseFilename == log_file
