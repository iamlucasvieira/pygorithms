def is_palindrome_permutation(s: str) -> bool:
    frequency_counter: dict[str, int] = {}

    for char in s:
        if char not in frequency_counter:
            frequency_counter[char] = 0
        frequency_counter[char] += 1

    odd_frequency_counter = 0

    for frequency in frequency_counter.values():
        if frequency % 2 != 0:
            odd_frequency_counter += 1

        if odd_frequency_counter > 1:
            return False
    return True
