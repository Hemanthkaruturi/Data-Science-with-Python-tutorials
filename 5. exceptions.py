# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 09:19:45 2021

@author: 600037209
"""

try:
    x = int(input("Enter x value:"))
    y = int(input("Enter y value:"))
    
    divison = x/y
    
    print(divison)

except ValueError:
    print('You must provide an integer')
except ZeroDivisionError:
    print('Y value must be greater than zero')
    


