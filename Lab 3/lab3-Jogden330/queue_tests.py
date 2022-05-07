import unittest
from queue_array import Queue
# from queue_linked import Queue

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        self.assertTrue(q.is_empty())
        q.enqueue(0)
        self.assertFalse(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 0)
        with self.assertRaises(IndexError):
            q.dequeue()
        q.enqueue(None)
        self.assertEqual(q.dequeue(), None)
        q.enqueue(0)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        with self.assertRaises(IndexError):
            q.enqueue(5)
        self.assertTrue(q.is_full())
        self.assertEqual(q.dequeue(), 0)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        q.enqueue("puppies")
        q.enqueue("are")
        q.enqueue("the")
        q.enqueue("best")
        q.enqueue("ever")
        self.assertEqual(q.dequeue(), "puppies")
        self.assertEqual(q.dequeue(), "are")
        self.assertEqual(q.dequeue(), "the")
        self.assertEqual(q.dequeue(), "best")
        self.assertEqual(q.dequeue(), "ever")

if __name__ == '__main__': 
    unittest.main()
