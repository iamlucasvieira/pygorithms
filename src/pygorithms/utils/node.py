from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    value: T
    next: Node | None = None


class LinkedArray(Generic[T]):
    def __init__(self):
        self.head: Node[T] | None = None

    def insert(self, value: T):
        node = Node(value=value)
        if self.head is None:
            self.head = node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = node
