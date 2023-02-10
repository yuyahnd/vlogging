import pytest
from vlogging import loggers


@pytest.mark.parametrize("level, handlers, propagate, filters", [
    ("DEBUG", ["defaut_handler"], None, None),
    ("INFO", [], True, []),
    (None, None, None, None),
])
def test_getLoggerConfig(level, handlers, propagate, filters):
    config = loggers.getLoggerConfig(level, handlers, propagate, filters)
    assert config.get("level", None) == level
    assert config.get("handlers", None) == handlers
    assert config.get("propagate", None) == propagate
    assert config.get("filters", None) == filters
