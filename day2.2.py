# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 11:17:44 2020

@author: user
"""



n=2
while True:
    num=input('number')
    num=int(num)
    if num%n==0:
        print('不是質數')
    else:
        print('是質數')
    n=n+1
    if n>num-1:
       break