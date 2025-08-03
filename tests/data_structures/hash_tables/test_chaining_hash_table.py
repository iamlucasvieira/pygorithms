"""Tests for the chaining hash table."""

import pytest
from hypothesis import given
from hypothesis import strategies as st

from pygorithms.data_structures.hash_tables import HashTableChaining
from pygorithms.data_structures.hash_tables.chaining_hash_table import InvalidCapacityError, Node


class TestHashTableChaining:
    """Test class for HashTableChaining."""

    def test_init(self) -> None:
        """Test if the hash table initializes correctly."""
        table = HashTableChaining(10)
        assert table.capacity == 10
        assert len(table.table) == 10
        assert all(node is None for node in table.table)

    @pytest.mark.parametrize("capacity", [-1, 0])
    def test_init_invalid_capacity(self, capacity: int) -> None:
        """Test if the hash table raises an error for invalid capacity."""
        with pytest.raises(InvalidCapacityError):
            HashTableChaining(capacity)

    @given(st.integers(min_value=1, max_value=1_000), st.text())
    def test_hash(self, capacity: int, key: str) -> None:
        """Test if insert works."""
        table = HashTableChaining(capacity)
        assert 0 <= table._hash(key) < capacity

    def test_insert(self) -> None:
        """Test if value is inserted in the correct index."""
        table = HashTableChaining(10)
        key = "test_key"
        value = "test_value"
        table.insert(key, value)

        index = table._hash(key)
        node = table.table[index]
        assert node is not None
        assert node.key == key
        assert node.value == value

    def test_insert_same_key(self) -> None:
        """Test if inserting the same key updates the value."""
        table = HashTableChaining(10)
        key = "test_key"
        value1 = "test_value1"
        value2 = "test_value2"
        table.insert(key, value1)
        table.insert(key, value2)

        index = table._hash(key)
        node = table.table[index]
        assert node is not None
        assert node.key == key
        assert node.value == value2

    def test_insert_collision(self) -> None:
        """Adding more items than capacity will lead to collision."""
        values_inserted = 20
        table = HashTableChaining(1)
        for i in range(values_inserted):
            table.insert(str(i), i)

        counter = 0
        current_node = table.table[0]
        while current_node is not None:
            counter += 1
            current_node = current_node.next
        assert counter == values_inserted

    def test_insert_same_key_with_collision(self) -> None:
        """Test inserting the same key when there are collisions."""
        table = HashTableChaining(1)
        table.insert("1", "2")
        table.insert("2", "2")
        table.insert("2", "NEW")

        current_node = table.table[0]
        assert current_node is not None
        while current_node.next is not None:
            current_node = current_node.next
        assert current_node.value == "NEW"

    def test_search(self) -> None:
        """Test if searching for a key returns the correct value."""
        table = HashTableChaining(10)
        key = "test_key"
        value = "test_value"
        table.insert(key, value)
        assert table.search(key) == value

    def test_search_with_collision(self) -> None:
        """Test searching for a key when there are collisions."""
        table = HashTableChaining(1)
        for i in range(10):
            table.insert(str(i), i)

        assert table.search("5") == 5

    def test_search_key_error(self) -> None:
        """Test searching for a non-existent key raises KeyError."""
        table = HashTableChaining(10)
        with pytest.raises(KeyError):
            table.search("non_existent_key")


class TestNode:
    """Test class for Node."""

    def test_node_creation(self) -> None:
        """Test if a Node is created correctly."""
        node = Node("test_key", "test_value", None)
        assert node.key == "test_key"
        assert node.value == "test_value"
        assert node.next is None

    def test_node_next(self) -> None:
        """Test if the next pointer in Node works correctly."""
        next_node = Node("next_key", "next_value", None)
        node = Node("test_key", "test_value", next_node)
        assert node.next is next_node
