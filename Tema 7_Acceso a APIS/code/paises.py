# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 18:52:11 2020

@author: Antonio
"""

import requests
#error pagina web, la he cambiado
response = requests.get('https://restcountries.com/v2/all')
paises=response.json()

#" Capital:",p["capital"], he borrado esto poruqe hay paises que no tienen
for p in paises:
    print("País:",p["name"]," Población:",p["population"], " Idioma:",p["languages"][0]['iso639_1'])
