import unittest
import perm_lex

# Starter test cases - write more!

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])
        self.assertEqual(perm_lex.perm_gen_lex('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(perm_lex.perm_gen_lex('ago'), ['ago', 'aog', 'gao', 'goa', 'oag', 'oga'])
        self.assertEqual(perm_lex.perm_gen_lex('abcd'), ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad','bcda', 'bdac', 'bdca', 'cabd','cadb','cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca','dcab','dcba'])
        self.assertEqual(perm_lex.perm_gen_lex(''), [])
        self.assertEqual(perm_lex.perm_gen_lex('a'), ['a'])

if __name__ == "__main__":
        unittest.main()



