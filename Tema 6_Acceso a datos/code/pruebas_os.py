# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 11:22:09 2020

@author: Antonio
"""

import os
print(os.getcwd())
os.rename("info.txt", "pruebas.txt")
os.remove("datos.txt")