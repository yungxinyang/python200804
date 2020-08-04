# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:42:51 2020

@author: user
"""

name=list()
score=list()
total=0
avg=0

n=input('how many people?')
n=int(n)

for i in range(n):
    na=input('your name')
    name.append(name)
    sc=input('your score')
    sc=int(sc)
    score.append(score)
    total=total+sc
    print('avg is',total/n)


highest=0
for i in range(n):
    if sc[i]>highest:
       sc[i]=highest
       na=name[i]
       print(na,'you got the highest',highest)
lowest=100
for p in range(n):
    if sc[p]<lowest:
       sc[p]=lowest
       na=name[p]
       print(na,'you got the lowest',lowest)