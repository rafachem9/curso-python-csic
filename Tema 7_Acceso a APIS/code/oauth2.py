# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 17:17:19 2020

@author: Antonio
"""

import requests

pars={"client_id":"amartinsierra",}
response = requests.get('https://github.com/login/oauth/authorize',params=pars)
print(response.text)