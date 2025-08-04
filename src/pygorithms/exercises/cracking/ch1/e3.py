"""URLify

Assumptions:
- If %20 is part of the string and there is an space after it is okay to kee both %20
- Multi space possible

Options:
1. Find every space, split there, then join with %20. O(n)
"""


def urlify(s: str, true_length: int) -> str:
    """Returns an URLfied version of the string s."""
    s_list = list(s)

    index = len(s)
    for i in range(true_length - 1, -1, -1):
        if s[i] == " ":
            s_list[index - 1] = "0"
            s_list[index - 2] = "2"
            s_list[index - 3] = "%"
            index -= 3
        else:
            s_list[index - 1] = s_list[i]
            index -= 1

    return "".join(s_list)
