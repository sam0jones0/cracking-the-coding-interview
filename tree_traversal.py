from BinarySearchTree import BinarySearchTree, TreeNode


b = BinarySearchTree()

for i in [8, 4, 2, 6, 10, 20]:
    b.put(i, i)


def in_order_print(node: TreeNode) -> None:
    """Traverses a binary tree in order.

    Visits the nodes in ascending order. Fully explores left branch, then the
     current node and finally the right branch.
    """
    if node is not None:
        in_order_print(node.left_child)
        print(node.value)
        in_order_print(node.right_child)


def pre_order_print(node: TreeNode) -> None:
    """Traverses a binary tree in pre-order.

    Visits the current node first before fully exploring the left branch, then
     the right branch.
    """
    if node is not None:
        print(node.value)
        pre_order_print(node.left_child)
        pre_order_print(node.right_child)


def post_order_print(node: TreeNode) -> None:
    """Traverses a binary tree in post-order.

    Visits all child nodes before the current node. Fully exploring the left
     branch, then the right branch.
    """
    if node is not None:
        post_order_print(node.left_child)
        post_order_print(node.right_child)
        print(node.value)


post_order_print(b.root)
