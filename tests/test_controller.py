import pytest
import mock
import builtins
from controllers import AppController



@pytest.fixture
def controller():
    return AppController()


def test_running(controller):
    with mock.patch.object(builtins, 'input', side_effect= [5]):
        check = controller.run()
        assert check == False


def test_option_1(controller):
    with mock.patch.object(builtins, 'input', side_effect= [1, "", 5]):
        check = controller.run()
        assert check == False


def test_option_2(controller):
    with mock.patch.object(builtins, 'input', side_effect=[2, "", 5]):
        check = controller.run()
        assert check == False
        
def test_option_2_valid(controller):
    with mock.patch.object(builtins, 'input', side_effect=[2, "16660308 3129", 5, 5]):
        check = controller.run()
        assert check == False


def test_option_3_True(controller):
    with mock.patch.object(builtins, 'input', side_effect=[3, "mo","mohseni", "15151512 2020","778452112", "specialist", 5]):
        check = controller.run()
        assert check == False

def test_option_3(controller):
    with mock.patch.object(builtins, 'input', side_effect=[3, "mo","mohseni", "15151512 2020", 5, 5]):
        check = controller.run()
        assert check == False

def test_option_4(controller):
    with mock.patch.object(builtins, "input", side_effect=[4, "15151512 2020", "Y", 5]):
        check = controller.run()
        assert check == False

def test_option_4_ID_does_not_exist(controller):
    with mock.patch.object(builtins, "input", side_effect=[4, "abcd", "Y", 5]):
        check = controller.run()
        assert check == False

def test_invalid_option_controller(controller):
    with mock.patch.object(builtins, "input", side_effect=["a", 5]):
        check = controller.run()
        assert check == False

def test_invalid_option_controller_integer(controller):
    with mock.patch.object(builtins, "input", side_effect=[10, 5]):
        check = controller.run()
        assert check == False

def test_option_4_no(controller):
    with mock.patch.object(builtins, "input", side_effect=[4, "16380323 8298", "N", 5]):
        check = controller.run()
        assert check == False

def test_4_invalid(controller):
    with mock.patch.object(builtins, "input", side_effect=[4, "16380323 8298", "A", "N", 5]):
        check = controller.run()
        assert check == False