# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 10:50:57 2020

@author: Antonio
"""
import json
class Empleado:
    def __init__(self,nombre,departamento,salario):
        self.nombre=nombre
        self.departamento=departamento
        self.salario=salario
class GestionEmpleados:
    ruta="empleados.json"
    def __init__(self):
        with open(self.ruta) as file:
            self.empleados = json.load(file)

    def agregar(self,emp):
        obj={}
        obj["nombre"]=emp.nombre
        obj["departamento"]=emp.departamento
        obj["salario"]=emp.salario
        self.empleados.append(obj)
    def recuperar(self,dep):
        total=list(map(lambda l:Empleado(l["nombre"],l["departamento"],l["salario"]),self.empleados))         
        result=list(filter(lambda emp:emp.departamento==dep,total))
        return result
    def buscar(self,nombre):
        for emp in self.empleados:
            if emp["nombre"]==nombre:
                return Empleado(emp["nombre"],emp["departamento"],emp["salario"])
        return None
    def todos(self):
        return list(map(lambda l:Empleado(l["nombre"],l["departamento"],l["salario"]),self.empleados)) 
    def volcar(self):
        with open(self.ruta, "w") as write_file:
            json.dump(self.empleados, write_file)

empleados=GestionEmpleados()
opcion=0

def menu():
    print("1. Añadir empleado")
    print("2. Recuperar por departamentos")
    print("3. Buscar empleado")
    print("4. Ver todos")
    print("5. Salir")
    global opcion
    opcion=int(input("opcion:"))
    return

while(opcion<5):
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

#finaliza el programa, pero antes se vuelcan los datos en fichero
empleados.volcar()
