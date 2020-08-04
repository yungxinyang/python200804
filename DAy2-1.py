# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 09:06:38 2020

@author: user
"""

import random
random.randint(1,10)
number=input('number')
number=int(number)
if number>=1 and number<=10:
  if number==random:
    print('correct')
  else:
    print('wrong')
else:
    print('輸入錯誤')