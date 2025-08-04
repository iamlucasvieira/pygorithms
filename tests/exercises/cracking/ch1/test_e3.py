import pytest

from pygorithms.exercises.cracking.ch1.e3 import urlify


@pytest.mark.parametrize(
    ("s", "true_length", "expected"),
    [
        ("Test", 4, "Test"),
        ("Test Test  ", 9, "Test%20Test"),
        ("Mr John Smith    ", 13, "Mr%20John%20Smith"),
    ],
)
def test_urlify(s, true_length, expected):
    assert urlify(s, true_length) == expected
