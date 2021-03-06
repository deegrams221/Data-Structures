import sys
sys.path.append('/queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # pass
        # compare root node, if greator or equal go right
        if value >= self.value:
            # if no child
            if self.right == None:
                # insert
                self.right = BinarySearchTree(value)
            # else try again, continue right
            else:
                return self.right.insert(value)
        # if lesser go left
        elif value < self.value:
            # if no child
            if self.left == None:
                # insert
                self.left = BinarySearchTree(value)
            # else try again, continue left
            else:
                return self.left.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # pass
        # look at root, if root is taget return true
        if target == self.value:
            return True
        # if value is less than node
        elif target < self.value:
            # go left
            if self.left != None:
                # return if found
                return self.left.contains(target)
        # if value is greater or equal to node
        elif target >= self.value:
            # go right
            if self.right != None:
                # return if found
                return self.right.contains(target)
        # else return false
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # pass
        # if go right is none
        if self.right == None:
            # return the value
            return self.value
        # else continue right
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # pass
        # cb contains value
        cb(self.value)
        # if left and right both are not none
        # if self.left != None and self.right != None:
        #     # return for each (left/right) cb
        #     return (self.left.for_each(cb), self.right.for_each(cb))
        # # elif left is not none but right is none
        # elif self.left != None and self.right == None:
        #     # return left for each cb
        #     return self.left.for_each(cb)
        # # elif left is none but right is not none
        # elif self.left == None and self.right != None:
        #     # return right for each cb
        #     return self.right.for_each(cb)

        # can also be done this way... less code
        if self.left:
                self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
    # def in_order_print(self):
        # pass
        # if node is none, then return
        if node is None:
            return
        # else, in order print contains node left, print node value
        else:
            self.in_order_print(node.left)
            print(node.value)
            # in order print contains node right
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # pass
        # make a queue
        bftQueue = Queue()
        # enqueue root to queue
        bftQueue.enqueue(node)
        # iterate through the current node, while queue is not empty
        while bftQueue.len() > 0:
            # dequeue the root and assign to temporary queue
            tempQueue = bftQueue.dequeue()
            # print the temporary queue value
            print(tempQueue.value)
            # if temporary queue left add to queue
            if tempQueue.left:
                bftQueue.enqueue(tempQueue.left)
            # if temporary queue right add to queue
            if tempQueue.right:
                bftQueue.enqueue(tempQueue.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # pass
        # make a Stack
        dftStack = Stack()
        # use push to add root to stack
        dftStack.push(node)
        # iterated through current node, while while stack is not empty
        while dftStack.len() > 0:
            # use pop root and assign to temporary stack
            tempStack = dftStack.pop()
            # print the temporary stack value
            print(tempStack.value)
            # if temporary stack left then use push left
            if tempStack.left:
                dftStack.push(tempStack.left)
            #  if temporary stack right then use push right
            elif tempStack.right:
                dftStack.push(tempStack.right)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
