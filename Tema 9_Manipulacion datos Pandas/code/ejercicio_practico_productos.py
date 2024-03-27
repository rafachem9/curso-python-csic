# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:27:23 2020

@author: Antonio
"""
import pandas as pd
df=pd.read_csv("productos.csv", encoding="UTF-8")
caro=""
max=0
medio=0
for k,v in df.iterrows():
    if v["precio"]>max:
        caro=v["producto"]
        max=v["precio"]
    medio=medio+v["precio"]
print("Producto más caro: ",caro," :",max)
print("Precio medio: ",medio/len(df.values))
