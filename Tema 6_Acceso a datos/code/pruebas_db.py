# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:40:57 2020

@author: Antonio
"""
import pymongo as py
uri="mongodb://localhost:27017"
sr=py.MongoClient(uri)
#referencia a base de datos "formacion"
db=sr.formacion
print(db.list_collection_names())
cursos=db.cursos
#cursos.insert_many([{"curso":"Java","duracion":120,"precio":350},{"curso":"Python","duracion":80,"precio":250}])
#cursos.update_one({"curso":"Java"},{"$mul":{"precio":1.2}});

for c in cursos.find():
    print(c)