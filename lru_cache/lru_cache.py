# import DoublyLinkedList
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        # pass
        # set self.limit to limit (for the max number of nodes it can hold)
        self.limit = limit
        # count set to 0 for the current number of nodes it is holding
        self.count = 0
        # a doubly-linked list that holds the key-value entries in the correct order
        self.doublyLinkedList = DoublyLinkedList()
        # storage dict that provides fast access to every node stored in the cache
        self.storageDict = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # pass
        if key in self.storageDict:
            # move the key-value pair to the end of the order such that the pair is
            # considered most-recently used
            self.doublyLinkedList.move_to_front(self.storageDict[key])
            # Returns the value associated with the key or None if the key-value pair
            # doesn't exist in the cache
            return self.storageDict[key].value
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # pass
        # if the key already exists in the cache
        if key in self.storageDict:
            # then overwrite the old value associated with the key with the newly-specified value
            node = self.storageDict[key]
            node.value = value
            self.doublyLinkedList.move_to_front(self.storageDict[key])
            return node.value
        # If the cache is already at max capacity before this entry is added
        if len(self.doublyLinkedList) >= self.limit:
            # then the oldest entry in the cache needs to be removed to make room
            tail = self.doublyLinkedList.tail
            self.doublyLinkedList.remove_from_tail()
            # check postion
            for oldest in self.storageDict:
                if self.storageDict[oldest] == tail:
                    # if the oldest item is at the tail, then delete it, otherwise break
                    del self.storageDict[oldest]
                    break
        # else add the new entry to the head
        self.doublyLinkedList.add_to_head(value)
        self.storageDict[key] = self.doublyLinkedList.head