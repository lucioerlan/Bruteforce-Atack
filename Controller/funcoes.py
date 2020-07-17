#coding: utf-8
# -*- coding:utf-8 -*-

import os
import sys
import time

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white
C = '\033[1;36m' #cyanClaro
P = '\033[1;35m' #purpleClaro
Y = '\033[1;33m' #amarelo

class funcoes:

    def __init__(self):
        self.error = None
        time.sleep(1)
    
        
    def banner(self):
        os.system('cls')
        version = '1.0.'
        print ('\n' + R +
        r'''
                                                                 
            )    )     )         (       )  
   (     ( /( ( /(  ( /(     (   )\ ) ( /(  
   )\    )\()))\()) )\())    )\ (()/( )\()) 
((((_)( ((_)\((_)\ ((_)\   (((_) /(_)|(_)\  
 )\ _ )\ _((_) ((_) _((_)  )\___(_))__ ((_) 
 (_)_\(_) \| |/ _ \| \| | ((/ __| _ \ \ / / 
  / _ \ | .` | (_) | .` |  | (__|   /\ V /  
 /_/ \_\|_|\_|\___/|_|\_|   \___|_|_\ |_|   
                                           
                                                                                          
        ''' + R)
        
        print('\n' + G + '[>]' + C + ' Created By : ' + W + 'Erlan Lucio')
        print(G + '[>]' + C + ' Version    : ' + W + version + '\n')

    def escolheDep(self):    
        condicao = True
        while (condicao is True):
            install = input('Install Dependencies? [Y/n]: ')
            if (install == 'Y'):
                os.system('pip install  -r requiriments.txt')
                print('\n' + C + 'Libraries installed successfully!' + W + '\n')
                time.sleep(3)
                os.system('python ./BruteForce/crack.py')
                condicao = False
            elif(install == 'n'):
                condicao = False
                os.system('python ./BruteForce/crack.py')

pass

# _______________________________________________________________________________________#





