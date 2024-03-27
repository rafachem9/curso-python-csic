# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 18:09:54 2020

@author: Antonio
"""

import pandas as pd
df=pd.read_csv("../productos.csv", encoding="UTF-8")
caro=""
max=0
media=0
for k,v in df.iterrows():
    if v["precio"]>max:
        caro=v["producto"]
        max=v["precio"]
    media+=v["precio"]
print("Producto más caro: ",caro)
print("Precio medio total: ",media/len(df.values))