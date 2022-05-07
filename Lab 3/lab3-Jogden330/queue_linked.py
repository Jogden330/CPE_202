
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class Queue:
    '''Implements an link-based ,efficient first-in first-out Abstract Data Type'''

    # '''Creates an empty Queue with a capacity'''
    def __init__(self, capacity):

        self.capacity = capacity
        self.front = None
        self.back = None
        self.num_items = 0

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
    #    If Queue is full when enqueue is attempted, raises IndexError'''
    def enqueue(self, item):
        if not self.is_full():
            new_node = Node(item)
            if(self.num_items == 0):
                # new_node.next = self.front
                self.front = new_node
                self.back = new_node
            else:
                self.back.next = new_node
                self.back = new_node
            self.num_items += 1
        else:
            raise IndexError


    # '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
    #    If Queue is empty when dequeue is attempted, raises IndexError'''
    def dequeue(self):
        if not self.is_empty():
            self.num_items -= 1
            data = self.front.data
            self.front = self.front.next
            return data
        else:
            raise IndexError

    # '''Returns the number of elements currently in the Queue, not the capacity'''
    def size(self):
        return self.num_items
