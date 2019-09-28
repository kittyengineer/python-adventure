import python_adventure.adventure as adventure
import pytest
from unittest.mock import patch
import os
from os import name as os_name

@patch('os.system')
def test_clear_screen_posix_support(mocked_os_system):
    os.name = 'posix'
    adventure.clear_screen()
    os.system.assert_called_once_with('clear')

@pytest.mark.skip(reason='problem executing this test under linux environment')
@patch('os.system')
def test_clear_screen_nt_support(mocked_os_system):
    os.name = 'nt'
    adventure.clear_screen()
    os.system.assert_called_once_with('cls')

def test_get_direction_north(mocker):
    mocker.patch('builtins.input', side_effect=['n'])
    assert adventure.get_direction() == 'n'

def test_get_direction_invalid(mocker, capsys):
    mocker.patch('builtins.input', side_effect=['z', 'n'])
    adventure.get_direction()
    captured = capsys.readouterr()
    assert 'try again' in captured.out
