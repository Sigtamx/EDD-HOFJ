# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 21:39:22 2018

@author: julianjavier
"""
class Nodo(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None       

r=Nodo("_")
q=r
p=q

def Raiz():
    Dato=raw_input("Ingrese el dato con el que creara la raiz\n")
    if(Dato=="_" and q.next==None):
        print("Ingrese un nombre distinto por favor")
        Raiz()
    else:
        global r
        r.data=Dato
        
def push(data):
    global q
    global p
    if(q.next==None):
        p=Nodo(data)
        q.next=p
        p.prev=q
        q=p

def pop(Val, t):
    global r
    global q
    p=t.next
    if(Val==r.data):
        t=r
        if(t.next==None):
            r.data="_"
            print("Se elimino el unico nodo existente")
        else:
            r=t.next
            r.prev=None
            print("Se destruye la raiz pero la nueva raiz es el siguiente dato")
            t=r     
    elif(p==None and t.data!=Val):
        print("El dato no se encuentra en ningun nodo")
    elif(Val==p.data):
        print("El valor se ha destruido")
        p=t.next
        t.next=p.next
        if(p.next!=None):
            (t.next).prev=t
        else:
            q=p.prev
            t.next=None
    else:
        t=t.next
        pop(Val, t)   
        
Raiz()
for i in range(1, 5):
    push(i)

def Verificacion(t):
    print(t.data)
    if(t.next!=None):
        t=t.next
        Verificacion(t)
    else:
        print("Fin")

Verificacion(r)

def VerifPop(t):
    print("Dato a eliminar")
    print(t.data)
    pop(t.data, r)
    if(t.next!=None):
        t=t.next
        VerifPop(t)
    else:
        print("Fin")
        
VerifPop(r)