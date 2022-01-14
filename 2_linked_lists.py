# 1. Remove Dups: Write code to remove duplicates from an  unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is  not allowed?

import collections


def dedupe_fast(self) -> None:
    """Removes duplicate items from list using additional storage to cut
    down on execution time."""
    seen = set()
    current = self.head
    prev = None
    while current is not None:
        if current.data in seen:
            prev.next = current.next
        else:
            seen.add(current.data)
            prev = current
        current = current.next


def dedupe_slow(self) -> None:
    """Removes duplicate items from list without using additional storage."""
    pointer_1 = self.head
    while pointer_1 is not None:
        pointer_2 = pointer_1
        while pointer_2.next is not None:
            if pointer_2.next.data == pointer_1.data:
                pointer_2.next = pointer_2.next.next
            else:
                pointer_2 = pointer_2.next
        pointer_1 = pointer_1.next


# [list.append(random.randint(0, 100)) for _ in range(1000)]
#   dedupe_fast_t.timeit(number=1000) == 0.0317972
#   dedupe_slow_t.timeit(number=1000) == 1.8594063


# ----
# 2. Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.


def k_to_last_sized(self, k: int) -> LlNode:
    """Finds the kth last element of a singly linked list where the size of the
    list is known.
    """
    if not 0 <= k < len(self):
        raise IndexError(f"`k` must be between 0 and {len(self)}.")

    current = self.head
    idx = 0
    while current is not None:
        if len(self) - 1 - idx == k:
            return current
        current = current.next
        idx += 1


def k_to_last_unsized(self, k: int) -> LlNode:
    """Finds the kth last element of a singly linked list where the size of the
    list is not known.

    Makes use of two pointers, where one pointer is k elements behind the other.
    """
    ahead = self.head
    behind = self.head
    idx = 0
    while ahead is not None:
        if idx > k:
            behind = behind.next
        idx += 1
        ahead = ahead.next

    if not 0 <= k < idx:
        raise IndexError(f"`k` must be between 0 and {idx}.")

    return behind


def print_k_to_last(self, k) -> None:
    """Prints the kth to last element using recursion."""
    self.k_to_last_helper(k, self.head, 0)


def k_to_last_helper(self, k, node, idx) -> int:
    if node is None:
        return idx

    size = self.k_to_last_helper(k, node.next, idx + 1)
    if size - 1 - idx == k:
        print(f"Result: {node}")

    return size


# ----
# 3. Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
# EXAMPLE
# Input: the node c from the linked list a -> b -> c -> d -> e -> f
# Result: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f


def delete_middle_node(self, node: LlNode) -> None:
    """Removes the provided node from the middle of a linked list."""
    if node == self.head or node == self.tail:
        raise ValueError("node cannot be the first or last element of the list.")

    node.data = node.next.data
    node.next = node.next.next


# ----
# 4. Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. lf x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5)
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8


def partition(self, x: int) -> None:
    """Partition a linked list around a value x using two linked lists and joining them
    together.
    """
    left = LinkedList()
    right = LinkedList()
    for item in self:
        if item.data < x:
            left.append(item)
        else:
            right.append(item)

    if left.tail is None:
        left.head = right.head
    else:
        left.tail.next = right.head
    self.head, self.tail = left.head, right.tail


def partition_deque(self, x: int) -> collections.deque:
    """Partition a linked list around a value using a deque."""
    from collections import deque

    d_q = deque()
    for item in self:
        if item.data < x:
            d_q.appendleft(item)
        else:
            d_q.append(item)

    return d_q


# ----
# 5. Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored  in reverse order, such that the 1's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
# Output:  2 -> 1 -> 9. That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# Input:  (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
# Output: 9 -> 1 -> 2. That is, 912.


def sum_llists(self, ll_1: LinkedList, ll_2: LinkedList) -> LinkedList:
    """Sums two numbers where the digits are stored in a linked list in reverse
    order, and returns the result in the same format.
    """
    from itertools import zip_longest

    pow_, sum_ = 0, 0
    for num_1, num_2 in zip_longest(ll_1, ll_2, fillvalue=LlNode(0)):
        sum_ += (num_1.data + num_2.data) * 10 ** pow_
        pow_ += 1

    result = LinkedList()
    for char in str(sum_):
        new_node = LlNode(int(char))
        new_node.next = result.head
        result.head = new_node

    return result


