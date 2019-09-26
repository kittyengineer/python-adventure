# The random module provides methods for randomizing game results (e.g. character damage)
from random import randint

HP_MIN = 5
HP_MAX = 20
MP_MIN = 5
MP_MAX = 20

class Adventurer:
    '''Basic character class for the pyadventure game'''
    def __init__(self, name, hit_points=randint(HP_MIN, HP_MAX), \
      magic_points=randint(MP_MIN, MP_MAX)):
        self.name = name
        self.hit_points = hit_points
        self.magic_points = magic_points

    def __str__(self):
        return f'name={self.name} hp={self.hit_points} ' \
             f'mp={self.magic_points}'