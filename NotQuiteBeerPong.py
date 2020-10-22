# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 18:48:53 2020

@author: chris
"""

import random
n=random.randint(0,300)
ls_of_ls=[]#list of lists
for i in range(n):
    ls=[]
    #append empty list to list of lists
    ls_of_ls.append(ls)
flag=1
#number of empty cups
emp=1
#iterations
iter=0
#balls drawn
balls=0
while emp!=0:
    #start of round
    flag=1
    while flag==1:
        #generate random ball number
        r=random.randint(1,n)
        #generate random cup
        k=random.randint(1,n)
        #throw ball into cup
        ls_of_ls[k-1].append(r)
        #increment number of balls
        balls=balls+1
        count=0
        for i in range(n):
            #count numbers of cup having balls greater than 0
            if len(ls_of_ls[i])>0:
                count=count+1
        #until each of the cup contain at least 1 ball
        if count==n:
            flag=0
    for i in range(n):
        #keep only the ball having number i on the cup having number i
        ls_of_ls[i]=list(filter(lambda a: a == (i+1),ls_of_ls[i]))
    emp=0
    for i in range(n):
            #counting no of empty cup
            if len(ls_of_ls[i])==0:
                emp=emp+1
    #increase iteration count
    iter=iter+1
print("Number of rounds: ",iter)
print("Balls would you expect to need to draw and throw to finish :  ",balls)