from typing import Any, List, Union, Type


# 1. Three in One: Describe how you could use a single array to implement three stacks.


class TripleStackList:
    """Three stacks implemented using a single list.

    Methods for pushing, popping and checking if a stack is empty are provided.
     Methods for each stack can be accessed using its ID (0, 1 or 2).

    Attributes:
        _data: The stored data for all three stacks.
        _data_top: A record of the top index for each individual stack.
    """

    _data: List[Any]
    _data_top: List[int]

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

    _data: List[Any]
    _mins: List[Any]

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

    stacks: List[List[Any]]

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


class MyQueue1:
    """A Queue implemented using two stacks.

    Attributes:
        _stack_1: A stack in old -> new order to which new items are added.
        _stack_2: A stack to hold the reversed _stack_1. Items in new -> old order
             from which items are popped.
        _enqueued_last: A toggle flag denoting if an item was enqueued more recently
             than dequeued.
    """

    _stack_1: List[Any]
    _stack_2: List[Any]
    _enqueued_last: bool

    def __init__(self):
        self._stack_1 = []
        self._stack_2 = []
        self._enqueued_last = False

    def enqueue(self, item: Any) -> None:
        """Enqueues the provided ``item`` to the back of the queue.

        If an item was dequeued last, the items must be reversed first.

        Args:
            item: The item to enqueue.
        """
        if not self._enqueued_last:
            self._reverse(self._stack_2, self._stack_1)
            self._enqueued_last = True
        self._stack_1.append(item)

    def dequeue(self) -> Any:
        """Dequeues and returns an item from the front of the queue.

        If an item was enqueued last, the items must be reversed first.
        """
        if self._enqueued_last:
            self._reverse(self._stack_1, self._stack_2)

        return self._stack_2.pop()

    def _reverse(self, from_: list, to: list) -> None:
        """Reverses the items in internal stacks so items can be added to the correct
         end of the queue.

        Args:
            from_: The stack which to be reversed.
            to: The stack to place the reversed items.
        """
        # FIXME: After reading solution; reverse in order to enqueue can be avoided
        #  by only populating the 'oldest' stack_2 when dequeuing (see MyQueue2 below).
        if self._stack_1 or self._stack_2:
            to.clear()
            while from_:
                to.append(from_.pop())
            self._enqueued_last = True if self._stack_1 else False

    def __str__(self) -> str:
        if self._enqueued_last:
            self._reverse(self._stack_1, self._stack_2)

        return str(self._stack_2)


class MyQueue2:
    """A Queue implemented using two stacks.

    Attributes:
        _new_top: A stack in old -> new order to which new items are added.
        _old_top: A stack to hold the reversed _new_top. Items are in new -> old
             order from which items are popped.
    """

    _new_top: List[Any]
    _old_top: List[Any]

    def __init__(self):
        self._new_top = []
        self._old_top = []

    def enqueue(self, item: Any) -> None:
        """Enqueues the provided ``item`` to the back of the queue.

        Args:
            item: The item to enqueue.
        """
        self._new_top.append(item)

    def dequeue(self) -> Any:
        """Dequeues and returns an item from the front of the queue.

        If _old_top if empty, items must be popped from _new_top and pushed to
         _old_top (in effect reversing _new_top).
        """
        if not self._old_top:
            self._reverse()

        return self._old_top.pop()

    def _reverse(self) -> None:
        """Pops items from _new_top onto _old_top (in effect reversing _new_top)."""
        while self._new_top:
            self._old_top.append(self._new_top.pop())

    def __str__(self) -> str:
        return str(list(reversed(self._new_top)) + self._old_top)


# q = MyQueue()
#
# for i in range(11):
#     q.enqueue(i)
# print(q)
#
# for _ in range(6):
#     q.dequeue()
# for _ in range(11, 14):
#     q.enqueue(_)
# for _ in range(2):
#     q.dequeue()
# print(q)


# ----
# 5. Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.

import operator


def sort_stack(stack: list, reverse: bool = False) -> list:
    """Sorts ``stack`` so the smallest items are on top only using an additional
     temporary stack.

     Recursive calls are made on each partially sorted stack until no further
      swaps are made.

    Args:
        stack: The stack to sort.
        reverse: Flag tracking whether the stack is reversed or in its original
             order on each sort pass.
    """
    comp = operator.lt if reverse else operator.gt
    temp_stack = []
    made_swaps = False

    current = stack.pop()
    while stack:
        if comp(current, stack[-1]):
            temp_stack.append(stack.pop())
            made_swaps = True
        else:
            temp_stack.append(current)
            current = stack.pop()
    temp_stack.append(current)

    if made_swaps or not reverse:
        stack = sort_stack(temp_stack, not reverse)
    else:
        return temp_stack

    return stack


