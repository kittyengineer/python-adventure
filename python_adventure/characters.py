# The random module provides methods for randomizing game results (e.g. character damage)
from random import randint
from enum import Enum

HP_MIN = 5
HP_MAX = 20
MP_MIN = 5
MP_MAX = 20

class Coord(Enum):
    X = 0
    Y = 1

class Hero:
    '''Basic character class for the pyadventure game'''
    def __init__(self, name, hit_points=randint(HP_MIN, HP_MAX), \
      magic_points=randint(MP_MIN, MP_MAX), location=None):
        self.name = name
        self.hit_points = hit_points
        self.magic_points = magic_points
        self.weapons = []
        self.armour = []
        self.gear = []
        if location is None:
            self.location = [0, 0]
        else:
            self.location = location

    def __str__(self):
        return f'name={self.name} hp={self.hit_points} ' \
             f'mp={self.magic_points}'

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def add_armour(self, armour):
        self.armour.append(armour)

    def north(self):
        self.location[Coord.X.value] += 1

    def east(self):
        self.location[Coord.Y.value] += 1

    def south(self):
        self.location[Coord.X.value] -= 1

    def west(self):
        self.location[Coord.Y.value] -= 1
