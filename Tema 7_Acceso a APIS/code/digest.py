# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 18:03:14 2020

@author: Antonio
"""
from requests.auth import HTTPDigestAuth
import requests
resp=requests.get('https://api.github.com/user', auth=HTTPDigestAuth('amartinsierra', 'Almasoul.2'))
print(resp.headers)
