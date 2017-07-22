"""
This program tests the A(rea) and V(olume) of a cube
"""
import unittest
import cubeprogram

class MyTestCase(unittest.TestCase):
    def test_positive(self):
        self.assertEqual( "The V(olume) of the cube is: 8 The A(rea) of the cube is: 24", cubeprogram.cube(2))
    def test_negative(self):
        self.assertEqual("The input parameter must be positive", cubeprogram.cube(-1))
    def test_zero(self):
        self.assertEqual("The input parameter must be positive", cubeprogram.cube(0))
    def test_string(self):
        self.assertEqual("The input cannot be converted to integer", cubeprogram.cube("asd"))
        print("Pass")
if __name__ == '__main__':
    unittest.main()
