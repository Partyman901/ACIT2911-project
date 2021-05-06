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
