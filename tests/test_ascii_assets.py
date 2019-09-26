import python_adventure.ascii_assets as assets

def _assert_unempty_string(string):
    assert isinstance(string, str)
    assert len(string) > 0


def test_title_available():
    _assert_unempty_string(assets.TITLE)


def test_splash_available():
    _assert_unempty_string(assets.SPLASH)
