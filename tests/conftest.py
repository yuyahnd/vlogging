import pytest

@pytest.fixture(scope="session")
def log_file(tmpdir_factory) -> str:
    logfile = tmpdir_factory.mktemp("vlogger").join("vlogging.log")
    return str(logfile)
