
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    # '''Creates an empty Queue with a capacity'''
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.back = 0
        self.num_items = 0

        pass

    # '''Returns True if the Queue is empty, and False otherwise'''
    def is_empty(self):
        if self.num_items == 0:
            return True
        else:
            return False


    # '''Returns True if the Queue is full, and False otherwise'''
    def is_full(self):
        if self.num_items == self.capacity:
            return True
        else:
            return False

    # '''If Queue is not full, enqueues (adds) item to Queue
    # If Queue is full when enqueue is attempted, raises IndexError'''
    def enqueue(self, item):
        if not self.is_full():
            self.items[self.back] = item
            if (self.back + 1) >= self.capacity:
                 self.back = 0
            else:
                self.back += 1
            self.num_items += 1
        else:
            raise IndexError

    # '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
    #    If Queue is empty when dequeue is attempted, raises IndexError'''
    def dequeue(self):
        if not self.is_empty():
            self.num_items -= 1
            data = self.items[self.front]
            if (self.front + 1) >= self.capacity:
                self.front = 0
            else:
                self.front += 1
            return data
        else:
            raise IndexError


    # '''Returns the number of elements currently in the Queue, not the capacity'''
    def size(self):
        return self.num_items

