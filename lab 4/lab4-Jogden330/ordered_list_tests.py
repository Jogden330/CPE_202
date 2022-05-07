import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        t_list.add(10)
        self.assertFalse(t_list.add(10))

        self.assertFalse(t_list.is_empty())
        self.assertTrue(t_list.add(8))
        self.assertEqual(t_list.python_list(), [8, 10])
        self.assertTrue(t_list.add(9))
        self.assertEqual(t_list.python_list(), [8, 9, 10])
        self.assertEqual(t_list.size(), 3)
        self.assertFalse(t_list.remove(2))
        self.assertTrue(t_list.remove(9))
        self.assertEqual(t_list.python_list(), [8, 10])
        self.assertEqual(t_list.index(10), 1)
        self.assertEqual(t_list.index("cats"), None)
        self.assertEqual(t_list.pop(0), 8)
        self.assertTrue(t_list.add(9))
        self.assertTrue(t_list.add(7))
        self.assertEqual(t_list.pop(1), 9)
        self.assertEqual(t_list.python_list(), [7, 10])
        with self.assertRaises(IndexError):
            t_list.pop(100)
        with self.assertRaises(IndexError):
            t_list.pop(-100)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.search("cats"))
        self.assertEqual(t_list.python_list_reversed(), [10, 7])
        self.assertTrue(t_list.remove(10))
        self.assertEqual(t_list.python_list_reversed(), [7])
        self.assertTrue(t_list.remove(7))
        self.assertTrue(t_list.is_empty())
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)
        t_list.add("D")
        t_list.add("A")
        t_list.add("F")
        t_list.add("B")
        t_list.add("Z")
        self.assertEqual(t_list.python_list(), ["A", "B", "D", "F", "Z"])
        self.assertEqual(t_list.python_list_reversed(), ["Z", "F", "D", "B", "A"])

if __name__ == '__main__': 
    unittest.main()
