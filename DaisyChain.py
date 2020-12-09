# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 10:52:24 2020

@author: chris
"""

import random

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata
        
    def setNext(self, newnext):
        self.next = newnext
        
class UnorderedList:

    def __init__(self):
        self.head = None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found
    
    def printLL(self):
        current = self.head
        while(current):
          print(current.data)
          current = current.next
    
    def switch(self, position):
        node = self.head
        i = 0
        while i <=13:
            if i == position:
                node.setData(0)
                break
            i += 1
            node = node.next
        while node.getNext() != None:
            node = node.next
            node.setData(0)
    
def main():
    loop = True
    while loop:
        #creating linked list 
        daisyChain = UnorderedList()
        #setting all values to 1
        for i in range(14):
            daisyChain.add(1)
        #printing List
        print("Before: ")
        daisyChain.printLL()
        print()
        #creating random index to interrupt 
        ranInx = random.randint(0,13)
        #implementing
        print("After: ")
        daisyChain.switch(ranInx)
        daisyChain.printLL()
        
        userInp = input("Would you like to run simulation again (y/n): ")
        
        if userInp == 'n':
            loop = False
            
    
    
    
if __name__ == "__main__":
    main()