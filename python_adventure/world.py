'''Definitions for World and Location classes'''

class World:
    '''Basic square grid layout for a world map'''
    def __init__(self, max_x=1, max_y=1): # , current=(0, 0)):
        self.max_x = max_x
        self.max_y = max_y
        self.locations = [[Location() for x in range(max_x)] for y in range(max_y)]
        for x_coord in range(max_x):
            for y_coord in range(max_y):
                self.locations[x_coord][y_coord].x_coord = x_coord
                self.locations[x_coord][y_coord].y_coord = y_coord

    def is_in_bounds(self, x_coord, y_coord):
        '''Check that coordinates references are in the world bounds'''
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
        '''Move location coordinates to the north'''
        self.y_coord += 1

    def east(self):
        '''Move location coordinates to the east'''
        self.x_coord += 1

    def south(self):
        '''Move location coordinates to the south'''
        self.y_coord -= 1

    def west(self):
        '''Move location coordinates to the west'''
        self.x_coord -= 1
