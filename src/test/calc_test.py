import unittest
from main import Calc

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = Calc()
        self.calc.num1 = 10
        self.calc.num2 = 5
    
    def test_plus_works(self):
        
        self.assertEqual(self.calc.plus(),15)

    def test_minus_works(self):
        self.assertEqual(self.calc.minus(),5)
    
    def test_devide_works(self):
        self.assertEqual(self.calc.devide(),2)
    
    def test_multiply_works(self):
        self.assertEqual(self.calc.multiply(),50)