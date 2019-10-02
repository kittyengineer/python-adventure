# Definitions for world's Grid and Location classes
#import Location from python_adventure.world

class Grid:
    '''Basic square grid layout for a world map'''
    def __init__(self, max_x=1, max_y=1, current=(0, 0)):
        self.max_x = max_x
        self.max_y = max_y
        self.current = current
        self.locations = [[Location() for i in range(max_x)] for j in range(max_y)]

# TODO
# OK - Location.description can remain a string    
# Location.creature requires a new class
# Location.items requires a new class

class Location:
    '''Each individual square on the grid is a Location'''
    def __init__(self, description="", creature="", items=""):
        self.description = description
        self.creature = creature
        self.items = items
    

