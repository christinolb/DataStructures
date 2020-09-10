# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 10:16:45 2020

@author: chris
"""

aArray = [[["" for j in range(4)]for j in range(4)]for j in range(3)]

for i in range(3):
    print("Level",i)
    for j in range(4):
        for l in range(4):
            print('|',end="")
            print(str(l),",",str(j),",",str(i), end="")
            if l == 3:
                print("|")
