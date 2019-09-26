# The time module allows us to pause and stop the game
# from time import *
# For calls to the operating system
import os
# import sys
# ASCII art assets
import python_adventure.ascii_assets as assets
import python_adventure.characters as characters


def main():
    clear_screen()
    print(assets.TITLE)
    print(assets.SPLASH)
    name = input("What is your name adventurer? ")
    adventurer = characters.Adventurer(name)
    print(adventurer)


def clear_screen():
    '''Simple function that clears the screen. '''
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    main()
