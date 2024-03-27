# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 13:10:23 2020

@author: Antonio
"""

import json

#lectura de JSON desde memoria
myjson='[{"nombre":"lucas","telefono":33333},{"nombre":"gema","telefono":1111}]'
conver=json.loads(myjson)
#envía documento a fichero
with open("personas.json", "w") as write_file:
    json.dump(conver, write_file)





print(json.dumps(conver,separators=("-",".")))
#for n in conver:
#    print(n["nombre"])
#    
with open('datos.json') as file:
    datos = json.load(file)
    for l in datos:
        print(l["titulo"])
        
