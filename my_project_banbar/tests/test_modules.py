import sys, os 
import unittest

testdir = os.path.dirname(__file__)
srcdir = '../../'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

from my_project_banbar.add_subtract import * 
from my_project_banbar.advanced import * 

class TestFunctions(unittest.TestCase):
   
    def setUp(self):        
        # Polygon 1: Simple square - CCW - total must be 360               
        self.num1 = 50
        self.num2 = 2
        self.p1 = (3,6)
        self.poly1 = Polygon([(0, 0), (5, 0), (5, 5), (0, 5), (0, 0)])   
    
    def test_multiply(self):
        self.assertEqual(multiply_two_numbers(self.num1, self.num2),100)
    
    def test_distance(self):
        self.assertEqual(distance_between_point_polygon(self.p1, self.poly1), 1)
    
    def test_super_f3(self):
        self.assertEqual(super_f3(self.num2), 8)
    
    def test_super_f4(self):
        self.assertEqual(super_f4(self.num2), 16)
    
    def test_super_f5(self):
        self.assertEqual(super_f5(self.num2), 32)
    
    def test_super_f6(self):
        self.assertEqual(super_f6(self.num2), 64)
    

        

if __name__ == '__main__':
    unittest.main()