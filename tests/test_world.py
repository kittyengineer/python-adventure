from python_adventure.world import *

def test_grid_init_basic():
    g = Grid()
    g.max_x == 0
    g.max_y == 0
    g.current == (0, 0)
    len(g.locations) == 1