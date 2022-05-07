import unittest
import rec_list

# Starter test cases - write more!

class TestRecList(unittest.TestCase):

    # def test_first1(self):
    #     strlist = rec_list.Node("49ers", rec_list.Node("Abc", rec_list.Node("cats", None)))
    #     self.assertEqual(rec_list.first_string(strlist), "49ers")
    #     strlist = rec_list.Node("junk", rec_list.Node("49ers", rec_list.Node("cats", None)))
    #     self.assertEqual(rec_list.first_string(strlist), "49ers")
    #     strlist = rec_list.Node(None, None)
    #     self.assertEqual(rec_list.first_string(strlist), None)
    #
    # def test_split1(self):
    #     strlist = rec_list.Node("xyz", rec_list.Node("Abc", rec_list.Node("49ers", None)))
    #     self.assertEqual(rec_list.split_list(strlist), (rec_list.Node('Abc', None), rec_list.Node('xyz', None), rec_list.Node('49ers', None)))
    #
    # def test_split2(self):
    #     strlist = rec_list.Node("Yellow", rec_list.Node("abc", rec_list.Node("$7.25", rec_list.Node("lime", rec_list.Node("42", rec_list.Node("Ethan", None))))))
    #     self.assertEqual(rec_list.split_list(strlist), (rec_list.Node('abc', rec_list.Node("Ethan", None)), rec_list.Node('Yellow', rec_list.Node("lime", None)), rec_list.Node('$7.25', rec_list.Node("42", None))))
    #
    # def test_split3(self):
    #     strlist = rec_list.Node(None, None)
    #     self.assertEqual(rec_list.split_list(strlist),(None, None, None))
    #
    #     strlist = rec_list.Node("Abc", rec_list.Node("49ers", None))
    #     self.assertEqual(rec_list.split_list(strlist), (rec_list.Node('Abc', None), None, rec_list.Node('49ers', None)))
    #
    # def test_repr(self):
    #     strlist = rec_list.Node("49ers", rec_list.Node("Abc", rec_list.Node("cats", None)))
    #     self.assertEqual(repr(strlist),"Node('49ers', Node('Abc', Node('cats', None)))")
    #
    def test_add_str(strlist, s)
        strlist = rec_list.Node("49ers", rec_list.Node("Abc", rec_list.Node("cats", None)))
        self.assertEqual(rec_list.add_str(strlist, s), ['49erss', 'ABCs', 'Catss'])
        strlist = none
        self.assertEqual(rec_list.split_list(strlist,s), (None))
if __name__ == "__main__":
        unittest.main()