"""Implementation of Hash Table using Chaining for Collision Resolution."""

from dataclasses import dataclass
from typing import Generic, Self, TypeVar

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    key: str
    value: T
    next: Self | None


class InvalidCapacityError(Exception):
    """Exception raised when the capacity of the hash table is invalid."""

    def __init__(self, message: str = "Capacity must be a positive integer."):
        super().__init__(message)


class HashTableChaining(Generic[T]):
    """Hash Table using Chaining for Collision Resolution.

    Attributes:
        capacity (int): The size of the hash table.
        table (list[Node | None]): The list of linked lists for chaining.
    """

    def __init__(self, capacity: int = 10):
        """Initialize the hash table with a given capacity.

        Args:
            capacity (int): The initial size of the hash table.

        Raises:
            InvalidCapacityError: If the capacity is not a positive integer.
        """
        if capacity <= 0:
            raise InvalidCapacityError()
        self.capacity = capacity
        self.table: list[Node | None] = [None] * capacity

    def _hash(self, key: str) -> int:
        """Compute the hash value for a given key."""
        return hash(key) % self.capacity

    def insert(self, key: str, value: T) -> None:
        """Insert a key-value pair into the hash table.

        Args:
            key (str): The key to insert.
            value (T): The value associated with the key.
        """
        index = self._hash(key)
        node = Node(key, value, None)

        node_at_index = self.table[index]
        if node_at_index is None:
            self.table[index] = node
        else:
            current_node = node_at_index
            while current_node is not None:
                if current_node.key == key:
                    current_node.value = value
                    return
                elif current_node.next is None:
                    current_node.next = node
                    return
                current_node = current_node.next

    def search(self, key: str) -> T:
        index = self._hash(key)
        current_node = self.table[index]
        while current_node is not None:
            if current_node.key == key:
                return current_node.value
            else:
                current_node = current_node.next
        raise KeyError()
