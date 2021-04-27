# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 09:30:08 2021

@author: 600037209
"""

# import page1
# import page2

# import page1 as p1
# import page2 as p2

from page1 import x
from page2 import y

# print(page1.x)
# print(page2.y)

# print(p1.x)
# print(p2.y)

print(x)
print(y)


import page1
import page2

page1.func()
page2.func()


from page1 import func,x
from page2 import func,y

func()
x


from page1 import Dummy

d = Dummy()
d.dummy()


from Modules import page1
from Modules import page2

from page1 import x

from Modules.page1 import x
from Modules.page2 import y

print(x)
print(y)

import os

os.getcwd()
os.chdir()


import re


def get_name():
    return __name__



get_name()

from Modules.page1 import get_name_page1
from Modules.page2 import get_name_page2


get_name_page1()

get_name_page2()


if __name__ == '__main__':
    print("Starting the program")


