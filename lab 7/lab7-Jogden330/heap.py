
class MaxHeap:
    #'''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''
    def __init__(self, capacity=50):
        self.heap = [None]*(capacity+1)
        self.nume_items = 0

    # '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
    # "item" can be any primitive or ***object*** that can be compared with other
    # items using the < operator'''
    def enqueue(self, item):
        if self.is_full():
            return False
        else:
            self.nume_items += 1
            self.heap[self.get_size()] = item
            self.perc_up(self.get_size())
            return True

        # Should call perc_up
        

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.heap[1]
    #     '''returns max without changing the heap, returns None if the heap is empty'''
    #
    # '''returns max and removes it from the heap and restores the heap property
    #     returns None if the heap is empty'''
    def dequeue(self):
        if self.is_empty():
            return None
        max = self.heap[1]
        self.heap[1] = self.heap[self.get_size()]
        self.heap[self.get_size()] = None
        self.nume_items -= 1
        self.perc_down(1)
        return max
        # Should call perc_down

    # '''returns a list of contents of the heap in the order it is stored internal to the heap.
    #         (This may be useful for in testing your implementation.)'''
    def contents(self):
       return self.heap[1:self.get_size()+1]


    # '''Discards all items in the current heap and builds a heap from
    # the items in alist using the bottom-up construction method.
    # If the capacity of the current heap is less than the number of
    # items in alist, the capacity of the heap will be increased to accommodate
    # exactly the number of items in alist'''
    # # Bottom-Up construction.  Do NOT call enqueue

    def build_heap(self, alist):
        self.nume_items = len(alist)
        if self.get_capacity() < len(alist):
            self.heap = [None] + alist[:]
        else:
            for index in range(len(alist)):
                self.heap[index+1] = alist[index]
        i = (len(alist))//2
        while (i > 0):
            self.perc_down(i)
            i -= 1


    # '''returns True if the heap is empty, false otherwise'''
    def is_empty(self):
        if self.nume_items == 0:
            return True
        else:
            return False


        # '''returns True if the heap is full, false otherwise'''
    def is_full(self):
        if self.get_size() == (self.get_capacity()):
            return True
        else:
            return False


        # '''this is the maximum number of a entries the heap can hold
        # 1 less than the number of entries that the array allocated to hold the heap can hold'''
    def get_capacity(self):
        return (len(self.heap) - 1)

    # '''the actual number of elements in the heap, not the capacity'''
    def get_size(self):
        return self.nume_items


        # '''where the parameter i is an index in the heap and perc_down moves the element stored
        # at that location to its proper place in the heap rearranging elements as it goes.'''
    def perc_down(self, i):
        while (i * 2) <= self.get_size():
            if i * 2 + 1 > self.get_size():
              LargerIndex = i * 2
            else:
                if self.heap[i * 2] > self.heap[i * 2 + 1]:
                    LargerIndex = i * 2
                else:
                    LargerIndex = i * 2 + 1
            if self.heap[i] < self.heap[LargerIndex]:
                self.swop(i, LargerIndex)
            i = LargerIndex

    def swop(self, i, LargerIndex):
        temp = self.heap[i]
        self.heap[i] = self.heap[LargerIndex]
        self.heap[LargerIndex] = temp


        # item = self.heap[i]
        #
        # while i * 2 < self.get_size()  and  (item <= self.heap[i*2] or item <= self.heap[i * 2 + 1]):
        #     # left = self.heap[i*2]
        #     # right = self.heap[i * 2 + 1]
        #
        #     if self.heap[i*2] > self.heap[i * 2 + 1]:
        #         self.heap[i] = self.heap[i*2]
        #         i = i * 2
        #     else:
        #         self.heap[i] = self.heap[i * 2 + 1]
        #         i = i * 2 + 1
        #
        # if i * 2 == self.get_size() and item <= self.heap[i*2]:
        #     self.heap[i] = self.heap[i*2]
        #     i = i * 2
        # self.heap[i] = item


        # '''where the parameter i is an index in the heap and perc_up moves the element stored
        # at that location to its proper place in the heap rearranging elements as it goes.'''
    def perc_up(self, i):
        iteam = self.heap[i]

        while i//2 > 0 and self.heap[i] >= self.heap[i//2]:
              self.heap[i] = self.heap[i//2]
              i = i // 2

        self.heap[i] = iteam

    # '''perform heap sort on input alist in ascending order
    #         This method will discard the current contents of the heap, build a new heap using
    #         the items in alist, then mutate alist to put the items in ascending order'''
    def heap_sort_ascending(self, alist):
        self.heap = []
        self.build_heap(alist)
        while self.get_size() > 0:
            alist[self.get_size()] = self.dequeue()





