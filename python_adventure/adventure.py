# The time module allows us to pause and stop the game
from time import *
# The random module provides methods for randomizing game results (e.g. character damage)
from random import *
# For calls to the operating system
import os, sys


def main():
    pass


def clear_screen():
    '''Simple function that clears the screen. '''
    os.system('cls' if os.name=='nt' else 'clear')


if __name__ == '__main__':
    main()

