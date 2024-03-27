# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 18:05:55 2020

@author: Antonio
"""

import threading
import time

class Contador:
    value=0
    def inc(self):
        act=self.value
        act+=1
        time.sleep(0.1)
        self.value=act

class Tarea(threading.Thread):
    conta=None
    def __init__(self,contador):
        threading.Thread.__init__(self)
        self.conta=contador
    def run(self):
        #Para ver el funcionamiento tenemos que eliminar lk.acquire() y lk.release() para que no se puedan sincronizar
        #   las tareas
        lk.acquire()
        self.conta.inc()
        lk.release()
        print("Valor actual del contador "+str(self.conta.value))
lk=threading.Lock()
ct=Contador()       
for i in range(1,10):
    Tarea(ct).start()