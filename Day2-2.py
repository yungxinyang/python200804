# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:20:37 2020

@author: user
"""

import random
n = random.randint(1,20)
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
        
