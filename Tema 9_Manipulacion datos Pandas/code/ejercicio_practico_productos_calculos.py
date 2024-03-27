# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:05:06 2020

@author: Antonio
"""

import pandas as pd
df=pd.read_csv("productos.csv", encoding="UTF-8")
print("Precio más alto: ",df["precio"].max())
print("Precio más bajo: ",df["precio"].min())
print("Precio medio: ",df["precio"].mean())
print("Total de productos: ",df["precio"].count())
limite=int(input("Introduce precio límite: "))
filtro=df.query("precio<=@limite")
print(filtro)