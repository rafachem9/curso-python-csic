# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 15:53:00 2020

@author: Antonio
"""

import requests
resp=requests.get('https://google.com')

#codigo HTML resp.text
print(resp)

for k, v in resp.headers.items():
   print(k,"=",v)
