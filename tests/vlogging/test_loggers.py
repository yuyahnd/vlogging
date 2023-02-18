import pytest
from vlogging import loggers
from vlogging import DEFAUT_HANDLER

@pytest.mark.parametrize("level, handlers, propagate, filters", [
    ("DEBUG", [DEFAUT_HANDLER], None, None),
    ("INFO", [], True, []),
    (None, None, None, None),
])
def test_getLoggerConfig(level, handlers, propagate, filters):
    config = loggers.getLoggerConfig(level, handlers, propagate, filters)
    assert config.get("level", None) == level
    assert config.get("handlers", None) == handlers
    assert config.get("propagate", None) == propagate
    assert config.get("filters", None) == filters
