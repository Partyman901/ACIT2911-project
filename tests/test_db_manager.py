import pytest
from models import DatabaseManager
from models import Employee

@pytest.fixture
def database():
    """ creating a fixture to test DatabaseManager class """
    return DatabaseManager()


def test_list_all(database):
    """ testing list all function """
    check = database.list_all()
    for emp in check:
        assert type(emp) == Employee


def test_return_one(database, number='16291118 1812'):
    """ testing that it returns an Employee """
    check = database.return_one(number)
    assert type(check) == Employee


def test_error_return_one(database, number='1'):
    """ testing for error when it returns None """
    check = database.return_one(number)
    assert check == None
