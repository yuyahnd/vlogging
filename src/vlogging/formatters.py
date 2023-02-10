import logging
from datetime import datetime

SIMPLE_FORMAT = "%(asctime)s %(levelname)-8s %(message)s"
BASIC_FORMAT = "%(asctime)s %(levelname)-8s %(filename)s:%(lineno)d: %(message)s"
DATE_FMT_MICROSECONDS = "%Y-%m-%d %H:%M:%S.%f"

def getFormatConfig(format: str,
                datefmt: str = None,
                className: str = "vlogging.formatters.Formatter") -> dict:
    config = {
        "class": className,
        "format": format,
    }
    if datefmt is not None:
        config["datefmt"] = datefmt
    return config

class Formatter(logging.Formatter):
    """
    Formatter instances are used to convert a LogRecord to text.

    %(name)s            Name of the logger (logging channel)
    %(levelno)s         Numeric logging level for the message (DEBUG, INFO,
                        WARNING, ERROR, CRITICAL)
    %(levelname)s       Text logging level for the message ("DEBUG", "INFO",
                        "WARNING", "ERROR", "CRITICAL")
    %(pathname)s        Full pathname of the source file where the logging
                        call was issued (if available)
    %(filename)s        Filename portion of pathname
    %(module)s          Module (name portion of filename)
    %(lineno)d          Source line number where the logging call was issued
                        (if available)
    %(funcName)s        Function name
    %(created)f         Time when the LogRecord was created (time.time()
                        return value)
    %(asctime)s         Textual time when the LogRecord was created
    %(msecs)d           Millisecond portion of the creation time
    %(relativeCreated)d Time in milliseconds when the LogRecord was created,
                        relative to the time the logging module was loaded
                        (typically at application startup time)
    %(thread)d          Thread ID (if available)
    %(threadName)s      Thread name (if available)
    %(process)d         Process ID (if available)
    %(processName)s     Process name (if available)
    %(message)s         The result of record.getMessage(), computed just as
                        the record is emitted
    """


    def getFormatDict(self, format: str, datefmt: str=None) -> dict:
        format = {
            "class": "vlogging.Formatter",
            "format": format,
        }
        if datefmt is not None:
            format["datefmt"] = datefmt
        return format

    def getDefautFormatDict(self) -> dict:
        return self.getFormatDict(Formatter.SIMPLE_FORMAT)

    def getConsoleFormatDict(self) -> dict:
        return self.getFormatDict(Formatter.BASIC_FORMAT, Formatter.DATE_FMT_MICROSECONDS)

    def formatTime(self, record: logging.LogRecord, datefmt: str=None) -> str:
        """
        Return the creation time of the specified LogRecord as formatted text.

        Parameters
        ----------
        record : logging.LogRecord
            log record
        datefmt : str, optional
            datetime format, by default None

        Returns
        -------
        str
            formatted text
        """
        dt = datetime.fromtimestamp(record.created)
        if datefmt is None:
            time = dt.isoformat(sep=" ", timespec="milliseconds")
        else:
            time = dt.strftime(datefmt)
        return time
