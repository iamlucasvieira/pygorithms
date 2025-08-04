from typing import TypeVar

from pygorithms.utils.node import LinkedArray

T = TypeVar("T")


def remove_duplicates(array: LinkedArray[T]) -> LinkedArray[T]:
    seen = set()
    current_node = array.head

    if current_node is None:
        return array

    seen.add(current_node.value)

    while current_node and current_node.next is not None:
        next_node = current_node.next
        if next_node.value in seen:
            current_node.next = next_node.next
        else:
            seen.add(next_node.value)
            current_node = current_node.next

    print(seen)
    return array
