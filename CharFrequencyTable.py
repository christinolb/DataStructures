# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 09:04:54 2020

@author: chris
"""

import random, string

def main():
    ## the list of lowercase characters that 
    ##you will build your string from.
    aAlphabet = list(string.ascii_lowercase)
    ##The dictionary you will build from the
    ##character frequencies.
    dCharCnt = {}
    ## a counter for your loop
    cnt = 0
    ## Builds the string from aAlphabet.
    strEncrypt = "".join([random.choice(aAlphabet)for strChar in range (45)])
    #nested loop for counting each letter
    for letter in strEncrypt:
        for l in strEncrypt:
            if letter == l:
                cnt+=1
                dCharCnt.update({l:cnt})
        cnt=0
    #displaying output
    print(strEncrypt)
    aSorted = sorted(dCharCnt.items(), key=lambda x: x[1],reverse=True)
    for i in aSorted:
        print(i[0],":",i[1])
    print(aSorted)
if __name__ == "__main__":
    main()