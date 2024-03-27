# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:48:02 2020

@author: Antonio
"""
import types
class Mymeta(type):
    def __new__(cls,clase,bases,args):
        nuevos_args={}
        #recorre todos los miembros de la nueva clase
        #si son atributos, añade un caracter de subrayado delante del nombre
        for name, val in args.items():
            if not isinstance(val, types.FunctionType):
                nuevos_args["_"+name]=val
            else:
                nuevos_args[name]=val
        return super().__new__(cls,clase,bases,nuevos_args)

class Test(metaclass=Mymeta):
    data=5
    def metodo():
        print("metodo")

print(Test.__dict__)
obj=Test()
print(obj._data)