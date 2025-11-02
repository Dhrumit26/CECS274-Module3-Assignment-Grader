from Interfaces import Deque
from tests.m3.DLList import DLList
import numpy as np


class DLLDeque(Deque, DLList):
    def __init__(self):
        DLList.__init__(self)

    def add_first(self, x: object):
        """
        adds to the head of the list the element x
        :param x: object type; the new element
        """
        self.add(0, x)

    def add_last(self, x: object):
        """
        adds to the tail of the list the element x
        :param x: object type; the new element
        """
        self.add(self.n, x)

    def remove_first(self) -> object:
        """
        removes the head of the list and returns it
        :return: object type; the element that was removed
        """
        return self.remove(0)

    def remove_last(self) -> object:
        """
        removes the tail of the list and returns it.
        :return: object type; the element that was removed
        """
        return self.remove(self.n - 1)

    def clear(self):
        """
        removes all contents in the deque
        :return: None
        """
        self.__init__()

    def size(self):
        """
        returns the number of elements in the deque
        :return: int type;
        """
        return DLList.size(self)


# deque = DLLDeque()
#
# deque.add_last("A")
# deque.add_last("B")
# deque.add_last("C")
# deque.add_last("D")
# deque.add_last("E")
# deque.add_last("F")
#
# print("Result: ", deque)
# print("Expected deque: ['A','B','C','D','E','F']")
#
# expected = ['A','B','C','D','E','F']
# i = 0
# while deque.size() > 3:
#     print(f"\nResult: {deque.remove_first()}")
#     print(f"Expected: {expected[i]}")
#     i +=1
# print("\nResult: ", deque)
# print("Expected: ['D','E','F']")
#
# deque.clear()
# print("\nResult: ", deque)
# print("Expected: []")
#
# deque.add_last("a")
# deque.add_last("b")
# deque.add_last("c")
# deque.add_last("d")
# deque.add_last("e")
# deque.add_last("f")
# print("\nResult: ", deque)
# print("Expected: ['a','b','c','d','e','f']")
#
# expected = ['f', 'e', 'd']
# i = 0
# while deque.size() > 3:
#     print(f"\nResult: {deque.remove_last()}")
#     print(f"Expected: {expected[i]}")
#     i +=1
# print("\nResult: ", deque)
# print("Expected: ['a','b','c']")
#
# deque.clear()
# print("\nResult: ", deque)
# print("Expected: []")
#
# print("Attempting to access empty list (IndexError expected):", deque.get(0))
#
