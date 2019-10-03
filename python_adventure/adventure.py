# The time module allows us to pause and stop the game
import time
# For calls to the operating system
import os
import sys

# ASCII art assets
import python_adventure.ascii_assets as assets
# Hero class
from python_adventure.characters import Hero


def main():
    """Here's where the game begins."""
    clear_screen()
    print(assets.TITLE)
    print(assets.SPLASH)
    name = input("What is your name adventurer? ")
    hero = Hero(name)
    intro(hero)
    # TODO - game loop needs a world grid

def clear_screen():
    '''Simple function that clears the screen. '''
    os.system('cls' if os.name == 'nt' else 'clear')


def intro(hero):
    '''Initial introduction to the adventure setting initial hero stats'''
    print(f'Welcome to Meowland, {hero.name}', end='\n\n')
    time.sleep(2)
    print(f'Your health is {hero.hit_points}')
    print(f'Your magic skill is {hero.magic_points}', end='\n\n')
    answer = input("Would you like to venture out into the land? Press y to continue > ")
    if answer == "y":
        print("\nYou are in your home, with a roaring fireplace in front of you," \
          " above the fire you can see your sword and shield")
        answer = input("Would you like to take your sword and shield? Press y to continue > ")
        if answer == "y":
            hero.add_weapon('sword')
            hero.add_armour('shield')
            print(f'\nYou are carrying your {", ".join(hero.weapons)} and {", ".join(hero.armour)}')
            print(f'Armed with these trusty items, you swing open the door to' \
                  ' your home and see a green valley gleaming in the sunshine.')
        else:
            print('You choose not to take your weapons')
            print('Armed with your sense of humour, You swing open the door to see' \
                  ' a green valley full of opportunity awaiting you.')
    else:
        lazy_end()


def lazy_end():
    print("You stay at home, sat in your favourite chair watching the fire grow" \
          " colder. The land of Meowland no longer has a hero.")
    print("Game Over")
    sys.exit(0)


def get_direction(direction_options=None):
    '''Ask player for direction they want to proceed towards'''
    if direction_options is None:
        direction_options = {'n': '(n)orth', 's': '(s)outh',
                             'e': '(e)ast', 'w': '(w)est'}
    while True:
        direction = input(f'Would you like to go {", ".join(direction_options.values())}> ')
        if direction in direction_options.keys():
            return direction
        print("Ohh that's not a valid option, please try again ...")


if __name__ == '__main__':
    main()
