# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:57:19 2018

@author: Takuto
"""
def fib(n):
    if n >= 3:
        return fib(n-1) + fib(n-2)
    else:
        return 1
print(fib(10))


print(fib(5))