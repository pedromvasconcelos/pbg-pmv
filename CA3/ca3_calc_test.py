# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:50:32 2020

@author: pmesquit
"""

import unittest

from ca3_calculator import calculator

calc = calculator()

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = calc
        self.x = [1,2,3,4]
        self.y = [1,2,3,4]
          
    def testAdd(self):
        result = [2, 4, 6, 8]
        self.assertEqual(self.calc.add(self.x,self.y),result)
    
    def testSubtract(self):
        result = [0, 0, 0, 0]
        self.assertEqual(self.calc.subtract(self.x,self.y),result) 
    
    def testMultiply(self):
        result = [1, 4, 9, 16]
        self.assertEqual(self.calc.multiply(self.x,self.y),result)
    
    def testDivide(self):
        result = [1, 1, 1, 1]
        self.assertEqual(self.calc.divide(self.x,self.y),result)

    def testDivisionByZero(self):
        self.assertEqual(self.calc.divide(self.x,[0,1,1,0]),None)
    
    def testPower(self):
        result = [1,4,27,256]
        self.assertEqual(self.calc.power(self.x,self.y),result)
    
    def testMax(self):
        result = 4
        self.assertEqual(self.calc.max(self.x),result)

    def testMin(self):
        result = 1
        self.assertEqual(self.calc.min(self.x),result)
        
    def testFactorial(self):
        result = [1,2,6,24]
        self.assertEqual(self.calc.factorial(self.x),result)
    
    def testPrimes(self):
        result = [1,2,3]
        self.assertEqual(self.calc.primes(self.x),result)
        
    def testSqr(self):
        result = [1.0, 1.4142135623730951, 1.7320508075688772, 2.0]
        self.assertEqual(self.calc.sqr(self.x),result)
        
    def testSides(self):
        result = [(10, 30), (12, 25), (15, 20)]
        self.assertEqual(self.calc.sides(50,300),result)
        
    
if __name__ == "__main__":
    unittest.main()      