# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:38:42 2020

@author: Antonio
"""

import pymongo as py
uri="mongodb://localhost:27017"
sr=py.MongoClient(uri)
db=sr.formacion
cr=db.cursos
#cr.insert_one({"curso":"Ofimática","duracion":80,"precio":150})
#$inc = incrementar el valor
cr.update_one({"curso":"Ofimática"},{"$inc":{"precio":100}})

#Buscar algo en la base de datos $lt lt= lest thanç
#{"precio": {"$lt":300}}

for c in cr.find():
    print(c)

sr.close()

