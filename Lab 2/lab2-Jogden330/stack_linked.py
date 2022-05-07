class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    #Implements an efficient last-in first-out Abstract Data Type using a Linked List

    def __init__(self, capacity):
        #Creates and empty stack with a capacity'''
        self.capacity = capacity
        self.top = None
        self.num_items = 0

    # Returns True if the stack is empty, and False otherwise
    # MUST have O(1) performance'''
    def is_empty(self):
        if self.num_items == 0:
            return True
        else:
            return False


    # Returns True if the stack is full, and False otherwise
    #  MUST have O(1) performance''
    def is_full(self):
        if self.num_items == self.capacity:
            return True
        else:
            return False


    # If stack is not full, pushes item on stack. If stack is full when push is attempted, raises IndexError
    # MUST have O(1) performance

    def push(self, item):
        if not self.is_full():
            new_node = Node(item)
            new_node.next = self.top
            self.top = new_node
            self.num_items += 1
        else:
            raise IndexError


    # If stack is not empty, pops item from stack and returns item.
    # If stack is empty when pop is attempted, raises IndexError
    # MUST have O(1) performance'''
    def pop(self):
        if not self.is_empty():
            self.num_items -= 1
            data = self.top.data
            self.top = self.top.next
            return  data
        else:
            raise IndexError


    # If stack is not empty, returns next item to be popped (but does not pop the item)
    # If stack is empty, raises IndexError MUST have O(1) performance'''
    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            raise IndexError

    def size(self):
        return self.num_items


