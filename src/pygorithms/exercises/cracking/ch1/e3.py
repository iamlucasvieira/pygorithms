"""URLify

Assumptions:
- If %20 is part of the string and there is an space after it is okay to kee both %20
- Multi space possible

Options:
1. Find every space, split there, then join with %20. O(n)
"""

from collections.abc import Iterable


def urlify(s: Iterable) -> str:
    """Returns an URLfied version of the string s."""

    for char in s:
        return char
    return ""


def trim(s: str) -> str:
    start_index = get_first_non_empty_index(s)
    end_index = get_first_non_empty_index(reversed(s))
    return s[start_index:end_index]


def get_first_non_empty_index(s: Iterable) -> int:
    for idx, char in enumerate(s):
        if char != " ":
            return idx
    raise ValueError()
