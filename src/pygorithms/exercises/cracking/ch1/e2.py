"""Permutation of two strings
Options

1) Check all chars in s1 if in s2 and keep track of index for repeated O(n^2)
2) Sort both strings and compare them O(nlogn)
3) Create a hashmap of each string then check if the maps are equal O(n)
"""


def is_permutation(s1: str, s2: str):
    return get_char_frequency(s1) == get_char_frequency(s2)


def get_char_frequency(s: str) -> dict[str, int]:
    """Returns a hashmap with char as key and frequency as value."""
    char_frequency = {}
    for char in s:
        if char not in char_frequency:
            char_frequency[char] = 0
        else:
            char_frequency[char] += 1
    return char_frequency
