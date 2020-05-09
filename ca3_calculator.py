# -*- coding: utf-8 -*-
"""
Created on May 2020
for B8IT105 CA3
@author: pmesquit
"""

class calculator:
    
    def __init__(self):
       self.x = []
       self.y = []

    def setx(self, x):
        self.x = x
        
    def setny(self, y):
        self.y = y
                
    def add(self, x, y):
        add = lambda x, y: x + y
        return list(map(add,x,y))
    
