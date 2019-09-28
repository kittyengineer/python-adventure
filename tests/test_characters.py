import python_adventure.characters as chars

def test_init_adventurer_random_stats():
    adventurer = chars.Adventurer(name='Kitty')
    assert adventurer.name == 'Kitty'
    assert adventurer.hit_points >= chars.HP_MIN and  \
        adventurer.hit_points <= chars.HP_MAX
    assert adventurer.magic_points >= chars.MP_MIN and \
        adventurer.magic_points <= chars.MP_MAX

def test_init_adventurer_fixed_stats():
    adventurer = chars.Adventurer('Mutt', hit_points=10, magic_points=10)
    assert adventurer.name == 'Mutt'
    assert adventurer.hit_points == 10
    assert adventurer.magic_points == 10

def test_adventurer_str():
    adventurer = chars.Adventurer('Patch', 15, 15)
    assert str(adventurer) == 'name=Patch hp=15 mp=15'

def test_adventurer_move():
    adventurer = chars.Adventurer('Mover')
    for my_move in ('n', 'e', 'w', 's'):
        adventurer.move = my_move
        assert adventurer.move == my_move
    