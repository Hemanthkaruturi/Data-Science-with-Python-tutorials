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

except Exception as e:
    print(e)
else:
    print('This is the else block')
finally:
    print('This is the final block')
    

try:
    x = int(input("Enter x value:"))
    y = int(input("Enter y value:"))
    
    divison = x/y

    print(divison)

except:
    print('There is some issue in the logic')
