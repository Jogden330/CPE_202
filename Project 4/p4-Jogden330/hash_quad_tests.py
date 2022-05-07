import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_horner_hash(self):
        ht = HashTable(7)
        self.assertEqual(ht.horner_hash("cat"), 98262)
        self.assertEqual(ht.horner_hash("catapults"), ht.horner_hash("catapulted"))


    def test_next_prime(self):
        ht = HashTable(7)
        self.assertEqual(ht.next_prime(19), 23)
        self.assertEqual(ht.next_prime(47), 53)
        self.assertEqual(ht.next_prime(0),2)
        self.assertEqual(ht.next_prime(2), 3)
        self.assertEqual(ht.next_prime(1019), 1021)
        self.assertEqual(ht.isPrime(-1), False)

    def test_while_loops(self):
        ht = HashTable(7)
        ht.hash_table = [(0,None), (1,None), (2,None), (3,None), (4,None), (5,None), (6,None)]
        self.assertEqual(ht.get_index("dog"), None)
        self.assertEqual(ht.in_table("dog"), False)
        self.assertEqual(ht.get_value("dog"), None)

    def test_01a(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        ht.insert("cat", 2)
        ht.insert("cat", 0)
        ht.insert("cat", 7)
        ht.insert("cat", 7)
        # self.assertEqual(ht.table_size, 1)
        self.assertEqual(ht.get_table_size(), 7)
        self.assertEqual(ht.get_num_items(), 1)

    def test_01b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)

    def test_01c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)
        self.assertEqual(ht.get_num_items(), 1)

    def test_01d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_01e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)
        self.assertEqual(ht.in_table("dogs"), False)
        self.assertEqual(ht.get_num_items(), 1)
        ht.insert("catapults", 9)
        ht.insert("catapulted", 10)
        self.assertEqual(ht.in_table("catapults"), True)
        self.assertEqual(ht.in_table("catapulted"), True)
        self.assertEqual(ht.get_num_items(), 3)

    def test_01f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), 5)
        ht.insert("cat", 17)
        self.assertEqual(ht.get_value("cat"), 17)
        self.assertEqual(ht.get_value("dogs"), None)
        ht.insert("catapults", 9)
        ht.insert("catapulted", 10)
        self.assertEqual(ht.get_value("catapults"), 9)
        self.assertEqual(ht.get_value("catapulted"), 10)

    def test_01g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)
        self.assertEqual(ht.get_index("dog"), None)
        ht.insert("catapults")
        ht.insert("catapulted")
        self.assertEqual(ht.get_index("catapults"), 6)
        self.assertEqual(ht.get_index("catapulted"), 0)

    def test_02(self):
        ht = HashTable(7)
        ht.insert("a", 0)
        self.assertEqual(ht.get_index("a"), 6)
        ht.insert("h", 0)
        self.assertEqual(ht.get_index("h"), 0)
        ht.insert("o", 0)
        self.assertEqual(ht.get_index("o"), 3)
        ht.insert("v", 0) # Causes rehash
        self.assertEqual(ht.get_index("a"), 12)
        self.assertEqual(ht.get_index("h"), 2)
        self.assertEqual(ht.get_index("o"), 9)
        self.assertEqual(ht.get_index("v"), 16)
        self.assertEqual(ht.get_num_items(), 4)

    def test_03(self):
        ht = HashTable(7)
        ht.insert("catapults")
        ht.insert("catapulted")
        ht.insert("catapulting")
        self.assertEqual(ht.get_index("catapults"), 6)
        self.assertEqual(ht.get_index("catapulted"), 0)
        self.assertEqual(ht.get_index("catapulting"), 3)
        ht.insert("catapultinged")
        self.assertEqual(ht.get_index("catapults"), 16)
        self.assertEqual(ht.get_index("catapulted"), 7)
        self.assertEqual(ht.get_index("catapulting"), 11)
        self.assertEqual(ht.get_index("catapultinged"), 8)
        self.assertEqual(ht.get_all_keys(), ['catapulted', 'catapultinged', 'catapulting', 'catapults'] )
        self.assertTrue(ht.in_table("catapultinged"))
        self.assertFalse(ht.in_table("dog"))
        self.assertEqual(ht.get_num_items(), 4)


    def test_04(self):
        ht = HashTable(7)
        ht.insert("cat", [93, 32, 5])
        self.assertEqual(ht.get_value("cat"), [93, 32, 5])
        value = ht.get_value("cat")
        value.append("dogs")
        self.assertEqual(ht.get_value("cat"), [93, 32, 5, "dogs"])
        self.assertEqual(value[-1], "dogs")
        self.assertEqual(ht.get_value("cat")[-2],  5)
        value.append("cats")
        self.assertEqual(ht.get_value("cat"), [93, 32, 5, "dogs", "cats"])

if __name__ == '__main__':
   unittest.main()
