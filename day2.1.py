# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:46:54 2020

@author: user
"""

import random
n = random.randint(1,20)
i=0
while True:
        number=input("number")
        number=int(number)
        if number>20 or number<0:
            print('輸入錯誤')
        else:
            if number>n:
                print('再小一點')
            elif number<n:
                print('再大一點')
            else:
                print('BINGO')
                break 
        i=i+1
        if i>4:
            break
    
