# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 09:45:17 2020

@author: chris
"""
from random import shuffle, randint

def pickSearch(l):
    n = randint(1,10)
    for i in range(10):
        if l[i] == n:
            l.remove(n)
            l.insert(0,n)
    return l
    

def main():
    num = [i for i in range(1,11)]
    shuffle(num)
    for i in range(10):
        num = pickSearch(num)
        print(num)

if __name__ == "__main__":
    main()