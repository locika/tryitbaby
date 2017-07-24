"""
This program tests the A(rea) and V(olume) of a cube
"""
import unittest
import sphereprogram

class MyTestCase(unittest.TestCase):
    def test_positive(self):
        self.assertEqual( "The V(olume) of the sphere is: 33,49 The A(rea) of the sphere is: 50,24",sphereprogram.sphere(2))
    def test_negative(self):
        self.assertEqual("The input parameter must be positive", sphereprogram.sphere(-1))
    def test_zero(self):
        self.assertEqual("The input parameter must be positive", sphereprogram.sphere(0))
    def test_string(self):
        self.assertEqual("The input cannot be converted to integer", sphereprogram.sphere("asd"))

if __name__ == '__main__':
unittest.main()
