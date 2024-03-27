# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 20:16:25 2020

@author: Antonio
"""

class Test:
    data=100
    def __init__(self):
        pass
    def metodo1(self):
        print("metodo1")
        
ob=Test()
#print(dir(ob))
#print(type(ob))
print(ob.__class__) #igual que type
print(Test.__dict__) #igual que dir(ob)
print(ob.__module__)
print(ob.__hash__)


#def mifuncion():
#    print("otra funcion")
#ob.metodo2=mifuncion
#ob.metodo2()
#print(dir(ob))

#función type
print("--type del objeto ob---")
print(type(ob))
print("--type de la propia clase Test---")
print(type(Test))
print("----HijaTest----")
#crear clase
HijaTest=type("HijaTest",(Test,),{})
ob2=HijaTest

print(ob2.__doc__)

def fun():
    print("metodo2")
def f():
    print("constructor hija")
HijaTest2=type("HijaTest2",(Test,),{"dato":200,"metodo2":fun})
HijaTest2.__init__=f
print("---HijaTest2---")
ob3=HijaTest2
print(ob3.dato)
print(ob3.metodo2())
print(HijaTest2.__dict__)