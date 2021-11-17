# 1. Remove Dups: Write code to remove duplicates from an  unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is  not allowed?


def dedupe_fast(self):
    """Remove duplicate items from list using additional storage to cut
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


def dedupe_slow(self):
    """Remove duplicate items from list without using additional storage."""
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


def k_to_last(self, k: int) -> Ll_node:

