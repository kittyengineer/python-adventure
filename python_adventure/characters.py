'''A module that hosts the main Hero class
Note - Consider if this should go into the world.py module instead
'''
# The random module provides methods for randomizing game results (e.g. character damage)
from random import randint
from python_adventure.world import Location

HP_MIN = 5
HP_MAX = 20
MP_MIN = 5
MP_MAX = 20

class Hero:
    '''Basic character class for the pyadventure game'''
    def __init__(self, name, hit_points=randint(HP_MIN, HP_MAX), \
      magic_points=randint(MP_MIN, MP_MAX), location=Location()):
        self.name = name
        self.hit_points = hit_points
        self.magic_points = magic_points
        self.weapons = []
        self.armour = []
        self.gear = []
        self.location = location

    def __str__(self):
        return f'name={self.name} hp={self.hit_points} ' \
             f'mp={self.magic_points}'

    def add_weapon(self, weapon):
        '''Add a weapon to the hero's inventory. Currently only one weapon
        supported and it has no attributes. Consider a better design in future
        iterations.'''
        self.weapons.append(weapon)

    def add_armour(self, armour):
        '''Add armour to the hero's inventory. Similar shortcomings to weapon'''
        self.armour.append(armour)
