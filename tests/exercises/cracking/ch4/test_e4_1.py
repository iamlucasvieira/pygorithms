from pygorithms.exercises.cracking.ch4.e1 import is_connected
from pygorithms.utils.graph import Graph


def test_is_connected():
    graph = Graph()
    graph.add_edges(
        ("A", "B"),
        ("B", "C"),
        ("C", "D"),
        ("B", "E"),
        ("E", "F"),
        ("A", "G"),
        ("G", "H"),
    )

    assert not is_connected(graph, "A", "1")
    assert not is_connected(graph, "1", "A")
    assert is_connected(graph, "A", "D")
    assert not is_connected(graph, "D", "A")
    assert is_connected(graph, "B", "F")
    assert not is_connected(graph, "B", "G")
