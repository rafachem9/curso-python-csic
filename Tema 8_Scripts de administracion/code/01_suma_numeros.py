# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 18:07:43 2020

@author: Antonio
"""

import sys
if len(sys.argv)==1:
    print("Debe introducir argumentos")
    sys.exit()
args=sys.argv
args.remove(0)
sum=0
for n in args:
    sum=int(n)
    
print("La suma es ",sum)