def sum_lists(self, ll_1: LinkedList, ll_2: LinkedList) -> LinkedList:
    """Sums two numbers where the digits are stored in a linked list and returns
    the result in the same format.
    """
    from itertools import zip_longest

    step, sum_ = 0, 0
    for num_1, num_2 in zip_longest(ll_1, ll_2, fillvalue=LlNode(0)):
        sum_ += num_1.data * 10 ** (len(ll_1) - 1 - step)
        sum_ += num_2.data * 10 ** (len(ll_2) - 1 - step)
        step += 1

    result = LinkedList()
    for char in str(int(sum_)):
        result.append(int(char))

    return result


# ----
# 6. Palindrome: Implement a function to check if a linked list is a palindrome.


def is_palindrome(ll: LinkedList) -> bool:
    """Checks if the items in a linked list form a palindrome."""
    from queue import LifoQueue

    stack = LifoQueue()
    for idx, node in enumerate(ll):
        if idx < len(ll) // 2:
            stack.put(node)
        elif len(ll) / 2 == idx + 0.5:
            pass
        elif node.data != stack.get().data:
            return False

    return True


def is_palindrome_2(ll: LinkedList) -> bool:
    """Checks if the items in a linked list form a palindrome.

    Similar to the above, but avoids the unnecessary check performed on each iteration
    to see if we are currently checking the middle node of a list of odd length.
    """
    from queue import LifoQueue

    stack = LifoQueue()
    current = ll.head
    idx = 0
    while idx < len(ll) // 2:
        stack.put(current)
        current = current.next
        idx += 1
    if len(ll) % 2 == 1:
        current = current.next
    while current is not None:
        if current.data != stack.get().data:
            return False
        current = current.next

    return True


# ----
# 7. Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the inter-
# secting node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.


def intersection_hashmap(ll_1: LinkedList, ll_2: LinkedList) -> Optional[LlNode]:
    """Determines if two linked lists intersect and if so returns the intersecting node.

    Takes up O(k) space where k is the length of the longest list.
    """
    ll_1_set = set()
    ll_1_node = ll_1.head
    while ll_1_node is not None:
        ll_1_set.add(ll_1_node)
        ll_1_node = ll_1_node.next

    ll_2_node = ll_2.head
    while ll_2_node is not None:
        if ll_2_node in ll_1_set:
            return ll_2_node
        ll_2_node = ll_2_node.next


def intersection_o1_space(ll_1: LinkedList, ll_2: LinkedList) -> Optional[LlNode]:
    """Determines if two linked lists intersect and if so returns the intersecting node.

    Takes up O(1) additional space.
    """
    len_diff = len(ll_1) - len(ll_2)
    if len_diff >= 0:
        bigger, smaller = ll_1.head, ll_2.head
    else:
        smaller, bigger = ll_1.head, ll_2.head
    for _ in range(abs(len_diff)):
        # Align so both lists have same number of elements remaining.
        bigger = bigger.next

    while bigger is not None:
        if bigger is smaller:
            return bigger
        smaller, bigger = smaller.next, bigger.next


# ----
# 8. Loop Detection: Given a circular linked list, implement an algorithm that returns
# the node at the beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer
# points to an earlier node, so as to make a loop in the linked list.
# EXAMPLE
# Input: A -> B -> C -> D -> E -> C [the same C as earlier]
# Output: C


def is_loop(self) -> Optional[LlNode]:
    slow, fast = self.head, self.head
    count = 0
    while fast is not None:
        count += 1
        slow = slow.next
        try:
            fast = fast.next.next  # Jump 2 ahead.
        except AttributeError:
            fast = None
        if fast is slow:
            return fast


def find_loop_start(self, collision_node: LlNode) -> LlNode:
    current = self.head
    c_node = collision_node

    while current is not c_node:
        current = current.next
        c_node = c_node.next

    return current


# collision_node = some_list.is_loop()
# if collision_node:
#     loop_start = some_list.find_loop_start(collision_node)
#     print(loop_start)
