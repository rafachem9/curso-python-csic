# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 07:30:08 2020

@author: Antonio
"""

import subprocess


proc = subprocess.Popen(
    ['echo', 'hacia la salida'],shell=True,
    stdout=subprocess.PIPE
)

stdout_value = proc.communicate()[0].decode('iso-8859-1')
print('valor:', stdout_value)
print("pid",proc.pid)