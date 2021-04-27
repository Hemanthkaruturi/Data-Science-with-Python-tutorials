# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 09:09:23 2021

@author: 600037209
"""

x = "This is page 1"

def func():
    print("This is a function in page 1")

class Dummy():
    def dummy(self):
        print("This is dummy class")

def get_name_page1():
    return __name__


print(get_name_page1())