def sort_stack_2(stack: list) -> list:
    """Sorts ``stack`` so the smallest items are on top only using an additional
      temporary stack.

     Marginally faster than `sort_stack` as in certain conditions the whole stack
      does not need to be traversed.

    Args:
        stack: The stack to sort.
    """
    temp_stack = []
    while stack:
        current = stack.pop()
        while temp_stack and current < temp_stack[-1]:
            stack.append(temp_stack.pop())
        temp_stack.append(current)
    while temp_stack:
        stack.append(temp_stack.pop())

    return stack


# s = [6, 1, 7, 2, 9, 3, 5, 4, 8, 10]
#
# print(sort_stack_2(s))

# n              sort_stack   sort_stack_2
# 100               0.00065        0.00086
# 200               0.00252        0.00227
# 300               0.00534        0.00509
# 400               0.00856        0.00851
# 500               0.01293        0.01395
# 600               0.02039        0.01940
# 700               0.02504        0.02565
# 800               0.03237        0.03233
# 900               0.04062        0.04062
# 1000              0.05031        0.05258


# ----
# 6. Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat. You may use the built-in Linked List data structure.

from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class Animal:
    num: int = None


@dataclass
class Cat(Animal):
    pass


@dataclass
class Dog(Animal):
    pass


class AnimalShelter:
    """A data structure representing an animal shelter that only accepts dogs
    and cats. Animals must be adopted on a FIFO basis, although a choice between
    dog or cat can be made.

    Attributes:
        cats: A linked list containing all cats currently in the shelter.
        dogs: A linked list containing all dogs currently in the shelter.
        order_in: An int representing the order animals are admitted.
        allowed_animals: A list of Types of animals allowed at the shelter.
    """

    cats: LinkedList
    dogs: LinkedList
    order_in: int
    allowed_animals: List[Type[Union[Cat, Dog]]]

    def __init__(self) -> None:
        self.cats = LinkedList()
        self.dogs = LinkedList()
        self.order_in = 0
        self.allowed_animals = [Cat, Dog]

    def enqueue(self, animal: Animal) -> None:
        """Adds an animal to the shelter.

        Args:
            animal: The cat or dog to admit to the shelter.
        """
        if type(animal) not in self.allowed_animals:
            raise TypeError(self.gen_accepted_animals_err())
        animal.num = self.order_in
        if isinstance(animal, Cat):
            self.cats.append(animal)
        elif isinstance(animal, Dog):
            self.dogs.append(animal)
        self.order_in += 1

    def dequeue_any(self) -> Optional[Union[Cat, Dog]]:
        """Dequeues either a dog or cat from the shelter, whichever animal has
        been there the longest.
        """
        dog = self.dogs.head.data
        cat = self.cats.head.data
        if dog is None and cat is None:
            animal = None
        elif cat is None:
            animal = self.dequeue_dog()
        elif dog is None:
            animal = self.dequeue_cat()
        elif dog.num < cat.num:
            animal = self.dequeue_dog()
        else:
            animal = self.dequeue_cat()

        return animal

    def dequeue_cat(self) -> Optional[Cat]:
        """Dequeues the cat which has been at the shelter the longest."""
        if not self.cats.is_empty():
            return self.cats.pop(0)

    def dequeue_dog(self) -> Optional[Dog]:
        """Dequeues the dog which has been at the shelter the longest."""
        if not self.dogs.is_empty():
            return self.dogs.pop(0)

    def gen_accepted_animals_err(self) -> str:
        """Generates an error message clarifying which animals are accepted at
        the shelter.
        """
        if len(self.allowed_animals) > 1:
            err = f"""Only {"'s, ".join([type(animal).__name__ for animal in self.allowed_animals[:-1]])}"""
            err += f"""'s and {type(self.allowed_animals[-1]).__name__}'s are accepted at this shelter."""
        elif len(self.allowed_animals) == 1:
            err = f"Only {type(self.allowed_animals[0]).__name}'s are accepted at this shelter."
        else:
            err = "Shelter currently can't accept any animals."

        return err
