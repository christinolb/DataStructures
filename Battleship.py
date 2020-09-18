# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 13:31:03 2020

@author: chris
"""
from random import randint

def hint(l,r,c, aArray):
  try:
    if aArray[l][r-1][c] == "S":
        return "(above)"
    if aArray[l][r+1][c] == "S":
        return "(below)"
    if aArray[l][r][c+1] == "S":
        return "(right)"
    if aArray[l][r][c-1] == "S":
        return "(left)"
    else:
      return "No ships in radius"
  except IndexError:
    return "No ships in radius"
        

def coord():
    row = randint(0, 9)
    column = randint(0,9)
    level = randint(0,2)
    
    return level, row, column

def collision(level,row,column,size,aArray,opt):
    #ensures ship will fit on plane
    column1=column
    while column+(size-1) > 9:
        column = randint(0,9)
        if column > 9:
            column = column1
    clear = True
    if opt == 0:
        for i in range(size-1):
            if aArray[level][row][column] == "S":
                clear = False
            else:
                column+=1
    
    if opt == 1:
        #ensures ship will fit on plane
        row1=row
        while row+(size-1) > 9:
            row = randint(0,9)
            if row > 9:
                row = row1
        for i in range(size-1):
            if aArray[level][row][column] == "S":
                clear = False
            else:
                row+=1
    
    if opt == 2:
        #ensures ship will fit on plane
        column1=column
        row1=row
        while column+(size-1) > 9 or row+(size-1) > 9:
            column = randint(0,9)
            row = randint(0,9)
            if column > 9 or row > 9:
                column = column1
                row = row1
        for i in range(size-1):
            if aArray[level][row][column] == "S":
                clear = False
            else:
                row+=1
                column+=1
            
    return clear, level, row, column, opt
        

def aRow(level,row,column,size,aArray):
    #ensures ship will fit on plane
    row1=row
    while row+(size-1) > 9:
        row = randint(0,9)
        if row > 9:
            row = row1
    #creates ship
    for i in range(size):
        aArray[level][row][column]="S"
        row+=1
            
    return aArray

def aColumn(level,row,column,size,aArray):
    #ensures ship will fit on plane
    column1=column
    while column+(size-1) > 9:
        column = randint(0,9)
        if column > 9:
            column = column1
    #creates ship
    for i in range(size):
        aArray[level][row][column]="S"
        column+=1
        
    return aArray

def aDiagnal(level,row,column,size,aArray):
    #ensures ship will fit on plane
    column1=column
    row1=row
    while column+(size-1) > 9 or row+(size-1) > 9:
        column = randint(0,9)
        row = randint(0,9)
        if column > 9 or row > 9:
            column = column1
            row = row1
    #creates ship
    for i in range(size):
        aArray[level][row][column]="S"
        column+=1
        row+=1
    return aArray

def createShip(level, row, column, size, pos, aArray):
    #VERTICAL
    if pos == 0:
        aArray=aColumn(level,row,column,size,aArray)
    
    #HORIZONTAL
    if pos == 1:
        aArray = aRow(level,row,column,size,aArray)
    
    #DIAGNAL  
    if pos == 2:
        aArray = aDiagnal(level, row, column, size, aArray)
    
    return aArray
            
            
def main():
    #creating array
    aArray = [[["-" for j in range(10)]for j in range(10)]for j in range(3)]
    bArray = [[["-" for j in range(10)]for j in range(10)]for j in range(3)]
    
    #list of ship sizes
    sizes = [2,3,3,4,5]
    
    clear = False
    #creating 5 ships
    for size in sizes:
        while clear == False:
            #random coodinates
            level, row, column = coord()
            #randomly chooses position of ship 
            pos = randint(0,2)
            #checks for collision
            clear, level, row, column, pos = collision(level, row, column, size, aArray, pos)
              
        #if test is passed ship is created
        aArray = createShip(level, row, column, size, pos, aArray)
        clear = False
    #Game starts
    print("██████╗░░█████╗░████████╗████████╗██╗░░░░░███████╗░██████╗██╗░░██╗██╗██████╗░")
    print("██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║░░░░░██╔════╝██╔════╝██║░░██║██║██╔══██╗")
    print("██████╦╝███████║░░░██║░░░░░░██║░░░██║░░░░░█████╗░░╚█████╗░███████║██║██████╔╝")
    print("██╔══██╗██╔══██║░░░██║░░░░░░██║░░░██║░░░░░██╔══╝░░░╚═══██╗██╔══██║██║██╔═══╝░")
    print("██████╦╝██║░░██║░░░██║░░░░░░██║░░░███████╗███████╗██████╔╝██║░░██║██║██║░░░░░")
    print("╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚══════╝ ═════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░")
    print()
        
    run = True
    spots = 0
    while run:
        for guess in range(30):
            #printing array
            print()
            
            for i in range(3):
                print("Level",i)
                print("  0 1 2 3 4 5 6 7 8 9")
                for j in range(10):
                    print(j,end="")
                    for l in range(10):
                        print('|',end="")
                        print(bArray[i][j][l],end="")
                        if l == 9:
                            print("|")
            print()
            
            #User enters guess
            print("🅁🄴🄼🄰🄸🄽🄸🄽🄶 🄰🅃🅃🄴🄼🄿🅃🅂:", 30-guess)
            print("Spots found:",spots,"/17")
            print("Enter your guess")
            l=int(input("Level:"))
            r=int(input("Row:"))
            c=int(input("Column:"))
            
            
            if aArray[l][r][c] == "S":
                print()
                print("Spot found!")
                spots+=1
                bArray[l][r][c] = "S"
            else:
                print("Nothing found here, try again.")
            
            print(hint(l,r,c,aArray))
            if spots == 17:
                run = False
if __name__ == "__main__":
    main()
    
