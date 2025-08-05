"""Graph utils."""

from __future__ import annotations

from collections import defaultdict
from typing import Generic, TypeVar

T = TypeVar("T")


class Graph(Generic[T]):
    """Graph implementation"""

    def __init__(self) -> None:
        """Create an empty graph"""
        self._adj: dict[T, set[T]] = defaultdict(set)
        self._vertices: set[T] = set()

    def add_vertex(self, vertex: T) -> None:
        """Add a vertex to the graph"""
        self._vertices.add(vertex)

    def add_edge(self, from_vertex: T, to_vertex: T) -> None:
        """Add a directed edge from_vertex -> to_vertex"""
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        self._adj[from_vertex].add(to_vertex)

    def add_edges(self, *edges: tuple[T, T]) -> None:
        """Add multiple edges at once: graph.add_edges(("A","B"), ("B","C"))"""
        for from_v, to_v in edges:
            self.add_edge(from_v, to_v)

    def has_vertex(self, vertex: T) -> bool:
        """Check if vertex exists"""
        return vertex in self._vertices

    def has_edge(self, from_vertex: T, to_vertex: T) -> bool:
        """Check if edge exists"""
        return to_vertex in self._adj.get(from_vertex, set())

    def neighbors(self, vertex: T) -> set[T]:
        """Get all neighbors of a vertex"""
        return self._adj.get(vertex, set()).copy()

    def vertices(self) -> set[T]:
        """Get all vertices"""
        return self._vertices.copy()
