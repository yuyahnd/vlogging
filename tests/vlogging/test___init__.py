##------------------------------------------------------------------------------
## Usage:
## pytest -s
## pytest --durations=0 -v
##------------------------------------------------------------------------------

import pytest
import vlogging

def test_vlogging():
    print(type(vlogging))
    vlogging.critical("TEST critical")
    vlogging.fatal("TEST fatal")
    vlogging.error("TEST error")
    vlogging.warning("TEST warning")
    vlogging.info("TEST info")
    vlogging.debug("TEST debug")
    vlogging.log(vlogging.INFO, "TEST log")
    try:
        raise Exception("TEST exception")
    except Exception as e:
        vlogging.exception(e)


@pytest.mark.parametrize("name, expected", [
    ("vlogging", "vlogging"),
    (__name__, __name__),
    (None, "root")
])
def test_getLogger(name, expected):
    logger = vlogging.getLogger(name)
    print(type(logger))
    logger.critical("TEST critical")
    logger.error("TEST error")
    logger.warning("TEST warning")
    logger.info("TEST info")
    logger.debug("TEST debug")
    assert logger.name == expected


@pytest.fixture
def vconfig():
    return vlogging._config


@pytest.mark.parametrize("config", [
    (None),
    ({}),
])
def test_config_configure(vconfig, config):
    vconfig.configure(config)
    cfg = vconfig.config
    assert cfg.get("formatters") is not None
    assert cfg.get("filters") is not None
    assert cfg.get("handlers") is not None
    assert cfg.get("loggers") is not None


@pytest.mark.parametrize("config", [
    (None),
    ({}),
    ({"formatters": {"defaut_format": None}})
])
def test_config_configureFormatters(vconfig, config):
    cfg = vconfig.configureFormatters(config)
    assert cfg.get("defaut_format") is not None


@pytest.mark.parametrize("config", [
    (None),
    ({}),
    ({"filters": {"defaut_filter": None}})
])
def test_config_configureFilters(vconfig, config):
    cfg = vconfig.configureFilters(config)
    assert cfg.get("defaut_filter", None) is None


@pytest.mark.parametrize("config", [
    (None),
    ({}),
    ({"handlers": {"defaut_handler": None}})
])
def test_config_configureHandlers(vconfig, config):
    cfg = vconfig.configureHandlers(config)
    assert cfg.get("defaut_handler") is not None


@pytest.mark.parametrize("config", [
    (None),
    ({}),
    ({"loggers": {"vlogging": None}})
])
def test_config_configureLoggers(vconfig, config):
    cfg = vconfig.configureLoggers(config)
    assert cfg.get("vlogging") is not None


@pytest.mark.parametrize("config, key, defaut", [
    ({"handlers": {"defaut_handler": None}}, "handlers", "defaut_handler"),
    ({"loggers": {"vlogging": None}},        "loggers",  "vlogging"),
])
def test_config_configureItems(vconfig, config, key, defaut):
    cfg = vconfig.configureItems(config, key, defaut)
    assert cfg.get(defaut) is not None


@pytest.mark.parametrize("key, defaut", [
    ("formatters", "defaut_format"),
    ("filters",     None),
    ("handlers",   "defaut_handler"),
    ("loggers",    "vlogging"),
])
def test_config_configureDefautConfig(vconfig, key, defaut):
    cfg = vconfig.configureDefautConfig(key, defaut)
    if defaut is not None:
        assert cfg.get(defaut) is not None
    else:
        assert len(cfg.keys()) == 0
