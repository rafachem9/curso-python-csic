# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 18:29:22 2020

@author: Antonio
"""

import sys
import os

if len(sys.argv)==1:
    print("Debe introducir argumentos")
    sys.exit()
else:
    fichero=sys.argv[1]
    if os.path.exists(fichero):
        os.remove(fichero)
        print("Fichero borrado")
input("")