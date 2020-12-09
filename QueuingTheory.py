# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 10:45:46 2020

@author: chris
"""
import queue, random


def main():
    #creating line,couch and cashier queue
    Line = queue.Queue(maxsize=50)
    Couch = queue.Queue(maxsize=4)
    Cashier = queue.Queue(maxsize=50)
    
    #creating barber lists
    barber1 = []
    barber2 = []
    barber3 = []
    
    #generating random number 20 through
    #50 for customers
    totalCustomers = random.randint(20,50)
    
    #filling line with customers
    for i in range(1,totalCustomers):
        Line.put(i)
    empty = True
    b=0
    #loop for barbershop
    while empty:
        #check if couch is full
        while Couch.full() != True:
            #line to couch
            c = Line.get()
            Couch.put(c)
            print(c," is going to the couch")
            
        #check if barber chair is empty & fill
        if not barber1:
            c=Couch.get()
            print(c,"is going to barber1")
            barber1.append(c)
        if not barber2:
            c=Couch.get()
            print(c,"is going to barber2")
            barber2.append(c)
        if not barber3:
            c=Couch.get()
            print(c,"is going to barber3")
            barber3.append(c)
        #to cashier
        if b % 3 == 1:
            c=barber1.pop()
            print(c,"is going to the cashier")
            Cashier.put(c)
        if b % 3 == 2:
            c=barber2.pop()
            print(c,"is going to the cashier")
            Cashier.put(c)
        if b % 3 == 0:
            c=barber3.pop()
            print(c,"is going to the cashier")
            Cashier.put(c)
        b+=1
        if Cashier.empty() == True:
            empty = False
        c=Cashier.get()
        print(c,"has completed their transaction")
        
    

if __name__ == "__main__":
    main()