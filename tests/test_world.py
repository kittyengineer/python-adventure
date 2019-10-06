from python_adventure.world import *

def test_world_init_basic():
    world = World()
    world.max_x == 0
    world.max_y == 0
    len(world.locations) == 1

def test_world_is_inbounds_true():
    world = World(3, 3)
    assert world.is_in_bounds(0, 0) == True
    assert world.is_in_bounds(2, 2) == True

def test_world_is_inbounds_false():
    world = World(3, 3)
    assert world.is_in_bounds(-1, 0) == False
    assert world.is_in_bounds(0, -1) == False
    assert world.is_in_bounds(0, 3) == False
    assert world.is_in_bounds(3, 0) == False

def test_location_init_basic():
    location = Location(x_coord=1, y_coord=1, description="[1][1]")
    assert location.x_coord == 1
    assert location.y_coord == 1
    assert location.description == "[1][1]"

def test_location_north():
    location = Location(x_coord=1, y_coord=1)
    location.north()
    assert location.x_coord == 1
    assert location.y_coord == 2

def test_location_east():
    location = Location(x_coord=1, y_coord=1)
    location.east()
    assert location.x_coord == 2
    assert location.y_coord == 1

def test_location_south():
    location = Location(x_coord=1, y_coord=1)
    location.south()
    assert location.x_coord == 1
    assert location.y_coord == 0

def test_location_west():
    location = Location(x_coord=1, y_coord=1)
    location.west()
    assert location.x_coord == 0
    assert location.y_coord == 1

