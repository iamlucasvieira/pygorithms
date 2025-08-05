from pygorithms.exercises.cracking.ch2.e1 import remove_duplicates
from pygorithms.utils.array import LinkedArray


def test_remove_duplicates():
    array = LinkedArray()
    array.insert(1)
    array.insert(2)
    array.insert(3)
    array.insert(1)
    array.insert(2)
    array.insert(4)

    new_array = remove_duplicates(array)
    assert new_array.to_list() == [1, 2, 3, 4]
