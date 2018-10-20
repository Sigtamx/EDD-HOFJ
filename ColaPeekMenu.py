#Se crea la cola
#Se inicia el tamaño maximo de la cola en 5
cola=[]
index=0
size=5

#Metodo para llenar la cola con valores vacios, inicianizandola
def create():
    for I in range(size):
        cola.append(0)
    return cola
    
create()

#Metodo para agregar valores a la cola, se agregaran en el espacio disponible mas cercano al frente
def push(Val, index):
    #Se verifica que no se encuentre llena la cola
    if index < size:
        #Se sobreescribe el valor vacio con el valor ingresado por el usuario
        cola[index] = Val 
    else:
        print("****************Cola llena****************")
        
#Metodo para eliminar el valor mas antiguo dentro de la cola
def pop(index):
    #Se verifica que la cola no este vacia
    if index>0:
        #En caso de que no este vacia, se imprimira el numero que se encuentre al frente
        print("Numero eliminado:")
        print(cola[0])
        ind=0
        #Ahora se recorreran los valores, ocupando el espacio que dejo la salida del primero
        for I in range(size-1):
            cola[ind]=cola[ind+1]
            ind+=1
        #Con este metodo, se queda repetido el valor mas recientemente ingresado, asi que se iguala a 0
        cola[index-1]=0  
        
        
    else:
        print("****************Cola vacia****************")

#Un menu con varias opciones para visualizar la cola
def peek(index):
    print("Ingrese la opcion deseada peek")
    print("Ingrese 1 para ver el ultimo valor de la cola")
    print("Ingrese 2 para ver todos los valores")
    print("Ingrese 3 para buscar un valor manualmente")
    print("Ingrese 4 para volver al menu principal")
    opc = input()
    #La opcion del usuario se ingresa a un menu y se ejecuta el submetodo que el usuario desea
    if(opc==1):
        #Peek que muestra el valor mas reciente ingresado a la cola
        #Se verifica que haya por lo menos un valor en la cola
        if (0 < index):
            print("Ultimo de la cola:")  
            print(cola[index-1])
            print("Indice:")
            #Se muestra en que indice se encuentra dicho valor
            print(cola.index(cola[index-1]))
            #Se ejecuta de nuevo el metodo peek para poder utilizar las otras opciones de este subMenu
            peek(index)
        else:
            #En caso de que no haya algun valor en la cola, se manda un mensaje informando esto
            #Y se ejecuta de nuevo el metodo peek
            print("cola vacia");
            peek(index)
    if(opc==2):
        #Peek que muestra todos los valores en la cola
        #Se verifica que la cola cuente con un valor por lo menos
        if (0 < index):
            #Se imprimen en orden todos los valores dentro de la cola, no muestra valores vacios
            print("Los valores de la cola son estos")
            for Num in range(index):
                print(cola[Num])
            peek(index)
        else:
            #En caso que no haya algun valor en la cola, quiere decir que esta vacia
            print("La cola esta vacia")
            peek(index)
    if(opc==3):
        #Peek en el que el usuario ingresa un valor y se busca que este en la cola
        #Se verifica que por lo menos cuente con un valor la cola
        if (0 < index):
            #Se le pide al usuario el valor que desea buscar
            print("Ingrese el valor que desea buscar:")
            
            i = input()
            #Se guarda este valor en una variable y despues se comparan todos los valores 
            #Dentro de la cola con el ingresado, si hay una coincidencia se imprimira el indice donde esta
            for Num in cola:
                if (Num==i):
                    print("El valor se encuentra en el indice")
                    print(cola.index(Num))
                    peek(index)
            #En caso de no haber coincidencias, quiere decir que este dato no esta en la cola
            print("Valor no encontrado")
            peek(index)
    #Se regresa al menu principal para poder hacer uso de los demas metodos
    if(opc==4):
        print("De regreso al menu principal...")
        Menu(index)
    #En caso de ingresar una opcion fuera de las opciones disponibles, se mostrara un error
    #Y se mandara de regreso al menu de peek
    elif(opc<0 or opc>4):
        print("Valor invalido")
        peek(index)
    
#Menu principal donde se podran utilizar los menus principales
def Menu(index):
    print("Menu de cola")
    print("Ingrese numero 1 para la opcion push")
    print("Ingrese numero 2 para la opcion pop")
    print("Ingrese numero 3 para la opcion peek")
    print("Ingrese numero 4 para salir")
    #Se lee la opcion que el usuario ingreso y se guarda en una variable
    opc = input()
    #Esta variable luego se lee y se ingresa al menu 
    if (opc==1):
        #Si ingreso 1, se ejecutara el metodo Push, pero se debe verificar primero algo
        #Se verifica que la cola no este llena, osea que el indice este por debajo del limite
        if(index < size):
            #Se le pide al usuario el valor que ingresara a la cola
            print("Ingrese el numero que desea ingresar a la cola")
            i = input()
            #Se llama al metodo push 
            push(i, index)
            index+=1
            #Se ejecuta de nuevo el metodo Menu para poder utilizar las demas opciones
            Menu(index)
        else:
            #En caso que el indice no este por debajo del limite, estara llena y no se agregara el valor
            print("Cola llena")
            Menu(index)
    if (opc==2):
        #Si el usuario ingreso 2, se ejecutara el metodo pop despues de verificar algo
        #Se verifica que el indice sea mayor que 0, esto significara que hay por lo menos un valor
        if(index>0):
            #Se llama al metodo pop, que eliminara el valor mas antiguo en la cola
            pop(index)
            index-=1
            Menu(index)
        else:
            #En caso de que no haya algun valor en la cola, quiere decir que esta vacia
            #Se le notificara de esto al usuario y se llamara de nuevo al metodo Menu
            print("Cola vacia")
            Menu(index)
    if (opc==3):
        #Si ingresa la opcion 3, se le mandara el subMenu de peek
        peek(index)
    if(opc==4):
        #Al ingresar 4, termina el programa
        print("Fin del programa")
    elif(opc<1 or opc>4):
        #Si ingreso una opcion distinta a las establecidas, se le mostrara un mensaje de error
        #Y se le regresara al menu
        print("Ingreso una opcion invalida")
        Menu(index)  
Menu(index)   
