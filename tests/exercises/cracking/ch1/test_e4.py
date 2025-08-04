import pytest

from pygorithms.exercises.cracking.ch1.e4 import is_palindrome_permutation


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("ana", True),
        ("abcabc", True),
        ("abccba", True),
        ("aaa", True),
        ("aaaa", True),
        ("as", False),
        ("qwe", False),
    ],
)
def test_is_palindrome_permutation(s, expected):
    assert is_palindrome_permutation(s) == expected
