import python_adventure.ascii_assets as assets

def test_title_available():
    assert isinstance(assets.title, str)
    assert len(assets.title) > 0


def test_splash_available():
    assert isinstance(assets.splash, str)
    assert len(assets.splash) > 0
