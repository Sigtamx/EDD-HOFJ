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
    #Se muestra la cola completa despues de realizar una insercion
    print(cola)

#Metodo para eliminar el primer valor ingresado en la cola actual  
def pop():
    global F
    global R
    #Se verifica que el indice Front no haya sobrepasado la longitud de la cola
    if(F<size):
        #Se verifica que este espacio no este vacio, de ser asi, no hay valor que expulsar
        if(cola[F]!=0):
            #Cuando encuentra que hay un valor en el indice Front, lo mostrara y lo reemplazara con un 0
            print("Valor expulsado de la cola")
            print(cola[F])
            cola[F]=0
            #Se verifica si el indice Front y Rear estan en el mismo valor
            #De ser asi, querra decir que el ultimo valor fue eliminado
            #En este caso, decidi reiniciar los indices por pura estetica
            if(R==F):
                F=0
                R=0
            else:
                #En caso de que no esten en el mismo valor los indices Front y Rear
                #Esto quiere decir que aun hay valores en la cola
                #Se verifica que el indice Front no este al borde de la cola
                if(F!=(size-1)):
                    #Si encuentra que el indice Front todavia se puede recorrer, lo hara
                    F+=1
                else:
                    #Caso contrario, se reiniciara el indice a 0 para evitar desbordes
                    F=0
        #Si el valor en el indice Front es igual a 0, quiere decir que no hay valores en la cola
        else:
            #En cuyo caso, se imprimira un mensaje informando esto
            print("Cola vacia")
    #En caso de que se haya alcanzado el borde de la cola, se reiniciara el indice
    #Con esto, evitamos desbordamientos de indice      
    else:
        F=0
        cola[size-1]=0
    print(cola)    
  
push(1)
push(2)
push(3)
push(4)
push(5)
push(6)
push(7)
push(8)


pop()
pop()
pop()
pop()
pop()
pop()
pop()
pop()

push(1)
push(2)
push(3)
push(4)
pop()
pop()
pop()
push(5)
push(6)
push(7)
push(8)
push(9)
push(10)
pop()
pop()
pop()
pop()
pop()
pop()
pop()
pop()
