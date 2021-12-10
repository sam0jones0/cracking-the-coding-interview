from typing import Any


# 1. Three in One: Describe how you could use a single array to implement three stacks.


class TripleStackList:
    """Three stacks implemented using a single list.

    Methods for pushing, popping and checking if a stack is empty are provided.
     Methods for each stack can be accessed using its ID (0, 1 or 2).

    Attributes:
        _data: The stored data for all three stacks.
        _data_top: A record of the top index for each individual stack.
    """

    def __init__(self) -> None:
        """Inits 3 empty stacks."""
        self._data = [None, None, None]
        self._data_top = [0, 1, 2]

    def _extend(self) -> None:
        """Extends the internal data structure by one slot per stack."""
        self._data.extend([None, None, None])

    def _clean(self) -> None:
        """Reduces the size of the internal data structure if the last slot on
        each stack is unused.
        """
        if len(self._data) > 3:
            for idx in range(1, 4):
                if self._data[-idx] is not None:
                    return
            for _ in range(3):
                self._data.pop()

    def push(self, stack_id: int, item: Any) -> None:
        """Pushes ``item`` onto the stack with the matching ``stack_id``.

        Args:
            stack_id: The ID of the stack to push to (0, 1, or 2).
            item (): The data to be added to the stack.
        """
        if not self.is_empty(stack_id):
            self._data_top[stack_id] += 3
        top_idx = self._data_top[stack_id]
        if top_idx > len(self._data) - 1:
            self._extend()
        self._data[top_idx] = item

    def pop(self, stack_id: int) -> Any:
        """Pops the most recently added item from the stack ``stack_id``.

        Args:
            stack_id: The ID of the stack to pop from (0, 1 or 2)

        Returns:
            The most recently added item from stack ``stack_id``.

        Raises:
            IndexError: If an attempt to pop from an empty stack is made.
        """
        if self.is_empty(stack_id):
            raise IndexError(f"Popped empty stack. ID: {stack_id} is empty.")

        top_idx = self._data_top[stack_id]
        res = self._data[top_idx]
        self._data[top_idx] = None
        if not self.is_empty(stack_id):
            self._data_top[stack_id] -= 3
        self._clean()

        return res

    def is_empty(self, stack_id) -> bool:
        """Returns `True` if the stack ``stack_id`` is empty, `False` otherwise."""
        return self._data[stack_id] is None

    def __str__(self) -> str:
        return str(self._data)


# trip_stack = TripleStackList()


# ----
# 2. Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.


class StackMin:
    """A stack data structure with a min function.

    Uses lists for internal representation of the stack. In addition to push,
     pop and min are provided with O(1) time complexity.

    Attributes:
        _data: The data stored within the stack.
        _mins: The minimum value of the stack at each point a new minimum is
            found.
    """

    def __init__(self) -> None:
        """Initialises the internal stack data and list of minimums at each stack
        state.
        """
        self._data = []
        self._mins = []

    def push(self, item: Any):
        """Pushes the provided ``item`` onto the stack and updates the minimum
        if necessary.

        Args:
            item: The item to push onto the stack.
        """
        if not self._mins:
            self._mins.append(item)
        elif item <= self._mins[-1]:
            self._mins.append(item)
        self._data.append(item)

    def pop(self) -> Any:
        """Pops an item from the top of the stack and updates the minimum if
        necessary.
        """
        item = self._data.pop()
        if item == self._mins[-1]:
            self._mins.pop()

        return item

    def min(self) -> int:
        """Returns the minimum item in the stack."""
        return self._mins[-1]

    def __str__(self) -> str:
        return str(self._data)


# import random
# min_stack = StackMin()
# [min_stack.push(random.randint(0, 30)) for _ in range(11)]
#
# print(min_stack)
# print(min_stack._mins)
#
# for _ in range(len(min_stack._data)):
#     my_min = min_stack.min()
#     py_min = min(min_stack._data)
#     print(my_min, "=", py_min)
#     assert my_min == py_min
#     min_stack.pop()


# ----
# 3. Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
# (that is, pop() should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt (int index) which performs a pop operation on a specific sub-stack.


class SetOfStacks:
    """A stack data structure represented internally by sets of stacks of
    max length `max_stack_size`.

    Args:
        max_stack_size: The max length for each individual inner stack.

    Attributes:
        stack_size: The maximum inner stack size.
        stacks: The stack data represented as lists of lists (used as stacks).
    """

    def __init__(self, max_stack_size: int = 10) -> None:
        self.stack_size = max_stack_size
        self.stacks = [[]]

    def push(self, item: Any) -> None:
        """Pushes the provided ``item`` on the top of the current stack.

        Appends a new stack onto self.stacks if the current stack is full.
        """
        if len(self.stacks[-1]) == self.stack_size:
            self.stacks.append([item])
        else:
            self.stacks[-1].append(item)

    def pop(self) -> Any:
        """Pops the top item from the stack.

        Cleans up any empty stacks before popping, unless only one inner stack
         remains.
        """
        while not (self.stacks[-1] or len(self.stacks) == 1):
            self.stacks.pop()

        return self.stacks[-1].pop()

    def pop_at(self, idx: int) -> Any:
        """Pops an item from the inner stack at the provided index ``idx``.

        Should this lead to an empty inner stack, it will be cleaned/removed when
         reached by `self.pop()`.

        Attributes:
            idx: The index of the inner stack to pop from.
        """
        return self.stacks[idx].pop()

    def __str__(self) -> str:
        return str(self.stacks)


# s = SetOfStacks()
#
# for i in range(25):
#     s.push(i)
# print(s)
#
# for i in range(20):
#     s.pop()
# print(s)


# ----
# 4. Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.


class MyQueue:
    def __init__(self):
        self._stack_1 = []
        self._stack_2 = []
        self._enqueued_last = False

    def enqueue(self, item):
        if not self._enqueued_last:
            self._reverse(self._stack_2, self._stack_1)
            self._enqueued_last = True
        self._stack_1.append(item)

    def dequeue(self):
        if self._enqueued_last:
            self._reverse(self._stack_1, self._stack_2)

        return self._stack_2.pop()

    def _reverse(self, from_, to):
        """TODO"""
        # NOTE: After reading solution; reverse in order to enqueue can be avoided
        #  by only populating the 'oldest' stack_2 when dequeuing.
        if self._stack_1 or self._stack_2:
            to.clear()
            while from_:
                to.append(from_.pop())
            self._enqueued_last = True if self._stack_1 else False

    def __str__(self):
        if self._enqueued_last:
            self._reverse(self._stack_1, self._stack_2)

        return str(self._stack_2)


# q = MyQueue()
#
# for i in range(11):
#     q.enqueue(i)
# print(q)
#
# for _ in range(6):
#     q.dequeue()
# print(q)


# ----
# 5.