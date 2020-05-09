# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:22:21 2020

@author: pmesquit
"""
from ca3_calculator import calculator

calc = calculator()

def main():
    x = [1,2,3]
    y = [2,2,3]
    print(calc.add(x,y))
    
main()