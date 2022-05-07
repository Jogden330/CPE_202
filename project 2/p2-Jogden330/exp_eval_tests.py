# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
        self.assertAlmostEqual(postfix_eval("3 5 -"), -2)
        self.assertAlmostEqual(postfix_eval("3 5 *"), 15)
        self.assertAlmostEqual(postfix_eval("3 5 /"), 0.6)
        self.assertAlmostEqual(postfix_eval("3 5 **"), 243)
        self.assertAlmostEqual(postfix_eval("4 1 >>"), 2)
        self.assertAlmostEqual(postfix_eval("4 1 <<"), 8)

    def test_postfix_eval_02(self):
        self.assertAlmostEqual(postfix_eval("6 4 3 + 2 - * 6 /"), 5)
        self.assertAlmostEqual(postfix_eval("5 2 4 * + 7 2 - 4 6 2 / 2 - * + 4 - +"), 18)
        self.assertAlmostEqual(postfix_eval("5 1 2 + 4 ** + 3 -"), 83)

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
         try:
             postfix_eval("3  3 / 1 <<")
             self.fail()
         except PostfixFormatException as e:
             self.assertEqual(str(e), "Illegal bit shift operand")
         try:
             postfix_eval("2.0 1 <<")
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

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("( 6 - 3 ) + 6"), "6 3 - 6 +")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 )"), "3 4 2 * 1 5 - / +")
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 )")), 1)
        self.assertEqual(infix_to_postfix("( ( 1 + 3 ) - 3 ) + 5"), "1 3 + 3 - 5 +")
        self.assertEqual(infix_to_postfix("1 + 2 + 3 + 4 + 5"), "1 2 + 3 + 4 + 5 +")
        self.assertEqual(infix_to_postfix("(  ( 1 * 2  ) * 4 ) * 5"), "1 2 * 4 * 5 *")
        self.assertEqual(infix_to_postfix("5 ** 2 ** 3 "), "5 2 3 ** **")
        self.assertEqual(infix_to_postfix("1 - 2 ** 2"), "1 2 2 ** -")
        self.assertEqual(infix_to_postfix("1 - 2 ** 2"), "1 2 2 ** -")
        self.assertEqual(infix_to_postfix("3 + 4 * 2  /  5  ** 2 ** 3"), "3 4 2 * 5 2 3 ** ** / +")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) * 9"), "3 4 2 * 1 5 - / 9 * +")
        self.assertEqual(infix_to_postfix("5 >> ( ( 4 ** 2 ) >> 3 ) + 8 >> 3 ** 4"), "5 4 2 ** 3 >> >> 8 3 >> 4 ** +")

    def test_prefix_to_postfix(self):

        self.assertEqual(prefix_to_postfix("+ 3 3"), "3 3 +")
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

if __name__ == "__main__":
    unittest.main()
