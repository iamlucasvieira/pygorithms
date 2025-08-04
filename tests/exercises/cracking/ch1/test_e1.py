import pytest

from pygorithms.exercises.cracking.ch1.e1 import is_all_unique


@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("abcde", True),
        ("aabbcc", False),
        ("", True),
        ("1234567890", True),
        ("!@#$%^&*()", True),
        ("AaBbCc", True),
    ],
)
def test_is_all_unique(input_str, expected):
    assert is_all_unique(input_str) == expected
