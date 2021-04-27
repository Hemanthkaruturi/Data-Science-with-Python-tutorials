# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 09:43:36 2021

@author: 600037209
"""
import time
import multiprocessing
import os

def print_evens():
    print('Started printing even numbers..')
    print('Process ID:', os.getpid())
    for i in range(1,11):
        if (i%2 == 0):
            print(i)
            time.sleep(2)
            
def print_odds():
    print('Started printing odd numbers..')
    print('Process ID:', os.getpid())
    for i in range(1,11):
        if (i%2 != 0):
            print(i)
            time.sleep(2)

if __name__ == '__main__':
    # create threads
    process1 = multiprocessing.Process(target=print_evens, name='thread1')
    process2 = multiprocessing.Process(target=print_odds, name='thread2')
    
    # start my threads
    process1.start()
    process2.start()
    
    # join my threads
    process1.join()
    process2.join()


