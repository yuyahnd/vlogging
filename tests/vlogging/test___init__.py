##------------------------------------------------------------------------------
## Usage:
## pytest -s
## pytest --durations=0 -v
##------------------------------------------------------------------------------

import pytest
import vlogging

@pytest.mark.parametrize("name, expected", [
    ("vlogging", "vlogging"),
    (__name__, __name__),
    (None, "root")
])
def test_vlogging(name, expected):
    logger = vlogging.getLogger(name)
    print(type(logger))
    logger.critical('TEST critical')
    logger.error('TEST error')
    logger.warning("TEST warning")
    logger.info('TEST info')
    logger.debug('TEST debug')
    assert logger.name == expected

@pytest.mark.parametrize("config", [
    (None),
    ({}),
])
def test_config_configure(config):
    vlogging._config.configure(config)
    cfg = vlogging._config.config
    assert cfg.get("formatters") is not None
    assert cfg.get("filters") is not None
    assert cfg.get("handlers") is not None
    assert cfg.get("loggers") is not None
