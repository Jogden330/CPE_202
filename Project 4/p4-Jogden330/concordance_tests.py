import unittest
import subprocess
from concordance import *


class TestList(unittest.TestCase):

    def test_empty(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("empty_file.txt")
        conc.write_concordance("empty_file_con.txt")
        err = subprocess.call("diff -wb empty_file_con.txt empty_file.txt", shell=True)
        self.assertEqual(err, 0)

    def test_01(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.stop_table.get_all_keys()
        # self.assertEqual(conc.stop_table.get_all_keys(), "cats")
        conc.load_concordance_table("file1.txt")
        conc.write_concordance("file1_con.txt")
        err = subprocess.call("diff -wb file1_con.txt file1_sol.txt", shell = True)
        self.assertEqual(err, 0)


    def test_02(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("file2_con.txt")
        err = subprocess.call("diff -wb file2_con.txt file2_sol.txt", shell = True)
        self.assertEqual(err, 0)


    def test_03(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("declaration.txt")
        conc.write_concordance("declaration_con.txt")
        err = subprocess.call("diff -wb declaration_con.txt declaration_sol.txt", shell = True)
        self.assertEqual(err, 0)

    def test_two_inaRow(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file1.txt")
        conc.write_concordance("right_twice_con.txt")
        err = subprocess.call("diff -wb right_twice_con.txt file1_sol.txt", shell=True)
        self.assertEqual(err, 0)
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("right_twice_con.txt")
        err = subprocess.call("diff -wb right_twice_con.txt file2_sol.txt", shell=True)
        self.assertEqual(err, 0)

    def test_two_inaRow_2(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("declaration.txt")
        conc.write_concordance("right_twice_con.txt")
        err = subprocess.call("diff -wb right_twice_con.txt declaration_sol.txt", shell=True)
        self.assertEqual(err, 0)
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("right_twice_con.txt")
        err = subprocess.call("diff -wb right_twice_con.txt file2_sol.txt", shell=True)
        self.assertEqual(err, 0)

    # def test_04(self):
        # conc = Concordance()
        # conc.load_stop_table("stop_words.txt")
        # conc.load_concordance_table("dictionary_a-c.txt")
        # conc.write_concordance("dictionary_a-c_con.txt")
        # err = subprocess.call("diff -wb dictionary_a-c_con.txt dictionary_a-c_sol.txt", shell = True)
        # self.assertEqual(err, 0)

    # def test_05(self):
    #     conc = Concordance()
    #     # conc.load_stop_table("stop_words.txt")
    #     conc.load_concordance_table("file_the.txt")
    #     conc.write_concordance("file_the_con.txt")
    #     err = subprocess.call("diff -wb file_the_con.txt file_the_sol.txt", shell = True)
    #     self.assertEqual(err, 0)
    # #
    # def test_06(self):
    #     conc = Concordance()
    #     conc.load_stop_table("stop_words.txt")
    #     conc.load_concordance_table("War_And_Peace.txt")
    #     conc.write_concordance("War_And_Peace_con.txt")
    #     err = subprocess.call("diff -wb War_And_Peace_con.txt War_And_Peace_sol.txt", shell = True)
    #     self.assertEqual(err, 0)

    def test_FileNOtFound(self):
        conc = Concordance()
        with self.assertRaises(FileNotFoundError):  # used to check for exception
            conc.load_concordance_table("CATS")

    def test_FileNOtFound2(self):
        conc = Concordance()
        with self.assertRaises(FileNotFoundError):  # used to check for exception
            conc.load_stop_table("CATS")

if __name__ == '__main__':
    unittest.main()
