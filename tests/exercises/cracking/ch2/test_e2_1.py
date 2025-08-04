from typing import TypeVar

from pygorithms.exercises.cracking.ch2.e1 import remove_duplicates
from pygorithms.utils.node import LinkedArray

T = TypeVar("T")


def is_array_equal(array: LinkedArray[T], expected_values: list[T]) -> bool:
    current_node = array.head

    if current_node is None:
        return bool(expected_values)

    while current_node is not None:
        expect = expected_values.pop(0)
        if current_node.value != expect:
            print(current_node, expect)
            return False
        current_node = current_node.next
    return True


def test_remove_duplicates():
    array = LinkedArray()
    array.insert(1)
    array.insert(2)
    array.insert(3)
    array.insert(1)
    array.insert(2)
    array.insert(4)

    new_array = remove_duplicates(array)
    assert is_array_equal(new_array, [1, 2, 3, 4])
