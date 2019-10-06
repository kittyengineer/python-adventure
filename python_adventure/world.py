# Definitions for world's Grid and Location classes

class World:
    '''Basic square grid layout for a world map'''
    def __init__(self, max_x=1, max_y=1): # , current=(0, 0)):
        self.max_x = max_x
        self.max_y = max_y
        self.locations = [[Location() for x in range(max_x)] for y in range(max_y)]
        for x in range(max_x):
            for y in range(max_y):
                self.locations[x][y].x_coord = x
                self.locations[x][y].y_coord = y

    def is_in_bounds(self, x_coord, y_coord):
        if x_coord in range(self.max_x) and y_coord in range(self.max_y):
            return True
        return False

# TODO
# OK - Location.description can remain a string    
# Location.creature requires a new class
# Location.items requires a new class

class Location:
    '''Each individual square on the grid is a Location'''
    def __init__(self, x_coord=-1, y_coord=-1, description="", creature="", items=""):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.description = description
        self.creature = creature
        self.items = items

    def __repr__(self):
        return f'Location[{self.x_coord}][{self.y_coord}]'

    def north(self):
        self.y_coord += 1

    def east(self):
        self.x_coord += 1

    def south(self):
        self.y_coord -= 1

    def west(self):
        self.x_coord -= 1
