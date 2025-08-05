"""Find if there is a link between two nodes in a graph.


1) DFS O(V + E)
2) BFS O(V + E)

We only care if connected so DFS is simpler to implement.
"""

from typing import TypeVar

from pygorithms.utils.graph import Graph

T = TypeVar("T")


def is_connected(graph: Graph[T], from_vertex: T, to_vertex: T) -> bool:
    if not graph.has_vertex(from_vertex) or not graph.has_vertex(to_vertex):
        return False

    if from_vertex == to_vertex:
        return True

    stack = [from_vertex]
    visited = set()

    while stack:
        current = stack.pop()

        if current == to_vertex:
            return True

        if current not in visited:
            visited.add(current)
            for neighbor in graph.neighbors(current):
                print(neighbor)
                if neighbor not in visited:
                    stack.append(neighbor)

    return False
