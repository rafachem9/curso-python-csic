# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 16:33:14 2020

@author: Antonio
"""

import pymongo as py
class Empleado:
    def __init__(self,nombre,departamento,salario):
        self.nombre=nombre
        self.departamento=departamento
        self.salario=salario
class GestionEmpleados:
    uri="mongodb://localhost:27017"
    def agregar(self,emp):
        obj={}
        obj["nombre"]=emp.nombre
        obj["departamento"]=emp.departamento
        obj["salario"]=emp.salario
        sr=py.MongoClient(self.uri)
        db=sr.empresa
        empleados=db.empleados
        empleados.insert_one(obj)
        sr.close()
    def recuperar(self,dep):
        sr=py.MongoClient(self.uri)
        db=sr.empresa
        empleados=db.empleados
        result=empleados.find({"departamento":dep})     
        lista= list(map(lambda l:Empleado(l["nombre"],l["departamento"],l["salario"]),result))  
        sr.close()
        return lista             
    def buscar(self,nombre):
        sr=py.MongoClient(self.uri)
        db=sr.empresa
        empleados=db.empleados
        result=empleados.find({"nombre":nombre})       
        res=None
        for emp in result:
            res= Empleado(emp["nombre"],emp["departamento"],emp["salario"])
        sr.close()
        return res
    def todos(self):
        sr=py.MongoClient(self.uri)
        db=sr.empresa
        empleados=db.empleados
        result=empleados.find()      
        lista=list(map(lambda l:Empleado(l["nombre"],l["departamento"],l["salario"]),result)) 
        sr.close()
        return lista
    def subir_salario(self, dep):
        sr=py.MongoClient(self.uri)
        db=sr.empresa
        empleados=db.empleados
        empleados.update_many({"departamento":dep},{"$inc":{"salario":120}})

empleados=GestionEmpleados()
opcion=0

def menu():
    print("1. Añadir empleado")
    print("2. Recuperar por departamentos")
    print("3. Buscar empleado")
    print("4. Ver todos")
    print("5. Aumentar Salario")
    print("6. Salir")
    global opcion
    opcion=int(input("opcion:"))
    return

while(opcion<6):
    menu()
    if opcion==1:     
        n=input("Introduce nombre ")
        d=input("Introduce departamento ")
        s=int(input("Introduce salario "))
        empleados.agregar(Empleado(n,d,s))
    elif opcion==2:
        dep=input("Introduce departamento ")
        for e in empleados.recuperar(dep):
            print(e.nombre)
    elif opcion==3:
        nom=input("Introduce nombre ")
        res=empleados.buscar(nom)
        if res!=None:
            print("Encontrado")
        else:
            print("No encontrado")
    elif opcion==4:
        for e in empleados.todos():
            print(e.nombre," - ",e.departamento," - ",e.salario)
    elif opcion==5:
        dep=input("Introduce departamento ")
        empleados.subir_salario(dep)


