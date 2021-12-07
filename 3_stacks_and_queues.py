# 1. Three in One: Describe how you could use a single array to implement three stacks.

from typing import Any


class TripleStackList:
    """Three stacks implemented using a single list.

    Methods for pushing, popping and checking if a stack is empty are provided.
     Methods for each stack can be accessed using its ID (0, 1 or 2).
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
