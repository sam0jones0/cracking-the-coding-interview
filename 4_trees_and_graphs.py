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
    """Creates and returns a binary search tree of minimal height when provided
    a sorted (asc) array of unique integers.
    """
    bst = BinarySearchTree()
    bst.root = _build_min_bst_helper(lst, 0, len(lst))

    return bst


def _build_min_bst_helper(lst, start, end):
    mid = start + ((end - start) // 2)
    if mid == 0:
        return TreeNode(mid)
    elif start != mid:
        new_node = TreeNode(mid)
        new_node.left_child = _build_min_bst_helper(lst, start, mid)
        new_node.right_child = _build_min_bst_helper(lst, mid, end)
        return new_node


# a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# build_min_bst(b)


# ----
# 3. List of Depths: Given a binary tree, design an algorithm which creates a
# linked list of all the nodes at each depth (e.g., if you have a tree with
# depth 0, you'll have 0 linked lists).

import random
from collections import deque
from typing import List, Optional

from BinarySearchTree import BinarySearchTree, TreeNode


# tree = BinarySearchTree()
# for _ in range(10):
#     tree.put(random.randint(0, 100), None)


def list_of_depths(bst: BinarySearchTree) -> List[Optional[List]]:
    """Constructs a list of sublists containing the keys for nodes on each level
    of a binary search tree.

    Each sublist contains the keys for nodes found on that level.

    Args:
        bst: A binary search tree.
    """
    n_list = bst_bfs(bst.root)
    res = [[n_list[0]]] if n_list else []
    idx, level, found = 1, 1, 0
    while idx < len(n_list):
        res.append([])
        this_row_n = found * 2 or 2  # First loop found will be 0 as root already added.
        found = 0
        for _ in range(this_row_n):
            item = n_list[idx]
            if item is not None:
                res[level].append(item)
                found += 1
            idx += 1
        level += 1
    res.pop()

    return res


def bst_bfs(root: TreeNode) -> List[Optional[int]]:
    """Runs a breadth first search on a binary search tree, appending `None` to
    note a missing child of a previously discovered node.

    Args:
        root: The root of a binary search tree to start the search.

    Returns:
        A list of sublists of node keys grouped by level on a binary search tree.
    """
    result = []
    q = deque()
    q.append(root)
    while q:
        node: TreeNode = q.popleft()
        if node:
            left, right = node.left_child, node.right_child
            q.append(left)
            q.append(right)
            result.append(node.key)
        else:
            result.append(node)

    return result


# print(list_of_depths(tree))


# After reading the (much simpler) answer I implemented the solution in Python.


def list_of_depths_2(
    node: TreeNode, result: List[Optional[List]], level: int = 0
) -> Optional[List[Optional[List]]]:
    """Constructs a list of sublists containing the keys for nodes on each level
    of a binary search tree using a pre-order search.

    Args:
        node: The root of a binary search tree to start the search.
        result: A list to store the sublists.
        level: The level of the binary tree we are currently on.

    Returns:
        A list of sublists of node keys grouped by level on a binary search tree.
    """
    if node is None:
        return result
    if level > len(result) - 1:
        result.append([])
    result[level].append(node.key)
    list_of_depths_2(node.left_child, result, level + 1)
    list_of_depths_2(node.right_child, result, level + 1)

    return result


# print(list_of_depths_2(tree.root, []))


# ----
# 4. Check Balanced: Implement a function to check if a binary tree is balanced.
# For the purposes of this question, a balanced tree is defined to be a tree
# such that the heights of the two subtrees of any node never differ by more
# than one.

import random
from typing import Optional

from BinarySearchTree import BinarySearchTree, TreeNode


def is_balanced(root: TreeNode, max_imbalance: int = 1) -> bool:
    """Checks if a binary tree is balanced up to a provided ``max_imbalance``
    factor.

    Args:
        root: The root of a binary search tree.
        max_imbalance: The maximum amount the height of any two subtrees can
            differ.

    Returns:
        True if the tree is balanced, False otherwise.

    """
    return _is_balanced_helper(root, max_im=max_imbalance) >= 0


def _is_balanced_helper(
    root: TreeNode, max_im: int = 1, level: int = 0, leaf_lvl: Optional[int] = None
) -> int:
    if root is None:
        return leaf_lvl

    if not (root.left_child and root.right_child):  # 0 or 1 children (leaf node).
        if leaf_lvl is None:
            leaf_lvl = level + max_im
        elif not (0 <= abs(level - leaf_lvl) <= max_im):
            # Found leaf with height difference from another leaf of more than max_im.
            return -1

    if leaf_lvl and level > leaf_lvl:
        return -1  # Found imbalance.
    else:
        leaf_lvl = _is_balanced_helper(root.left_child, max_im, level + 1, leaf_lvl)
        leaf_lvl = _is_balanced_helper(root.right_child, max_im, level + 1, leaf_lvl)

    return leaf_lvl


# def gen_tree(n):
#     tree = BinarySearchTree()
#     for _ in range(n):
#         tree.put(random.randint(0, 101), None)
#     return tree
#
#
# tree = gen_tree(20)
# i = 1
# while not is_balanced(tree.root):
#     tree = gen_tree(20)
#     i += 1
#
# tree.root.display()
# print(f"Took {i} attempts")


# ----
# 5. Validate BST: Implement a function to check if a binary tree is a binary
# search tree.

import sys

from BinarySearchTree import TreeNode


def validate_bst(root: TreeNode) -> bool:
    """Validates that a binary tree is a binary search tree.

    In-order traversal is used to check each node is bigger than the last
    visited. Assumes all node keys are positive integers.

    Args:
        root: The root node of the binary tree to validate.

    Returns:
        `True` if ``root`` is a binary search tree, `False` otherwise.
    """
    return not _validate_bst_helper(root, -1) == sys.maxsize


def _validate_bst_helper(root: TreeNode, current: int = -1) -> int:
    if root is not None and current != sys.maxsize:
        current = _validate_bst_helper(root.left_child, current)
        current = root.key if root.key >= current else sys.maxsize
        current = _validate_bst_helper(root.right_child, current)

    return current


# 1st attempt below. It works but uses unnecessary additional space.

# def _validate_bst_helper(root: TreeNode, res: Optional[List] = None) -> List:
#     if root is not None and (res or [-1])[-1] != sys.maxsize:
#         _validate_bst_helper(root.left_child, res)
#         if root.key >= (res or [-1])[-1]:
#             res.append(root.key)
#         else:
#             res.append(sys.maxsize)
#             return res
#         _validate_bst_helper(root.right_child, res)
#
#     return res


# print(validate_bst(bst.root))
