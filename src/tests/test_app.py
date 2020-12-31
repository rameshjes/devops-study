import pytest

from src.app import find_label
from src.app import get_preprocessed_text

labels = ["negative", "positive"]


@pytest.mark.parametrize(
    "data, result",
    [
        ("Totally loved this movie", "positive"),
        ("Pathetic movie. Would not recommend anyone", "negative"),
        ("Worth watching. Highly recommended", "positive"),
    ],
)
def test_find_label(data, result):

    preprocessed_text = get_preprocessed_text(data)
    predict_label = find_label(preprocessed_text)[0]
    assert (labels[predict_label]) == result
