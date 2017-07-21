"""
This program tests the A(rea) and V(olume) of a cube
"""
import unittest
import cubeprogram

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual( "A kocka térfogata: 8 A kocka felülete: 24", cubeprogram.cube(2))
        self.assertEqual("Az oldalhossznak pozitív számnak kell lennie", cubeprogram.cube(-1))
        self.assertEqual("A bemenet nem alakítható át egész számmá", cubeprogram.cube("asd"))
        print("Pass")
if __name__ == '__main__':
    unittest.main()
