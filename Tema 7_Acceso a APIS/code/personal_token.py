# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 18:19:11 2020

@author: Antonio
"""
#personal token, es para evitar dar tu contraseña, hay que pedirlo a la empresa
import requests
token="787fbe6fe180980f2ff5d8507c2ca1cd65f800c8"
headers={'Authorization': 'token %s' % token}
resp=requests.get('https://api.github.com/user',headers=headers)
print(resp.text)