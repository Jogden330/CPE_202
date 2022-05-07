class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    # '''Use ONE dummy node as described in class
    # ***No other attributes***
    # DO NOT have an attribute to keep track of size'''
    def __init__(self):
        dummy_node = Node(None)
        self.head = dummy_node
        dummy_node.next = dummy_node
        dummy_node.prev = dummy_node

    # '''Returns True if OrderedList is empty
    # MUST have O(1) performance'''
    def is_empty(self):
        if(self.head.next == self.head):
            return True
        else:
            return False


    # '''Adds an item to OrderedList, in the proper location based on ordering of items
    # from lowest (at head of list) to highest (at tail of list) and returns True.
    # If the item is already in the list, do not add it again and return False.
    # MUST have O(n) average-case performance'''
    def add(self, item):
        new_node = Node(item)
        nodetochack = self.head
        while nodetochack.next != self.head:
            if nodetochack.next.item == new_node.item:
                return False
            elif nodetochack.next.item > new_node.item:
                nodetochack.next.prev = new_node
                new_node.next = nodetochack.next
                nodetochack.next = new_node
                new_node.prev = nodetochack
                return True
            else:
                nodetochack = nodetochack.next
        new_node.next = self.head
        new_node.prev = self.head.prev
        self.head.prev.next = new_node
        self.head.prev = new_node
        return True

    # '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list)
    # returns True.  If item was not removed (was not in the list) returns False
    # MUST have O(n) average-case performance'''
    def remove(self, item):
        nodetochack = self.head.next
        while nodetochack != self.head:
            if nodetochack.item == item:
                nodetochack.prev.next = nodetochack.next
                nodetochack.next.prev = nodetochack.prev
                return True
            nodetochack = nodetochack.next
        return False

    # '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
    # If item is not in list, return None
    # MUST have O(n) average-case performance'''
    def index(self, item):
        index = 0
        nodetochack = self.head.next
        while nodetochack != self.head:
            if nodetochack.item == item:
                return index
            index += 1
            nodetochack = nodetochack.next
        return None

    # '''Removes and returns item at index (assuming head of list is index 0).
    # If index is negative or >= size of list, raises IndexError
    #  MUST have O(n) average-case performance'''
    def pop(self, index):
       if index < 0 or index >= self.size():
           raise IndexError
       else:
           nodetochack = self.head.next
           for i in range(index):
               nodetochack = nodetochack.next
           nodetochack.prev.next = nodetochack.next
           nodetochack.next.prev = nodetochack.prev
           return nodetochack.item

    # '''Searches OrderedList for item, returns True if item is in list, False otherwise"
    #           To practice recursion, this method must call a RECURSIVE method that
    #           will search the list
    #           MUST have O(n) average-case performance'''

    def search(self, item):
        return self.search_helper(item, self.head.next)

    def search_helper(self, item, node):
        if node == self.head:
            return False
        if node.item == item:
            return True
        return self.search_helper(item, node.next)
    # '''Return a Python list representation of OrderedList, from head to tail
    # For example, list with integers 1, 2, and 3 would return [1, 2, 3]
    # MUST have O(n) performance'''
    def python_list(self):
        listiteam = [None]*self.size()    #needs to chnag to [none]*size to keep it 0(n)
        nodetochack = self.head.next
        for index in range(len(listiteam)):
            listiteam[index] = nodetochack.item
            nodetochack = nodetochack.next
        return listiteam

    # '''Return a Python list representation of OrderedList, from tail to head, using recursion
    #           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
    #           To practice recursion, this method must call a RECURSIVE method that
    #           will return a reversed list
    #           MUST have O(n) performance'''
    def python_list_reversed(self):
        revered_list = [None]*self.size()
        index = self.size()
        return self.python_list_reversed_helper(self.head.next, revered_list, index)

    def python_list_reversed_helper(self, node, revered_list, index):
        if node == self.head:
            return  revered_list
        revered_list[index - 1] = node.item
        return self.python_list_reversed_helper(node.next, revered_list, index - 1)


        # '''Returns number of items in the OrderedList
        # To practice recursion, this method must call a RECURSIVE method that
        # will count and return the number of items in the list
        # MUST have O(n) performance'''

    def size(self):
        return self.size_helper(self.head.next)

    def size_helper(self, node):
        if node == self.head:
            return 0
        else:
            return 1 + self.size_helper(node.next)

