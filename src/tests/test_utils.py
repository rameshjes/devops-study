import pytest

from utilities.utils import add, remove_spaces, return_string


@pytest.mark.parametrize('x, y, result', [(18, 10, 28), (12, 88, 100),
                                          (0.5, 1.4, 1.9)])
def test_add(x, y, result):
    assert add(x, y) == result


@pytest.mark.parametrize('data, result', [('he ', 'he'), ('h   ello', 'hello'),
                                          (' ', '')])
def test_remove_spaces(data, result):
    assert (remove_spaces(data)) == result


@pytest.mark.parametrize('data, result', [('hello', 'hello'), ('lok', 'lok'),
                                          ('ch ck', 'ch ck')])
def test_return_string(data, result):
    assert (str(data)) == result
