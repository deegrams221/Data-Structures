import sys
sys.path.append('doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Each element has a reference to both the next and the previous element.
        # This is useful bc having a reference to the previous element can speed up
        # some operations, like removing (“unlinking”) an element from a list or
        # traversing the list in reverse order.
        # sets doublylinkedlist to storage, used for adding and subtracting
        self.storage = DoublyLinkedList()

    # enqueue -> Adds an item to the queue. If the queue is full, then it is said to
    # be an Overflow condition – Time Complexity : O(1)
    # adding so set the size to += 1
    def enqueue(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)
        # pass

    # dequeue -> Removes an item from the queue. The items are popped in the same
    # order in which they are pushed. If the queue is empty, then it is said to be an
    # Underflow condition – Time Complexity : O(1)
    # removing so set the size -= 1
    def dequeue(self):
        # self.size -= 1
        # return self.storage.remove_from_head()
        # pass
        # if self.size == 0:
        #     pass
        # else:
        #     self.size -= 1
        #     return self.storage.remove_from_head()
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()

    # len -> length
    def len(self):
        return self.size
        # pass