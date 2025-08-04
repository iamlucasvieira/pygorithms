import pytest

from pygorithms.exercises.cracking.ch1.e2 import is_permutation


@pytest.mark.parametrize(
    ("s1", "s2", "expected"),
    [
        ("", "", True),
        ("abc", "cba", True),
        ("abc", "cbc", False),
        ("aab", "baa", True),
        ("1a#", "#1a", True),
        ("good ", "good", False),
    ],
)
def test_is_permutation(s1, s2, expected):
    assert is_permutation(s1, s2) == expected
