# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 06:11:05 2018

@author: pc
"""
#Declaracion de variables
cola=[]
size=7
F=0
R=0

#Se llena la cola de espacios vacios representados por 0
#La cantidad de espacios es igual al valor de la variable "size"
def create(cola):
    for i in range(size):
        cola.append(0)

create(cola)
#Metodo para agregar un valor en la cola circular
def push(item):
    global F
    global R
    #Se verifica si la cola esta vacia, en cuyo caso no se modificaran los valores de los indices
    #Ya que este primer valor es el principio y fin de la cola y ambos deben apuntar a el
    if(cola[F]==0):
        cola[R]=item
    #En caso que no este vacia la cola, deberan tomarse en cuenta otros factores
    else:
        #Se verifica que el indice del ultimo valor de la cola no este al limite de esta, 
        if(R<size-1):
            #Si el indice Rear esta un valor atras de Front, quiere decir que la cola esta llena
            #Ya que dio una vuelta completa y llego al ultimo valor disponible
            #En este caso se imprime el mensaje "Cola llena", ya que no hay espacios disponibles
            if(R==(F-1)):
                print("Cola llena")
            #En caso contrario, el indice se aumentara para no sobreeescribir el valor que se ingreso anteriormente
            #Acto seguido, se cambiara el 0(que representa el espacio vacio) por el valor ingresado
            else:
                R+=1
                cola[R]=item
        #En caso de que el indice ya este al limite, se verificara que el principio literal de la cola este vacio
        #En caso de que este vacio, el indice Rear se movera al principio y se agregara el valor ingresado
        elif(cola[0]==0):
            R=0
            cola[R]=item   
        #Si este espacio no esta vacio, quiere decir que ya no hay mas espacios vacios en la cola
        #Por lo tanto, se despliega el mensaje "Cola llena"
        else:
            print("Cola llena")
    #Metodos usados durante desarrollo
    #print(F)
    #print(R)
    #print(item)
    #Se muestra la cola completa despues de realizar una insercion
    print(cola)

push(1)
push(2)
push(3)
push(4)
push(5)
push(6)
push(7)
push(8)
