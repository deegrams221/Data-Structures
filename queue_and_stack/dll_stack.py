import sys
sys.path.append('doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    # adding so set the size to += 1
    def push(self, value):
        # pass
        self.size += 1
        return self.storage.add_to_head(value)

    # removing so set the size -= 1
    def pop(self):
        # pass
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()

    # len -> length
    def len(self):
        # pass
        return self.size
