import pytest
from logging import LogRecord
from datetime import datetime

from vlogging import INFO
from vlogging import formatters
from vlogging.formatters import (
    SIMPLE_FORMAT,
    BASIC_FORMAT,
    DATE_FMT_MICROSECONDS,
    Formatter
)


@pytest.mark.parametrize("format, datefmt, style, className", [
    (SIMPLE_FORMAT, DATE_FMT_MICROSECONDS, "%", "vlogging.formatters.Formatter"),
    (SIMPLE_FORMAT, None, "%", "vlogging.formatters.Formatter"),
    (BASIC_FORMAT, DATE_FMT_MICROSECONDS, "%", "vlogging.formatters.Formatter"),
    (BASIC_FORMAT, None, "%", "vlogging.formatters.Formatter"),
    (None, None, None, None),
])
def test_getFormatConfig(format, datefmt, style, className):
    config = formatters.getFormatConfig(format, datefmt, style, className)
    assert config.get("class") == className
    assert config.get("format") == format
    assert config.get("style") == style
    assert config.get("datefmt", None) == datefmt


@pytest.mark.parametrize("format, style", [
    (SIMPLE_FORMAT, "%"),
    (SIMPLE_FORMAT, None),
    (BASIC_FORMAT, "%"),
    (BASIC_FORMAT, None),
    (None, None),
])
def test_getMicrosecondsFormatConfig(format, style):
    config = formatters.getMicrosecondsFormatConfig(format, style)
    assert config.get("format") == format
    assert config.get("style") == style
    assert config.get("datefmt") == DATE_FMT_MICROSECONDS


@pytest.fixture
def logRecord():
    return LogRecord("vlogger", INFO, "path", 1, "Message", "args", exc_info=None)


@pytest.fixture
def formatter():
    return Formatter()


def test_formatTime_isoformat(formatter, logRecord):
    formatTime = formatter.formatTime(logRecord)

    dt = datetime.fromtimestamp(logRecord.created)
    expected = dt.isoformat(sep=" ", timespec="milliseconds")
    print(formatTime, logRecord.created)
    assert formatTime == expected


@pytest.mark.parametrize("datefmt", [
    ("%Y-%m-%d %H:%M:%S.%f"),
    ("%Y-%m-%d"),
    ("%H:%M:%S.%f"),
    ("%Y-%m-%d %H:%M:%S"),
])
def test_formatTime_strftime(formatter, logRecord, datefmt):
    formatTime = formatter.formatTime(logRecord, datefmt)

    dt = datetime.fromtimestamp(logRecord.created)
    expected = dt.strftime(datefmt)
    print(formatTime, logRecord.created)
    assert formatTime == expected
