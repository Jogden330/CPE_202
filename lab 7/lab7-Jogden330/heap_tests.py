import unittest
from heap import *

class TestHeap(unittest.TestCase):
    #     test_heap.build_heap([2, 9, 7, 6, 5, 8])
    #     self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])
    def test_01_enqueue(self):
        test_heap = MaxHeap(7)

        self.assertEqual(test_heap.get_capacity(), 7)
        insert = test_heap.enqueue(2)
        self.assertTrue(insert)
        insert = test_heap.enqueue(9)
        self.assertTrue(insert)
        insert = test_heap.enqueue(7)
        self.assertTrue(insert)
        insert = test_heap.enqueue(6)
        self.assertTrue(insert)
        insert = test_heap.enqueue(5)
        self.assertTrue(insert)
        insert = test_heap.enqueue(8)
        self.assertTrue(insert)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])
        insert = test_heap.enqueue(8)
        self.assertTrue(insert)
        insert = test_heap.enqueue(8)
        self.assertFalse(insert)
    def test_dequeue(self):
        test_heap = MaxHeap(7)

        insert = test_heap.enqueue(2)
        self.assertTrue(insert)
        insert = test_heap.enqueue(9)
        self.assertTrue(insert)
        insert = test_heap.enqueue(7)
        self.assertTrue(insert)
        insert = test_heap.enqueue(6)
        self.assertTrue(insert)
        insert = test_heap.enqueue(5)
        self.assertTrue(insert)
        insert = test_heap.enqueue(8)
        self.assertTrue(insert)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])
        self.assertEqual(test_heap.dequeue(), 9)

        self.assertEqual(test_heap.contents(), [8, 6, 7, 2, 5])
        self.assertEqual(test_heap.dequeue(), 8)

        self.assertEqual(test_heap.contents(), [7, 6, 5, 2])
        self.assertEqual(test_heap.dequeue(), 7)
        self.assertEqual(test_heap.contents(), [6, 2, 5])
        self.assertEqual(test_heap.dequeue(), 6)
        self.assertEqual(test_heap.contents(), [5 , 2])
        self.assertEqual(test_heap.dequeue(), 5)
        self.assertEqual(test_heap.contents(), [2])
        self.assertEqual(test_heap.dequeue(), 2)
        self.assertEqual(test_heap.contents(), [])
        self.assertEqual(test_heap.dequeue(), None)

    def test_init_capacity(self):
        test_heap = MaxHeap()
        self.assertEqual(test_heap.get_capacity(), 50)
        self.assertEqual(test_heap.contents(), [])
        self.assertEqual(test_heap.dequeue(), None)

    def test_is_empty(self):
        test_heap = MaxHeap(7)
        self.assertTrue(test_heap.is_empty())
        self.assertEqual(test_heap.peek(), None)
        self.assertEqual(test_heap.contents(), [])
        insert = test_heap.enqueue(2)
        self.assertEqual(test_heap.peek(), 2)
        self.assertTrue(insert)
        self.assertFalse(test_heap.is_empty())

    def test_04_build_heap(self):
        test_heap = MaxHeap(10)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_02_dequeue(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.dequeue(), 9)
        self.assertEqual(test_heap.get_size(), 5)
        self.assertEqual(test_heap.contents(), [8, 6, 7, 2, 5])

    def test_03_heap_contents(self):
        test_heap = MaxHeap(8)
        self.assertEqual(test_heap.get_capacity(), 8)
        test_heap.build_heap([1, 2, 3])
        self.assertEqual(test_heap.contents(), [3, 2, 1])
        self.assertEqual(test_heap.get_capacity(), 8)

    def test_2_build_heap(self):
        test_heap = MaxHeap(10)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])
        self.assertEqual(test_heap.get_capacity(), 10)

    # def test_3_build_heap(self):
    #     test_heap = MaxHeap(10)
    #     test_heap.build_heap([6, 11, 24, 13, 37, 36, 16])
    #     self.assertEqual(test_heap.contents(), [37, 36, 24, 16, 13, 11, 6])

    # def test_build_heap_with_deque(self):
    #     test_heap = MaxHeap(10)
    #     test_heap.build_heap([6, 11, 24, 13, 37, 36, 16])
    #     self.assertEqual(test_heap.contents(), [37, 36, 24, 16, 13, 11, 6])

    def test_4_build_heap(self):
        test_heap = MaxHeap(10)
        test_heap.build_heap([10, 7, 8, 6, 15, 5, 3, 1, 2, 4])
        self.assertEqual(test_heap.contents(), [15, 10, 8, 6, 7, 5, 3, 1, 2, 4])

    def test_05_is_empty(self):
        test_heap = MaxHeap(5)
        self.assertTrue(test_heap.is_empty())
        self.assertEqual(test_heap.get_capacity(), 5)

    def test_06_is_full(self):
        test_heap = MaxHeap(2)
        built = test_heap.build_heap([1, 2, 3, 4, 5])
        self.assertTrue(test_heap.is_full())
        self.assertEqual(test_heap.get_capacity(), 5)

    def test_07_get_heap_cap(self):
        test_heap = MaxHeap(7)
        self.assertEqual(test_heap.get_capacity(), 7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.get_capacity(), 7)
        insert = test_heap.enqueue(10)
        self.assertEqual(test_heap.get_capacity(), 7)

    def test_08_get_size(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.get_size(), 6)

    def test_09_perc_down(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        test_heap.perc_down(1)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_10_perc_up(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        test_heap.perc_up(6)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_11_heap_sort_ascending(self):
        test_heap = MaxHeap()
        list1 = [2, 9, 7, 6, 5, 8]
        test_heap.heap_sort_ascending(list1)
        self.assertEqual(list1, [2, 5, 6, 7, 8, 9])


if __name__ == "__main__":
    unittest.main()
