import numpy as np
import pytest
from numpy.testing import assert_array_equal

from src.utilities.utils import add
from src.utilities.utils import create_array
from src.utilities.utils import remove_punctuations
from src.utilities.utils import remove_spaces
from src.utilities.utils import return_string
from src.utilities.utils import subtract


@pytest.mark.parametrize("x, y, result", [(18, 10, 28), (12, 88, 100), (0.5, 1.4, 1.9)])
def test_add(x, y, result):
    assert add(x, y) == result


@pytest.mark.parametrize("x, y, result", [(18, 10, 8), (12, 88, -76), (1.5, 1.0, 0.5)])
def test_subtract(x, y, result):
    assert subtract(x, y) == result


@pytest.mark.parametrize(
    "data, result", [("he ", "he"), ("h   ello", "hello"), (" ", "")]
)
def test_remove_spaces(data, result):
    assert (remove_spaces(data)) == result


@pytest.mark.parametrize(
    "data, result", [("hello", "hello"), ("lok", "lok"), ("ch ck", "ch ck")]
)
def test_return_string(data, result):
    assert (return_string(data)) == result


@pytest.mark.parametrize(
    "text, output", [("he? wasup", "he wasup"), ("lost...", "lost")]
)
def test_remove_punctuations(text, output):
    assert (remove_punctuations(text)) == output


@pytest.mark.parametrize("data, output", [([1, 2, 3], np.array([1, 2, 3]))])
def test_create_array(data, output):
    assert_array_equal(create_array(data), output)
