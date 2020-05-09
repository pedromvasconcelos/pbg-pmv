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
        self.y = [-1,-2,-3,-4]
          
    def testAdd(self):
        result = [0, 0, 0, 0]
        self.assertEqual(self.calc.add(self.x,self.y),result)
 
       
if __name__ == "__main__":
    unittest.main()      