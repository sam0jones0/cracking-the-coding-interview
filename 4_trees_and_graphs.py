

# 1. Route Between Nodes: Given a directed graph, design an algorithm to find out
# whether there is a route between two nodes.

import copy
from typing import List, Optional

from AdjacencyListGraph import Graph, Vertex

# 1. Route Between Nodes: Given a directed graph, design an algorithm to find out
# whether there is a route between two nodes.

g = Graph()
for i in range(1, 11):
    g.add_vertex(i)

g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(5, 6)
g.add_edge(6, 7)
g.add_edge(6, 9)
g.add_edge(7, 8)
g.add_edge(7, 9)
g.add_edge(9, 10)


def reverse_copy(graph: Graph) -> Graph:
    """Returns a copy of ``graph`` with the direction of all edges reversed."""
    rev_graph: Graph = copy.deepcopy(graph)
    for vertex in rev_graph:
        vertex.connected_to = {}
    for from_v in graph:
        for to_v in from_v.connected_to:
            rev_graph.add_edge(from_=to_v.id, to=from_v.id)

    return rev_graph


def find_route(from_: Vertex, to: Vertex) -> Optional[List]:
    """TODO"""
    # Without returning shortest route: 2 BFS with one starting at ``from_`` and the other
    #  starting at ``to`` on a transposed graph; return True if either ever encounter a
    #  "visited" vertex.
    # With returning route: Store discovery time (i.e. How many edges traversed to reach
    #  that vertex) of each node and when (if) the two BFS collide have them go past each
    #  other only visiting nodes if the discovery time is lower. The reversed BFS can go
    #  first, retracing steps to the beginning. Followed by the 'normal ordered' BFS
    #  tracing steps from collision -> end.


rev_g = reverse_copy(g)
