import pytest

from pygorithms.exercises.cracking.ch1.e3 import urlify


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("Test", "Test"),
        ("Test Test", "Test%20Test"),
        ("Test    Test", "Test%20Test"),
        ("  a  b  c  ", "a%20b%20c"),
    ],
)
def test_urlify(s, expected):
    assert urlify(s) == expected
