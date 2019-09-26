import python_adventure.characters as chars

def test_init_adventurer_random_stats():
    mychar = chars.Adventurer(name='Kitty')
    assert mychar.name == 'Kitty'
    assert mychar.hit_points >= chars.HP_MIN and  \
        mychar.hit_points <= chars.HP_MAX
    assert mychar.magic_points >= chars.MP_MIN and \
        mychar.magic_points <= chars.MP_MAX

def test_init_adventurer_fixed_stats():
    mychar = chars.Adventurer('Mutt', hit_points=10, magic_points=10)
    assert mychar.name == 'Mutt'
    assert mychar.hit_points == 10
    assert mychar.magic_points == 10

def test_adventurer_str():
    mychar = chars.Adventurer('Patch', 15, 15)
    str(mychar) == 'name=Patch hp=15 mp=15'
