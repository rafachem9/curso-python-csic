# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 14:46:22 2020

@author: Antonio
"""
import requests
resp=requests.get('https://api.github.com/user', auth=('amartinsierra', 'xxxxxx'))
print(resp.text)