class Stack:
    # '''Implements an efficient last-in first-out Abstract Data Type using a Python List'''

    def __init__(self, capacity):
        # '''Creates and empty stack with a capacity'''
        self.capacity = capacity
        self.items = [None]*capacity
        self.num_items = 0 

    def is_empty(self):
        if self.num_items == 0:
            return True
        else:
            return False


    def is_full(self):
        if self.num_items == self.capacity:
            return True
        else:
            return False




    def push(self, item):
        if not self.is_full():
            self.items[self.num_items] = item
            self.num_items += 1
        else:
            raise IndexError



    # '''If stack is not empty, pops item from stack and returns item.
    #    If stack is empty when pop is attempted, raises IndexError
    #    MUST have O(1) performance'''
    def pop(self):
        if not self.is_empty():
            self.num_items -= 1
            return self.items[self.num_items]
        else:
            raise IndexError


    # '''If stack is not empty, returns next item to be popped (but does not pop the item)
    #    If stack is empty, raises IndexError
    #    MUST have O(1) performance'''
    def peek(self):
        if not self.is_empty():
            return self.items[self.num_items - 1]
        else:
            raise IndexError


    # '''Returns the number of elements currently in the stack, not the capacity
    #    MUST have O(1) performance'''
    def size(self):
        return self.num_items


 