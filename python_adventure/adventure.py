# The time module allows us to pause and stop the game
from time import *
# The random module provides methods for randomizing game results (e.g. character damage)
from random import *
# For calls to the operating system
import os, sys
# ASCII art assets
import python_adventure.ascii_assets as assets


def main():
    clear_screen()
    print(assets.title)
    print(assets.splash)


def clear_screen():
    '''Simple function that clears the screen. '''
    os.system('cls' if os.name=='nt' else 'clear')


if __name__ == '__main__':
    main()

