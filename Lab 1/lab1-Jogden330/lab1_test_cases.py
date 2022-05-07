    # CPE 202 Lab 1 Test Cases

import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_01(self):
        tlist = [1, 2, 3]
        self.assertEqual(max_list_iter(tlist), 3)
        tlist = [0, 2, 3]
        self.assertEqual(max_list_iter(tlist), 3)
        tlist = [0, -2, -2]
        self.assertEqual(max_list_iter(tlist), 0)
        tlist = [0, 9, 9]
        self.assertEqual(max_list_iter(tlist), 9)
        tlist = [0]
        self.assertEqual(max_list_iter(tlist), 0)
        tlist = [0, 1, 2, 3, 4, 5, 6, 9, 7, 8]
        self.assertEqual(max_list_iter(tlist), 9)



    def test_max_list_02(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        intlist = []
        self.assertEqual(max_list_iter(intlist), None)



    def test_reverse(self):
        intlist = [1, 2, 3]
        revlist = reverse_list(intlist)
        self.assertEqual(revlist, [3, 2, 1])
        self.assertEqual(intlist, [1, 2, 3])
        intlist = [3]
        revlist = reverse_list(intlist)
        self.assertEqual(revlist, [3])
        self.assertEqual(intlist, [3])
        intlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_list(intlist)
        intlist = []
        revlist = reverse_list(intlist)
        self.assertEqual(intlist, [])
        self.assertEqual(revlist, [])

    def test_reverse_mutate(self):
        intlist = [1, 2, 3]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist, [3, 2, 1])
        intlist = [3]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist, [3])
        intlist = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        intlist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        intlist = []
        self.assertEqual(reverse_list_mutate(intlist), None)
        intlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_list_mutate(intlist)


    def test_reverse_rec(self):
        intlist = [1, 2, 3]
        self.assertEqual(reverse_rec(intlist),[3, 2, 1])
        self.assertEqual(intlist,[1, 2, 3])
        intlist = [3]
        self.assertEqual(reverse_rec(intlist), [3])
        self.assertEqual(intlist, [3])
        intlist = [1, 2, 3, 4, 5, 6]
        self.assertEqual(reverse_rec(intlist), [6, 5, 4, 3, 2, 1])
        self.assertEqual(intlist, [1, 2, 3, 4, 5, 6])
        intlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(intlist)
        intlist = []
        self.assertEqual(reverse_rec(intlist), [])
        self.assertEqual(intlist, [])

if __name__ == "__main__":
        unittest.main()