# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 18:23:10 2020

@author: Antonio

w= escritura, r = lectura, a=añadir información
"""
#Escribe en modo sobrescritura
f=open('info.txt', 'w')
f.write("Esto es una nueva línea\n")
f.write("Esto es una segunda línea\n")
f.close()
#Escribe en modo append
f=open('info.txt', 'a')
f.write("Esto es una tercera línea\n")
f.write("Esto es una cuarta línea\n")
f.close()