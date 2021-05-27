import pytest
import mock
import builtins
from controllers import AppController



@pytest.fixture
def controller():
    """ created a fixture to easily call the method """
    return AppController()


def test_running(controller):
    """ tests that the controller runs """
    with mock.patch.object(builtins, 'input', side_effect= [6]):
        check = controller.run()
        assert check == False


def test_option_1(controller):
    """ test to go through option 1 """
    with mock.patch.object(builtins, 'input', side_effect= [1, "", 6]):
        check = controller.run()
        assert check == False


def test_option_2(controller):
    with mock.patch.object(builtins, 'input', side_effect=[2, "", 6]):
        """ test to go through option 2 """
        check = controller.run()
        assert check == False
        
def test_option_2_valid(controller):
    """ test to go through option 2 and search for a valid ID """
    with mock.patch.object(builtins, 'input', side_effect=[2, "16660308 3129", 6, 6]):
        check = controller.run()
        assert check == False


def test_option_3_True(controller):
    """ test to go through option 3 and add a new entry to the database """
    with mock.patch.object(builtins, 'input', side_effect=[3, "mo","mohseni", "15151512 2020","778452112", "specialist", 6]):
        check = controller.run()
        assert check == False

def test_option_3(controller):
    with mock.patch.object(builtins, 'input', side_effect=[3, "mo","mohseni", "15151512 2020", 6]):
        """ test to go through option 3 and try to add an employee ID that already exists """
        check = controller.run()
        assert check == False

def test_option_4(controller):
    """ test to go through option 4 and sucessfully deletes an existing employee """
    with mock.patch.object(builtins, "input", side_effect=[4, "15151512 2020", "Y", 6]):
        check = controller.run()
        assert check == False

def test_option_4_ID_does_not_exist(controller):
    """ test to go through option 4 and try to delete an employee that doesn't exist """
    with mock.patch.object(builtins, "input", side_effect=[4, "abcd", "Y", 6]):
        check = controller.run()
        assert check == False

def test_invalid_option_controller(controller):
    """ test to go through an invalid letter option in the controller """
    with mock.patch.object(builtins, "input", side_effect=["a", 6]):
        check = controller.run()
        assert check == False

def test_invalid_option_controller_numeric(controller):
    """ test to go through an invalid numeric option in the controller """
    with mock.patch.object(builtins, "input", side_effect=[10, 6]):
        check = controller.run()
        assert check == False

def test_option_4_no(controller):
    """ test to go through option 4 with 'N' to confirmation """
    with mock.patch.object(builtins, "input", side_effect=[4, "16400202 0180", "N", 6]):
        check = controller.run()
        assert check == False

def test_4_invalid(controller):
    """ test to go through option 4 with an invalid entry when asking for confirmation """
    with mock.patch.object(builtins, "input", side_effect=[4, "16380323 8298", "A", "N", 6]):
        check = controller.run()
        assert check == False


def test_option_5_valid(controller):
    """ test to go through option 5 with a valid entry that updates database """
    with mock.patch.object(builtins, "input", side_effect=[5, "16800109 5739", "", "", "", "", "Y", 6]):
        check = controller.run()
        assert check == False


def test_option_5_no(controller):
    """ test to go through option 5 and say N when confirming """
    with mock.patch.object(builtins, "input", side_effect=[5, "16800109 5739", "", "", "", "", "N", 6]):
        check = controller.run()
        assert check == False


def test_option_5_nonexistentID(controller):
    """ test to go through option 5, but with an non-existent ID """
    with mock.patch.object(builtins, "input", side_effect=[5, "123 6790", 6]):
        check = controller.run()
        assert check == False