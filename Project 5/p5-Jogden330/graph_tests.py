import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])

        # vert1 = Vertex('v1')
        # vert1.adjacent_to = ['v2', 'v3', 'v4', 'v5']
        # vert2 = g.get_vertex('v1')
        # self.assertEqual(vert2.id, vert1.id)
        # self.assertEqual(vert2.adjacent_to, vert1.adjacent_to)
        self.assertFalse(g.get_vertex('cats'))
        
    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())

    def test_3(self):
        g = Graph('test3.txt')
        self.assertEqual(g.conn_components(), [['v01', 'v02', 'v03', 'v04', 'v05'], ['v06', 'v07', 'v08', 'v09'],['v10', 'v11', 'v12', 'v13']])
        self.assertTrue(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['v01', 'v02', 'v03', 'v04', 'v05', 'v06', 'v07', 'v08', 'v09','v10', 'v11', 'v12', 'v13'])

    def test_4(self):
        g = Graph('test4.txt')
        self.assertEqual(g.conn_components(), [['v01', 'v02', 'v03', 'v04', 'v05']])
        self.assertFalse(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['v01', 'v02', 'v03', 'v04', 'v05'])

    def test_05(self):
        g = Graph('test5.txt')
        self.assertEqual(g.conn_components(), [['v01', 'v02', 'v03', 'v04'], ['v06', 'v07', 'v08']])
        self.assertFalse(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['v01', 'v02', 'v03', 'v04', 'v06', 'v07', 'v08'])

    def test_06(self):
        g = Graph('test6.txt')
        self.assertEqual(g.conn_components(), [['v01', 'v02', 'v03', 'v04']])
        self.assertTrue(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['v01', 'v02', 'v03', 'v04'])

    def test_07(self):
        g = Graph('test7.txt')
        self.assertEqual(g.conn_components(), [['f01', 'f02', 'f03', 'f04', 'f05'],
         ['f06', 'f07', 'f08', 'f09'],
         ['f10', 'f11', 'f12', 'f13'],
         ['v01', 'v02', 'v03', 'v04', 'v05'],
         ['v06', 'v07', 'v08', 'v09'],
         ['v10', 'v11', 'v12', 'v13']])
        self.assertTrue(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['f01', 'f02', 'f03', 'f04', 'f05', 'f06', 'f07', 'f08', 'f09', 'f10', 'f11', 'f12', 'f13', 'v01',
         'v02', 'v03', 'v04', 'v05', 'v06', 'v07', 'v08', 'v09', 'v10', 'v11', 'v12', 'v13'])

    def test_08(self):
        g = Graph('test8.txt')
        self.assertEqual(g.conn_components(), [['a01', 'a02', 'a03', 'a04', 'a05'],
                                                 ['a06', 'a07', 'a08', 'a09'],
                                                 ['a10', 'a11', 'a12', 'a13'],
                                                 ['c01', 'c02', 'c03', 'c04', 'c05'],
                                                 ['c06', 'c07', 'c08', 'c09'],
                                                 ['c10', 'c11', 'c12', 'c13'],
                                                 ['f01', 'f02', 'f03', 'f04', 'f05'],
                                                 ['f06', 'f07', 'f08', 'f09'],
                                                 ['f10', 'f11', 'f12', 'f13'],
                                                 ['g01', 'g02', 'g03', 'g04', 'g05'],
                                                 ['g06', 'g07', 'g08', 'g09'],
                                                 ['g10', 'g11', 'g12', 'g13'],
                                                 ['n01', 'n02', 'n03', 'n04', 'n05'],
                                                 ['n06', 'n07', 'n08', 'n09'],
                                                 ['n10', 'n11', 'n12', 'n13'],
                                                 ['r01', 'r02', 'r03', 'r04', 'r05'],
                                                 ['r06', 'r07', 'r08', 'r09'],
                                                 ['r10', 'r11', 'r12', 'r13'],
                                                 ['t01', 't02', 't03', 't04', 't05'],
                                                 ['t06', 't07', 't08', 't09'],
                                                 ['t10', 't11', 't12', 't13'],
                                                 ['v01', 'v02', 'v03', 'v04', 'v05'],
                                                 ['v06', 'v07', 'v08', 'v09'],
                                                 ['v10', 'v11', 'v12', 'v13']])
        self.assertTrue(g.is_bipartite())

    def test_09(self):
            g = Graph('test9.txt')
            self.assertFalse(g.is_bipartite())

    def test_10(self):
            g = Graph('test10.txt')
            self.assertEqual(g.conn_components(), [['v01', 'v02']])
            self.assertTrue(g.is_bipartite())
            self.assertEqual(g.get_vertices(),['v01', 'v02'])

    def test_11(self):
        g = Graph('test11.txt')
        self.assertEqual(g.conn_components(), [['v01', 'v02', 'v03', 'v04', 'v05']])
        self.assertTrue(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['v01', 'v02', 'v03', 'v04', 'v05'])

    def test_12(self):
        g = Graph('test12.txt')
        self.assertEqual(g.conn_components(), [['v01', 'v02', 'v03', 'v04', 'v05', 'v06', 'v07']])
        self.assertFalse(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['v01', 'v02', 'v03', 'v04', 'v05', 'v06', 'v07'])

if __name__ == '__main__':
   unittest.main()
