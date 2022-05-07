import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])
        nums = [10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 0)
        self.assertEqual(nums, [10])
        nums = []
        comps = selection_sort(nums)
        self.assertEqual(comps, 0)
        self.assertEqual(nums, [])
        nums = [6, 5, 3, 7, 8, 9, 2, 1, 4, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 45)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_simple2(self):
        nums = [23, 10]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])
        nums = [10]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 0)
        self.assertEqual(nums, [10])
        nums = []
        comps = insertion_sort(nums)
        self.assertEqual(comps, 0)
        self.assertEqual(nums, [])
        nums = [6, 5, 3, 7, 8, 9, 2, 1, 4, 10]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 26)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

if __name__ == '__main__': 
    unittest.main()
