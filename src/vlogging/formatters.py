from logging import Formatter
from logging import LogRecord
from datetime import datetime

class VFormatter(Formatter):

    def formatTime(self, record: LogRecord, datefmt: str=None) -> str:
        """
        Return the creation time of the specified LogRecord as formatted text.

        Parameters
        ----------
        record : LogRecord
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
            time = dt.isoformat(sep=' ', timespec='milliseconds')
        else:
            time = dt.strftime(datefmt)
        return time
