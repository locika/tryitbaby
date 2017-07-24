"""
This program tests the A(rea) and V(olume) of a sphere
"""
import unittest
import sphereprogram
class Sphere(unittest.TestCase):
    def test_whole(self):
        self.assertEqual("The (T)erritory of the triangle is: 6, sphereprogram.sphere(3,4,5))
    def test_positive(self):
        self.assertEqual("The (T)erritory of the triangle is: 39.42, sphereprogram.sphere(12,12,23))
    def test_nottriange(self):
        self.assertEqual("The sum of two sides must be larger than the third., sphereprogram.sphere(5,10,15))        
    def test_negative(self):
        self.assertEqual("The input parameter must be positive", sphereprogram.sphere(-1,10,10))
    def test_zero(self):
        self.assertEqual("The input parameter must be positive", sphereprogram.sphere(0,0,0))
    def test_twonegative(self):
        self.assertEqual("The input parameter must be positive", sphereprogram.sphere(-5,-5,10))    
    def test_string(self):
        self.assertEqual("The input cannot be converted to integer", sphereprogram.sphere("asd"))

if __name__ == '__main__':
unittest.main()
