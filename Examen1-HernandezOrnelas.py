# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 19:47:38 2018

@author: julianjavier

1. Realizar un programa que entregue el resultado de sumar 1+2+3+4+5+6+7+8+9, utilizando
recursividad

"""

""

def programaUno(num):
    if(num<=9):
        num+=1
        programaUno(num)
    else:
        print(((num)*(num-1))/2)
        
print("Inicio de programa 1")
programaUno(1)
print(1+2+3+4+5+6+7+8+9)
print("Final de programa 1")

"""

2. Realizar un programa que entregue el resultado de la siguiente ecuacion 2^n 
utilizar recursividad

"""

def programaDos(num, N):
    if(num>1):
        N*=2
        num-=1
        programaDos(num, N)
    else:
        print(N)

print("Inicio de programa 2")
print("Ingrese la potencia a la que desea elevar el numero 2")
n = input()    
programaDos(n, 2)    
print("Final de programa 2")


"""

3. Hacer un programa que lleve el control de versiones de un proyecto en una empresa
la estructura de datos debe controlar el numero de migraciones realizadas en el proyecto.
Utilizar una pila para introducir las migraciones una por una y
obtener las migraciones una por una empezando por la migracion mas actual y 
terminando por la migracion mas antigua.

"""

Registro=[]
indice=1

def AgregarV():
    global indice
    Registro.append(indice)
    indice+=1
    print(Registro)
    
def EliminarV():
    
    if(len(Registro)>0):
        global indice
        del Registro[indice-2]
        print(Registro)
        indice-=1
    else:
        print("Registro de migraciones vacio")
        
def VisualizarV():
    print("Todas las migraciones, de la mas reciente a la mas antigua")
    for i in range(len(Registro)):
        print(Registro[len(Registro)-i-1])

def MenuV():
    print("Ingrese 1 para agregar al registro una migracion.")
    print("Ingrese 2 para eliminar el registro de la migracion mas reciente.")
    print("Ingrese 3 para visualizar todo el registro de migraciones en el proyecto.")
    print("Ingrese 4 para salir del sistema.")
    opc = input()
    if(opc==1):
        AgregarV()
        MenuV()
    if(opc==2):
        EliminarV()
        MenuV()
    if(opc==3):
        VisualizarV()
        MenuV()
    if(opc==4):
        print("Fin del programa")
    elif(opc>4 or opc<1):
        print("Ingreso una opcion invalida")
        MenuV()
print("Inicio de programa 3")
MenuV()
print("Final de programa 3")

"""

4. Hacer un programa que simule la fila de clientes de una tienda de super mercado, considerando que
solo hay una caja que esta activa. La fila solo puede tener como maximo 5 clientes!

"""

fila=[]
size=5
actual=0

def crear(fila):
    for i in range(size):
        fila.append("Vacio")
    print(fila)
    


def push():
    global actual
    if(actual<5):
        fila[actual]="Ocupado"
        actual+=1
        print(fila)
    else:
         print("Fila de mercado llena")
         
def pop():
    global actual
    if(actual>0):
        act=1
        for i in range(size):
            fila[act-1]=fila[act]
        fila[actual-1]="Vacio"
        
        actual-=1
        print(fila)
    else:
        print("Fila de mercado vacia")

def peek():
    print("Frente de la fila esta")
    print(fila[0])
    
def empty():
    if(actual==0):
        print("Fila vacia")
    else:
        print("Fila no vacia")
        
def Menu():
    print("Ingrese 1 para agregar un cliente a la fila")
    print("Ingrese 2 para desocupar un cliente")
    print("Ingrese 3 para ver si el frente de la fila esta ocupado")
    print("Ingrese 4 para ver si la fila esta vacia")
    print("Ingrese 5 para salir")
    opc=input()
    if(opc==1):
        push()
        Menu()
    if(opc==2):
        pop()
        Menu()
    if(opc==3):
        peek()
        Menu()
    if(opc==4):
        empty()
        Menu()
    if(opc==5):
        print("Fin del programa")
    elif(opc>5 or opc<1):
        print("Ingreso una opcion invalida")
        Menu()
    
print("Inicio de programa 4")
crear(fila)
Menu()
print("Final de programa 4")
""