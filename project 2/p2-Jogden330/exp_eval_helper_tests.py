# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *
from stack_array import Stack

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
        self.assertAlmostEqual(postfix_eval("3 5 -"), -2)
        self.assertAlmostEqual(postfix_eval("3 5 *"), 15)
        self.assertAlmostEqual(postfix_eval("3 5 /"), 0.6)
        self.assertAlmostEqual(postfix_eval("3 5 **"), 243)
        self.assertAlmostEqual(postfix_eval("4 1 >>"), 2)
        self.assertAlmostEqual(postfix_eval("4 1 <<"), 8)


    def test_postfix_eval_03(self):
         with self.assertRaises(ValueError):
             postfix_eval("3 0 /")
         try:
             postfix_eval("4 +")
             self.fail()
         except PostfixFormatException as e:
             self.assertEqual(str(e), "Insufficient operands")
         try:
             postfix_eval("4 -")
             self.fail()
         except PostfixFormatException as e:
             self.assertEqual(str(e), "Insufficient operands")
         try:
             postfix_eval("4 *")
             self.fail()
         except PostfixFormatException as e:
             self.assertEqual(str(e), "Insufficient operands")
         try:
             postfix_eval("4 /")
             self.fail()
         except PostfixFormatException as e:
             self.assertEqual(str(e), "Insufficient operands")
         try:
             postfix_eval("4 **")
             self.fail()
         except PostfixFormatException as e:
             self.assertEqual(str(e), "Insufficient operands")
         try:
            postfix_eval("4 >>")
            self.fail()
         except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")
         try:
             postfix_eval("4 <<")
             self.fail()
         except PostfixFormatException as e:
             self.assertEqual(str(e), "Insufficient operands")

         try:
             postfix_eval("4 1.5 >>")
             self.fail()
         except PostfixFormatException as e:
             self.assertEqual(str(e), "Illegal bit shift operand")
         try:
             postfix_eval("4 1.5 <<")
             self.fail()
         except PostfixFormatException as e:
             self.assertEqual(str(e), "Illegal bit shift operand")
         try:
             postfix_eval("3  3 / 1 >>")
             self.fail()
         except PostfixFormatException as e:
             self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")
        try:
            postfix_eval("")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Empty input")
        try:
            postfix_eval("3 3 3 - ")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_05(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_06(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")



class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        with self.assertRaises(IndexError):
            stack.peek()
        self.assertTrue(stack.is_empty())
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), 0)
        self.assertEqual(stack.pop(), 0)
        with self.assertRaises(IndexError):
            stack.pop()
        stack.push(None)
        self.assertEqual(stack.pop(), None)
        stack.push(0)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        with self.assertRaises(IndexError):
            stack.push(5)
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), 0)




if __name__ == "__main__":
    unittest.main()
