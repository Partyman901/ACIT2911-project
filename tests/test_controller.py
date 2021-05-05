import pytest
from models import DatabaseManager

@pytest.fixture
def controller():
    return AppController()


