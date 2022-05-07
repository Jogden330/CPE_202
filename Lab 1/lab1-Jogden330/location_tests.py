# CPE 202 Location Class Test Cases, Lab 1

import unittest
from location import *

class TestLocation(unittest.TestCase):

    def test_repr(self):
        loc = Location('SLO', 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")
    # Add more tests!
    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = Location("SLO", 34.2 + .1 + .1 + .1 + .1 + .1 + .1 + .1 + .1 + .1 + .1 + .1, -120.7)
        loc4 = loc1
        self.assertTrue(loc1 == loc1)
        self.assertFalse(loc2 == loc1)
        self.assertTrue(loc1 == loc3)
        self.assertTrue(loc1 == loc4)
        self.assertFalse(loc2 == loc4)
        self.assertFalse(loc2 == "cats")


    def test_int(self):

        loc1 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc1.name, "SLO")
        self.assertEqual(loc1.lat, 35.3)
        self.assertEqual(loc1.lon, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertTrue(loc2 == loc1)
        locations = [loc1, loc2]
        loc3 = "cats"
        self.assertTrue(loc1 in locations)
        self.assertTrue(loc2 in locations)
        self.assertFalse(loc3 in locations)


if __name__ == "__main__":
        unittest.main()
