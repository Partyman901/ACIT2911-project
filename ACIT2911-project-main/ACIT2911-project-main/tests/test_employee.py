import pytest
from models import Employee

@pytest.fixture
def bob():
    return Employee('Bob', 'Smith', '12345678 9123', '604-123-4567', '2019-09-21', 'HR')


def test_attributes(bob):
    assert bob.first_name == 'Bob'
    assert bob.last_name == 'Smith'
    assert bob.id == '12345678 9123'
    assert bob.phone_num == '604-123-4567'
    assert bob.last_login == '2019-09-21'
    assert bob.position == 'HR'


def test_str(bob):
    assert str(bob) == ' Bob          | Smith        | 12345678 9123    | 604-123-4567     | 2019-09-21             | HR                  '