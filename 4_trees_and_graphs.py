# 1. Route Between Nodes: Given a directed graph, design an algorithm to find out
# whether there is a route between two nodes.

import copy
from collections import deque
from typing import Optional

from AdjacencyListGraph import Graph, Vertex


class ShortestRouteDirectedGraph:
    """Performs a bidirectional breadth first search on a graph to discover if
    there is a route between any two vertices and if so, what is the shortest
    route between them.

    Two copies are made of the provided graph, one with the edge's directions
     reversed. A BFS is performed starting at the `from_` and `to` vertices on
     the forward and reversed graphs respectively. The discovery of a node by a
     particular BFS is stored in the `vertex.colour` attribute (e.g. "red" or
     "black") which is initialised to "white", i.e. undiscovered. The discovery
     time of each vertex is stored in `vertex.disc`. Once a collision vertex is
     discovered a route has been found and the shortest route can be calculated.

    Attributes:
        _for_graph: A deepcopy of the provided ``graph``.
        _rev_graph: A deepcopy of the provided ``graph`` with the direction of
            all edges reversed.

    Args:
        graph: The directed `Graph` to search.
    """

    _for_graph: Optional[Graph]
    _rev_graph: Optional[Graph]

    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        self._for_graph = None
        self._rev_graph = None

    def route(self, from_: Vertex, to: Vertex) -> Optional[deque]:
        """Builds the optimal route between the vertices ``from_`` and ``to.

        Args:
            from_: The vertex at the start of the route.
            to: The vertex at the end of the route.

        Returns:
            A deque of the optimal route, or `None` if there is no route.
        """
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
        """Finds the collision node of two breadth first searches performed on a
         copy of the graph and on a reversed copy.

        The discovery time of each vertex is stored to help determine the shortest
         route.

        Args:
            from_: The vertex at the start of the route.
            to: The vertex at the end of the route.

        Returns:
            The vertex where the two BFS meet, else None.

        """
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
        """Visits the provided ``vertex`` and marks it's discovery by this particular
         BFS in the vertex's `colour` attribute. If the ``vertex`` has already been
         discovered by another BFS then it is returned as the collision node.

        Args:
            vertex: The vertex to visit.
            colour: The colour pertaining to a particular BFS

        Returns:
            The vertex where the two BFS collide, else None.

        """
        if vertex.colour == "white":
            vertex.colour = colour
        elif vertex.predecessor and vertex.colour != vertex.predecessor.colour:
            return vertex

    def _enqueue_neighbours(
            self, vertex: Vertex, queue: deque, disc_time: int, colour: str
    ) -> None:
        """Enqueues all neighbours of ``vertex`` to the end of the provided BFS
         ``queue``. Discovery time (round of BFS) and colour (particular BFS
         instance) are stored in the respective ``vertex`` attributes.

        Args:
            vertex: The ``vertex`` whose neighbours shall be enqueued.
            queue: The deque of the BFS to add neighbours to.
            disc_time: The discovery time of this vertex's neighbours. This increments
                 on each round of the BFS.
            colour: The colour pertaining to a particular BFS instance.
        """
        for neighbour_v in vertex.get_connections():
            if neighbour_v.colour != colour:
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

# g = Graph()
# for i in range(1, 11):
#     g.add_vertex(i)
#
# g.add_edge(1, 2)
# g.add_edge(2, 3)
# g.add_edge(3, 4)
# g.add_edge(3, 5)
# g.add_edge(5, 6)
# g.add_edge(6, 7)
# g.add_edge(6, 9)
# g.add_edge(7, 8)
# g.add_edge(7, 9)
# g.add_edge(9, 10)
#
#
# s = ShortestRouteDirectedGraph(g)
# route = s.route(g.get_vertex(1), g.get_vertex(10))
# print(route)
# print(list(map(lambda x: x.key, route)))  # [1, 2, 3, 5, 6, 9, 10]


# ----
# 2. Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height.

from BinarySearchTree import BinarySearchTree, TreeNode


def build_min_bst(lst: list) -> BinarySearchTree:
    """TODO"""
    mid = lst[(len(lst) // 2)]
    bst = BinarySearchTree()
    # bst.root = _build_min_bst_helper(lst[:mid], lst[mid + 1 :], mid)
    bst.root = _build_min_bst_helper(lst, mid)

    return bst


def _build_min_bst_helper(lst, mid):
    if mid == 0:
        return TreeNode(lst[0])
    elif mid == len(lst) - 1:
        return TreeNode(lst[len(lst - 1)])

    new_node = TreeNode(mid)
    new_node.left_child = _build_min_bst_helper(lst, mid // 2)
    new_node.right_child = _build_min_bst_helper(lst, mid + ((len(lst) - mid) // 2))

    return new_node


# def _build_min_bst_helper(left, right, mid):
#     if mid:
#         new_node = TreeNode(mid)
#         l_mid = left[len(left) // 2]
#         r_mid = right[len(right) // 2]
#         new_node.left_child = _build_min_bst_helper(
#             left[:l_mid], left[l_mid + 1:], l_mid
#         )
#         new_node.right_child = _build_min_bst_helper(
#             right[:r_mid], right[r_mid + 1:], r_mid
#         )
#
#         return new_node


# def _build_min_bst_helper(lst: list, node: TreeNode):
#     mid = lst[(len(lst) // 2)]
#
#     if mid is not None:
#         left = lst[:mid]
#         right = lst[mid + 1:]
#         node.left_child = _build_min_bst_helper(left, TreeNode)
#         node.right_child = TreeNode()
#         return mid

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = [0]

build_min_bst(a)
build_min_bst(b)
build_min_bst(c)
