import unittest
from binary_search_tree import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.tree_height(), None)
        self.assertTrue(bst.is_empty())
        self.assertFalse(bst.search(10))
        self.assertEqual(bst.find_min(), None)
        self.assertEqual(bst.find_max(), None)
        self.assertEqual(bst.level_order_list(), [])
        bst.insert(10, 'stuff')
        bst.insert(5, 'cats')
        bst.insert(6, 'Dogs')
        bst.insert(4, 'Batman')
        bst.insert(20, 'SpiderMan')
        self.assertEqual(bst.find_max(), (20, 'SpiderMan'))
        bst.insert(20, 'SpiderMan But from the future')
        self.assertEqual(bst.find_max(), (20, 'SpiderMan But from the future'))
        bst.insert(25, 'Other words')
        self.assertEqual(bst.find_max(), (25, 'Other words'))
        self.assertTrue(bst.search(5))
        self.assertFalse(bst.search(3))
        self.assertTrue(bst.search(20))
        self.assertFalse(bst.search(21))
        self.assertFalse(bst.search(100))
        self.assertEqual(bst.find_min(), (4, 'Batman'))
        self.assertEqual(bst.inorder_list(), [4, 5, 6, 10, 20, 25])
        self.assertEqual(bst.preorder_list(), [10, 5, 4, 6, 20, 25])
        self.assertEqual(bst.tree_height(), 2)
        bst.insert(26, 'now biger')
        self.assertEqual(bst.tree_height(), 3)
        # self.assertEqual(bst.inorder_list(), [10])

        self.assertEqual(bst.level_order_list(), [10, 5, 20, 4, 6, 25, 26])

if __name__ == '__main__': 
    unittest.main()
