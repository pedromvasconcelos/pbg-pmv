# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:22:21 2020

@author: pmesquit
"""
from ca3_calculator import calculator

calc = calculator()

def menu():
    print('*****Calculator using lists*****\n'
          'Options:\n'
          '+     - for addition of two lists(x+y)\n'
          '-     - for subtraction of two lists(x-y)\n'
          '*     - for multiplication of two lists(x*y)\n'
          '/     - for division of two lists (x/y)\n'
          '**    - for power of two lists (x^y)\n'
          'sqr   - for Square root of 1 list (sqrt(x))\n'
          '!     - for factorial of 1 lists (x!)\n'
          'max   - to find the max value of 1 list\n'
          'min   - to find the min value of 1 list\n'
          'prim  - to find the prime number inside of 1 list\n'
          'pyt   - to generate pythagorean triples\n'
          'sides - to find sides of rectangle of given area')

def main():
    cont = 'Y'
    while cont == 'Y':
        menu()
        op = input('Please enter the desired math operation to be completed: ').lower()
        if op == '+' or op == '-' or op == '*' or op == '/' or op == '**':
            x = list(map(float, input("Enter the list numbers separated by space : ").strip().split()))
            calc.setx(x)
            y = list(map(float, input("Enter the 2nd list of numbers separated by space : ").strip().split()))
            calc.sety(y)
            calc.optwo(op,x,y)
        elif op == 'pyt':
            n = int(input('Enter number of range to generate Pythagorean Tryplets: '))
            print(calc.pythagorean(n))
        elif op == 'sides':
            z = int(input('Enter area of rectangle: '))
            n = int(input('Enter max range of sides that can be generated: '))
            print(calc.sides(n, z))
        else:
            x = list(map(float, input("Enter the list numbers separated by space : ").strip().split()))
            calc.setx(x)
            calc.opone(op,x)
        cont = input('Enter Y to contine...')
main()
