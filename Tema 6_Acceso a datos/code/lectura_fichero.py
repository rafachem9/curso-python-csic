# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 17:32:20 2020

@author: Antonio

clase 1
"""
#Lectura del fichero, línea a línea
f=open("info.txt", "r")
cad=f.readline()
while cad!="":
    print(cad)
    cad=f.readline()
print("------")
f.close()   
#Lectura del fichero, todas las líneas de golpe
f=open("info.txt", "r")
cads=f.readlines()
for n in cads:
    print(n)
f.close()

print(cad)
print(cads)