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


def get_direction(direction_options=
    {'n': '(n)orth', 's': '(s)outh', 'e': '(e)ast', 'w': '(w)est'}):
    '''Ask player for direction they want to proceed towards'''
    direction = None
    while True:
        direction = input( f'Would you like to go {", ".join(direction_options.values())}> ')
        if direction in direction_options.keys():
            return direction
        else:
            print("Ohh that's not a valid option, please try again ...")
    

if __name__ == '__main__':

    main()