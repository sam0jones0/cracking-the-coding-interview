# 1. Route Between Nodes: Given a directed graph, design an algorithm to find out
# whether there is a route between two nodes.

import copy
from typing import List, Optional

from AdjacencyListGraph import Graph, Vertex

from collections import deque

# 1. Route Between Nodes: Given a directed graph, design an algorithm to find out
# whether there is a route between two nodes.


class ShortestRouteDirectedGraph:
    """# Without returning shortest route: 2 BFS with one starting at ``from_`` and the other
    #  starting at ``to`` on a transposed graph; return True if either ever encounter a
    #  "visited" vertex.
    # With returning route: Store discovery time (i.e. How many edges traversed to reach
    #  that vertex) of each node and when (if) the two BFS collide have them go past each
    #  other only visiting nodes if the discovery time is lower. The reversed BFS can go
    #  first, retracing steps to the beginning. Followed by the 'normal ordered' BFS
    #  tracing steps from collision -> end.

    # Visit: Set colour black, set discovery time and recursive DFS.
    # Visit from_ on g, visit to on rev_g
    # if encounter a black node we have found the midpoint of path and stop DFS, else return None.
    # Store mid point in linked list (ll).
    # continue g traverse only visiting lowest discovery time node, appending each to ll.
    # continue rev_g traverse only v low disc time, inserting at ll[0].
    # return ll as optimal path from -> to, else None.
    """

    _for_graph: Optional[Graph]
    _rev_graph: Optional[Graph]

    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        self._for_graph = None
        self._rev_graph = None

    def route(self, from_: Vertex, to: Vertex) -> Optional[deque]:
        """TODO"""
        collision_node = self._find_route(from_, to)
        if not collision_node:
            return
        route = deque()  # Used as a linked list.

        vertex = self._for_graph.get_vertex(collision_node.key)
        while vertex.key != to.key:
            route.append(self.graph.get_vertex(vertex.key))
            vertex = min(vertex.connected_to, key=lambda x: x.disc)
        route.append(to)

        vertex = self._rev_graph.get_vertex(collision_node.key)
        while vertex.key != from_.key:
            vertex = min(vertex.connected_to, key=lambda x: x.disc)
            route.appendleft(self.graph.get_vertex(vertex.key))

        return route

    def _find_route(self, from_: Vertex, to: Vertex) -> Optional[Vertex]:
        """TODO"""
        self._for_graph = copy.deepcopy(self.graph)
        self._rev_graph = self._reverse_copy()
        from_queue, to_queue = deque(), deque()
        from_queue.append(self._for_graph.get_vertex(from_.key))
        to_queue.append(self._rev_graph.get_vertex(to.key))

        disc_time = 1
        while from_queue and to_queue:
            from_v, to_v = from_queue.popleft(), to_queue.popleft()
            collision_node = self._visit(from_v, "red") or self._visit(to_v, "black")
            if collision_node:
                return collision_node
            self._enqueue_neighbours(from_v, from_queue, disc_time, "red")
            self._enqueue_neighbours(to_v, to_queue, disc_time, "black")
            disc_time += 1

    def _visit(self, vertex: Vertex, colour: str) -> Optional[Vertex]:
        """TODO"""
        if vertex.colour == "white":
            vertex.colour = colour
        elif vertex.predecessor and vertex.colour != vertex.predecessor.colour:
            return vertex

    def _enqueue_neighbours(
        self, vertex: Vertex, queue: deque, disc_time: int, colour: str
    ) -> None:
        """TODO"""
        for neighbour_v in vertex.get_connections():
            if neighbour_v.colour != colour:
                # TODO: Change colour here (?), otherwise discovery can be overwritten.
                if neighbour_v.colour == "white":
                    self._for_graph.get_vertex(neighbour_v.key).set_discovery(disc_time)
                    self._rev_graph.get_vertex(neighbour_v.key).set_discovery(disc_time)
                    self._for_graph.get_vertex(neighbour_v.key).colour = colour
                    self._rev_graph.get_vertex(neighbour_v.key).colour = colour
                neighbour_v.set_predecessor(vertex)
                queue.append(neighbour_v)

    def _reverse_copy(self) -> Graph:
        """Returns a copy of ``graph`` with the direction of all edges reversed."""
        reversed_graph: Graph = copy.deepcopy(self.graph)
        for vertex in reversed_graph:
            vertex.connected_to = {}
        for from_v in self.graph:
            for to_v in from_v.connected_to:
                reversed_graph.add_edge(from_=to_v.key, to=from_v.key)

        return reversed_graph


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


s = ShortestRouteDirectedGraph(g)
route = s.route(g.get_vertex(1), g.get_vertex(8))
print(route)
print(list(map(lambda x: x.key, route)))
