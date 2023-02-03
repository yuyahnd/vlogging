import pytest
from vlogging import logger

def test_vlogging():
    print(type(logger))
    assert True

def test_critical():
    logger.critical('TEST critical')
    assert True

def test_error():
    logger.error('TEST error')
    assert True

def test_warning():
    logger.warning("TEST warning")
    assert True

def test_info():
    logger.info('TEST info')
    assert True

def test_debug():
    logger.debug('TEST debug')
    assert True
