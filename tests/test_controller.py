import pytest
import mock
import builtins
from controllers import AppController



@pytest.fixture
def controller():
    return AppController()


def test_running(controller):
    with mock.patch.object(builtins, 'input', side_effect= [4]):
        check = controller.run()
        assert check == False


def test_option_1(controller):
    with mock.patch.object(builtins, 'input', side_effect= [1, "", 4]):
        check = controller.run()
        assert check == False


def test_option_2(controller):
    with mock.patch.object(builtins, 'input', side_effect=[2, "", 4]):
        check = controller.run()
        assert check == False
        
def test_option_2_valid(controller):
    with mock.patch.object(builtins, 'input', side_effect=[2, "16291118 1812", 4, 4]):
        check = controller.run()
        assert check == False

def test_option_3(controller):
    with mock.patch.object(builtins, 'input', side_effect=[3, "mo","mohseni", "15151512 2020", 4]):
        check = controller.run()
        assert check == False

def test_option_3_True(controller):
    with mock.patch.object(builtins, 'input', side_effect=[3, "mo","mohseni", "15151512 2020","778452112", "specialist", 4]):
        check = controller.run()
        assert check == False
