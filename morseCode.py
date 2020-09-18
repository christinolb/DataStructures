# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 13:16:23 2020

@author: chris
"""

import winsound

def sndDot():
    freq = 750
    dur = 100
    winsound.Beep(freq,dur)
    
def sndDash():
    freq = 750
    dur = 300
    winsound.Beep(freq,dur)
    
def sndSpace():
    freq = 37
    dur = 750
    winsound.Beep(freq,dur)
     
    
def encrypt(message,morseTrans):
    #converts to lowercase
    message = message.lower()
    morse = ''
    for letter in message: 
        if letter != ' ':
            morse += morseTrans[letter] + ' '
        else: 
            # 1 space indicates different characters 
            # and 2 indicates different words 
            morse += '| '
  
    return morse 

def main():
    #create alpha dict
    morseTrans = { 'a':'.-', 'b':'-...', 
     'c':'-.-.', 'd':'-..', 'e':'.', 
     'f':'..-.', 'g':'--.', 'h':'....', 
     'i':'..', 'j':'.---', 'k':'-.-', 
     'l':'.-..', 'm':'--', 'n':'-.', 
     'o':'---', 'p':'.--.', 'q':'--.-', 
     'r':'.-.', 's':'...', 't':'-', 
     'u':'..-', 'v':'...-', 'w':'.--', 
     'x':'-..-', 'y':'-.--', 'z':'--..'}
    
    phrase = input("Enter a phase: ")
    
    morse = encrypt(phrase,morseTrans)
    print(morse)
    for i in morse:
        if i == '-':
            sndDash()
        elif i == '.':
            sndDot()
        elif i == ' ':
            sndSpace()
if __name__ == "__main__":
    main()
    