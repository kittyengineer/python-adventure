import python_adventure.adventure as adventure
import python_adventure.characters as chars
from python_adventure.world import Location
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

def test_hero_init(mocker):
    mocker.patch('builtins.input', side_effect=['Conan'])
    hero = adventure.hero_init(Location())
    assert hero.name == 'Conan'

def test_get_direction_invalid(mocker, capsys):
    mocker.patch('builtins.input', side_effect=['z', 'n'])
    adventure.get_direction()
    captured = capsys.readouterr()
    assert 'try again' in captured.out

def test_intro_typical(mocker):
    mocker.patch('builtins.input', side_effect=['y', 'y'])
    mocker.patch('time.sleep')  # no need to sleep when testing
    hero = chars.Hero('Butch')
    adventure.intro(hero)
    assert 'sword' in hero.weapons
    assert 'shield' in hero.armour

def test_intro_joke(mocker):
    mocker.patch('builtins.input', side_effect=['y', 'n'])
    mocker.patch('time.sleep')  # no need to sleep when testing
    hero = chars.Hero('Pepto')
    adventure.intro(hero)
    assert len(hero.weapons) == 0
    assert len(hero.armour) == 0

def test_world_init():
    world = adventure.world_init()
    world.max_x = 3
    world.max_y = 2
    # bottom row
    for x in range(world.max_x):
        assert world.locations[x][0].x_coord == x
        assert world.locations[x][0].y_coord == 0
        assert repr(world.locations[x][0]) == f'Location[{x}][0]'
    # middle row
    for x in range(world.max_x):
        assert world.locations[x][0].x_coord == x
        assert world.locations[x][1].y_coord == 1
        assert repr(world.locations[x][1]) == f'Location[{x}][1]'
    # top row
    for x in range(world.max_x):
        assert world.locations[x][0].x_coord == x
        assert world.locations[x][2].y_coord == 2
        assert repr(world.locations[x][2]) == f'Location[{x}][2]'