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
                
                #print("REINICIO")
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
        
    #print(F)
    #print(R)
    print(cola)    

#Metodo para ver los valores en la cola, con distintas variaciones
def peek(F, R):
    print("Ingrese 1 para ver el primer valor ingresado")
    print("Ingrese 2 para ver el ultimo valor ingresado")
    print("Ingrese 3 para ver todos los valores en la cola actualmente")
    print("Ingrese 4 para buscar el indice de un numero que usted ingresara")
    print("Ingrese 5 para regresar al menu principal")
    #la opcion que ingrese el usuario se guardara en opeek
    opeek= input()
    if(opeek==1):
        #Si el usuario selecciona la opcion 1, se le mostrara el valor en el indice Front
        #Esto quiere decir, el valor mas antiguo en la cola
        #Acto seguido, se llamara de nuevo al metodo para poder utilizar otras opciones si asi se desea
        print(cola[F])
        peek(F, R)
    elif(opeek==2):
        #Si el usuario selecciona la opcion 2, se le mostrara el valor en el indice Rear
        #Esto significa que se imprimira el valor recientemente agregado
        #Despues, se llamara a si mismo el metodo para ver de nuevo el menu de opciones peek
        print(cola[R])
        peek(F, R)
    elif(opeek==3):
        #Si el usuario selecciono la opcion 3, se le mostrara la cola copmleta
        #Despues de mostrarlo, se llamara a si mismo para iniciar de nuevo el menu peek
        print(cola)
        peek(F, R)
    elif(opeek==4):
        #En caso de ingresar 4, se le pedira al usuario ingresar el numero que quiere buscar
        #Se guarda su busqueda en ope y se verifica que este en la cola
        print("Ingrese el numero que desea buscar")
        ope=input()
        if(ope in cola):
            #Una vez se haya verificado que se encuentra en la cola
            #Se imprimira el indice en el que se encuentra el valor buscado
            print("El valor se encuentra en el indice:")
            print(cola.index(ope))
        else:
            #En caso contrario, se mostrara el siguiente mensaje y se le enviara de nuevo al menu peek
            print("El valor que ingreso no se encuentra en la cola")
        peek(F, R)
    elif(opeek==5):
        #Si se selecciona 5, se le regresara al menu principal
        menu()
    else:
        #En caso de ingresar cualquier otra opcion, se le mostrara el siguiente mensaje
        #Y se le enviara al menu de peek
        print("Ingreso un valor invalido")
        peek(F, R)

#Metodo principal, menu donde se podran seleccionar los metodos de la cola circular
def menu():
    print("Ingrese 1 para utilizar metodo push")
    print("Ingrese 2 para utilizar metodo pop")
    print("Ingrese 3 para utilizar metodo peek")
    print("Ingrese 4 para salir del programa")
    #El valor ingresado por el usuario se guarda en opc, se usara para ingresar a los metodos
    opc = raw_input()
    if(opc=="1"):
        #Si el usuario selecciono 1, se le pregutnara que valor desesa agregar a la cola circular
        #Ese valor se guardara en "i" y se mandara como parametro para el metodo push
        #Despues de terminar la ejecucion del metodo push, se llamara al menu de nuevo
        print("Ingrese el valor que desea agregar a la cola")
        i = input()
        push(i)
        menu()
    elif(opc=="2"):
        #Si se ingreso el valor 2, se llamara al metodo pop
        #En este caso no se le pide nada al usuario, ya que pop no lleva parametros
        #Al terminar la ejecucion del metodo pop, se llamara al menu para utilizar otras opciones
        pop()
        menu()
    elif(opc=="3"):
        #En caso de ingresar 3, se ejecutara el metodo peek
        #Se mandaran como parametros los indices Front y Rear actuales
        #En este caso no se llama al menu de nuevo, ya que peek cuenta con su propio menu
        #Y con una opcion para regresar al menu principal
        peek(F, R)
    elif(opc=="4"):
        #Al ingresar 4 se termina el programa
        print("Fin del programa")    
    else:
        #En caso de ingresar algo distinto a las opciones brindadas, se mostrara este mensaje
        #Y se le regresara al menu para utilizar alguna opcion si asi se desea
        print("Ingreso una opcion invalida")
        menu()
        
#Se llama al metodo menu
menu()  
