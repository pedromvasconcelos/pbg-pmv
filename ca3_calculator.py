# -*- coding: utf-8 -*-
"""
Created on May 2020
for B8IT105 CA3
@author: pmesquit
"""
from functools import reduce

class calculator:
    
    def __init__(self):
       self.x = []
       self.y = []
       self.z = []

    def setx(self, x):
        self.x = x
        
    def sety(self, y):
        self.y = y

    def setz(self, z):
        self.z = z
    
    def setn(self, n):
        self.n = n

# Function to add two lists
              
    def add(self, x, y):
        add = lambda x, y: x + y
        return list(map(add,x,y))

# Function to subtract two lists    
    def subtract(self, x, y):
        sub = lambda x, y: x - y
        return list(map(sub,x,y))
    
# Function to multiply    
    def multiply(self, x, y):
        mult = lambda x, y: x * y
        return list(map(mult,x,y))
    
#Function x power of y
    def power(self, x, y):
        power = lambda x,y: x ** y
        return list(map(power,x,y))
    
#Function to divide    
    def divide(self, x, y):
        if 0 in y:
            print('Error: Not possible to divide by 0')
            return None
        else:
            div = lambda x, y: x/y
            return list(map(div,x,y))
        
#Function to return max value        
    def max(self, x):
        max = lambda a,b: a if (a>b) else b
        return reduce(max, x)
    
#Function to return max value        
    def min(self, x):
        min = lambda a,b: a if (a<b) else b
        return reduce(min, x)
    
#Function to factorial of a list
    def factorial(self,x):
        fact = lambda x: None if x < 0 else x-1 + abs(x-1) and fact(x-1)*x or 1
        return list(map(fact,x))  

#Function to discover primes
    def primes(self,x):
        for i in range(2,10):
            prime = lambda x: x == i or x % i
            return list(filter(prime,x))        

#Function to calculate square roots
    def sqr(self,x):
        sqr = lambda x: x**(0.5)
        return list(map(sqr,x))      
    
#Function to fid pythagorean triplets withn a n range
    def pythagorean(self, n):
        pyt = [(x,y,z) for x in range(1,n) for y in range(x,n) for z in range(y,n) if x**2 + y**2 == z**2]
        return pyt

#Function to find possible side dimentions for a given z area (rectangle) from a given n range of values  
    def sides(self, n, z):
        pyt = [(x,y) for x in range(1,n) for y in range(x,n) if x*y == z]
        return pyt
    
#Function for operations with two lists and for main program
    def optwo(self,op,x,y):
        if op == '+':
            value = self.add(x, y)
        elif op == '-':
            value = self.subtract(x, y)
        elif op == '*':
            value = self.multiply(x, y)
        elif op == '/':
            value = self.divide(x, y)
        elif op == '**':
            value = self.power(x, y)
        return print('The Result is: ', value)
    
#Function for operations with two lists and for main program
    def opone(self,op,x):
        if op == 'sqr':
            value = self.sqr(x)
        elif op == '!':
            value = self.factorial(x)
        elif op == 'max':
            value = self.max(x)
        elif op == 'min':
            value = self.min(x)
        elif op == 'prim':
            value = self.primes(x)
        return print('The Result is: ', value)
       
