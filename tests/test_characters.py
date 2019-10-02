import python_adventure.characters as chars
from python_adventure.characters import Hero

def test_hero_init_random_stats():
    hero = Hero(name='Kitty')
    assert hero.name == 'Kitty'
    assert hero.hit_points >= chars.HP_MIN and  \
        hero.hit_points <= chars.HP_MAX
    assert hero.magic_points >= chars.MP_MIN and \
        hero.magic_points <= chars.MP_MAX

def test_hero_init_fixed_stats():
    hero = Hero('Mutt', hit_points=10, magic_points=10)
    assert hero.name == 'Mutt'
    assert hero.hit_points == 10
    assert hero.magic_points == 10

def test_hero_str():
    hero = Hero('Patch', 15, 15)
    assert str(hero) == 'name=Patch hp=15 mp=15'

def test_hero_move():
    hero = Hero('Mover')
    for my_move in ('n', 'e', 'w', 's'):
        hero.move = my_move
        assert hero.move == my_move

def test_hero_add_weapon():
    hero = Hero('Battler')
    hero.add_weapon('sword')
    assert 'sword' in hero.weapons

def test_hero_add_armour():
    hero = Hero('Tank')
    hero.add_armour('shield')
    assert 'shield' in hero.armour