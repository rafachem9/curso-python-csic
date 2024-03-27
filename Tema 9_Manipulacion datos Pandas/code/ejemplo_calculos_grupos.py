# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 15:28:11 2020

@author: Antonio
"""

import pandas as pd
df=pd.read_csv("productos.csv", encoding="UTF-8")
print("Total de productos por sección: \n", df.groupby("seccion")["producto"].count())
print("\nMedia de precios por sección: \n",df.groupby("seccion").mean())
print("\nPrecio mayor de cada sección: \n",df.groupby("seccion")["precio"].max())
print("Sección con precio medio menor:  ",df.groupby("seccion")["precio"].mean().sort_values().index[0])
print("Producto más caro:  ",df.sort_values(by=["precio"],ascending=False).iloc[0]["producto"])