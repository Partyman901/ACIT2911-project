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


def test_return_one(database, number='16660308 3129'):
    """ testing that it returns an Employee """
    check = database.return_one(number)
    assert type(check) == Employee


def test_error_return_one(database, number='1'):
    """ testing for error when it returns None """
    check = database.return_one(number)
    assert check == None


def test_add_employee(database):
    """ testing for return in adding of employee """
    first_name = "raymond"
    last_name = "lee"
    id = "15242144 8512"
    phone_number = "7785412365"
    last_login = "2020-05-18 14:55:59"
    position = "manager"
    check = database.add_employee(first_name, last_name, id, phone_number, last_login, position)
    assert check == True


def test_remove_employee(database):
    """ testing for delete employee """
    id = "15242144 8512"
    check = database.remove_employee(id)
    assert check == True


def test_update_employee(database):
    """ testing for update employee """
    first_name = "Price"
    last_name = "Crawford"
    id = "16681023 1743"
    phone_num = "1-565-139-5739"
    last_login = "2018-12-15 13:15:32"
    position = "Human Resources"
    check = database.update_employee(first_name, last_name, id, phone_num, last_login, position)
    assert check == True