import pytest
from mixins.logger import logger
from datetime import datetime

@pytest.fixture
def loggere():
    return logger()

def test_log(loggere):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    loggere.log('Hello world')
    assert loggere.logs.get(f'{loggere.nums-1} {date}', 0)
