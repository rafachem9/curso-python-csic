# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:25:54 2020

@author: Antonio

Clase 4
"""
import types
class Mymeta(type):
    def __new__(cls,clase,bases,args):
        nuevos_args={}
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