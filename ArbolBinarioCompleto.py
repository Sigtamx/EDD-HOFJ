class Nodo(object):
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

#Se inicia la raiz como un campo vacio
r=Nodo("_")

#Metodo para agregar nodos, toma como parametro la raiz, que es donde comenzara a recorrer
#Y despues ira cambiando conforme se necesite
#Y el dato que se le pondra al nodo a crear
def Push(nodo, dat):
    global r
    #Se le da la opcion de añadir el nodo a la izquierda o derecha del nodo parametro
    #O regresar al menu principal
    print("Ingrese 1 para añadir el nodo a la izquierda de " + nodo.data)
    print("Ingrese 2 para añadir el nodo a la derecha de " + nodo.data)
    print("Ingrese 3 para regresar.")
    opc=raw_input()
    if(opc=="1"):
        #Si ingresa 1(añadir el nodo a la izquierda)
        #Se verificara que el .left del nodo en el que se encuentra, este vacio
        #De ser asi, creara el nodo y lo enlazara sin problemas
        #Por el contrario, se movera al nodo que este ocupando .left
        #Se le informara al usuario que se le movio al siguiente nodo 
        #Y se le enviara de regreso al principio de este metodo
        #Y ahora el parametro "nodo" sera el que estaba ocupando .left
        if(nodo.left==None):
            p=Nodo(dat)
            nodo.left=p
            print("Nodo agregado exitosamente")
        else:
            nodo=nodo.left
            print("Esta posicion esta ocupada, ahora se encuentra en " + nodo.data)
            Push(nodo, dat)
    elif(opc=="2"):
        #Si ingresa 2(añadir el nodo a la derecha)
        #Se verificara que el .right del nodo en el que se encuentra, este vacio
        #De ser asi, creara el nodo y lo enlazara sin problemas
        #Por el contrario, se movera al nodo que este ocupando .right
        #Se le informara al usuario que se le movio al siguiente nodo 
        #Y se le enviara de regreso al principio de este metodo
        #Y ahora el parametro "nodo" sera el que estaba ocupando .right
        if(nodo.right==None):
            p=Nodo(dat)
            nodo.right=p
            print("Nodo agregado exitosamente")
        else:
            nodo=nodo.right
            print("Esta posicion esta ocupada, ahora se encuentra en " + nodo.data)
            Push(nodo, dat)
    elif(opc=="3"):
        #Si ingresa 3(regresar al menu), volvera sin problemas al menu principal
        print("De regreso al menu")
        Menu(r)
    else:
        #Si ingresa una opcion distinta a las disponibles, se le mostrara un mensaje
        #Y se le regresara al principio de este metodo
        print("Ingreso una opcion invalida")
        Push(nodo, dat)

#Metodo menu principal
#Al inicio toma como parametro la raiz
def Menu(nodo):
    global r
    #Si el .data de la raiz, sigue siendo el valor con el que se creo por default
    #Se le hara al usuario crear una y se reemplazara la antigua
    #Entonces podra acceder al resto del menu
    if(r.data=="_"):
        print("Ingrese el dato para la raiz")
        dato=raw_input()
        print("Raiz creada exitosamente")
        r=Nodo(dato)
        Menu(r)
    else:
        #Se le pregunta al usuario si desea añadir mas nodos o terminar la ejecucion        
        print("Ingrese 1 para agregar otro nodo")
        print("Ingrese 2 para salir")
        opm=raw_input()
        if(opm=="1"):
            #Si desea crear mas nodos,
            #Se le pide al usuario el dato con el que creara un nuevo nodo
            #Luego se llama al menu
            print("Ingrese el dato del nodo que desea crear")
            dat=raw_input()
            Push(r, dat)
            Menu(r)
        elif(opm=="2"):
            #De lo contrario, simplemente terminara el programa
            print("Fin del programa")
            exit
        else:
            #Si ingresa algun valor invalido, se le notificara de esto y se regresara al inicio del menu
            print("Ingreso una opcion invalida")
            Menu(r)

Menu(r)


#Metodo para recorrer el nodo a su .left, siempre y cuando este no sea None
def GoLeftPre(nodo):
    if(nodo.left!=None):
        nodo=nodo.left
        Pre(nodo)

#Metodo para recorrer el nodo a su .right, siempre y cuando este no sea None
def GoRightPre(nodo):
    if(nodo.right!=None):
        nodo=nodo.right
        Pre(nodo)
      
#Metodo para recorrer todo el arbol en PreOrden
#Primero imprimira la raiz 
#Despues recorrera el subarbol izquierdo
#Y al final recorrera el subarbol derecho
def Pre(nodo):
    print(nodo.data)
    GoLeftPre(nodo)
    GoRightPre(nodo)

print("Recorrido PreOrden")    
Pre(r)


#Metodo para recorrer el nodo a su .left, siempre y cuando este no sea None
def GoLeftIno(nodo):
    if(nodo.left!=None):
        nodo=nodo.left
        Ino(nodo)

#Metodo para recorrer el nodo a su .right, siempre y cuando este no sea None
def GoRightIno(nodo):
    if(nodo.right!=None):
        nodo=nodo.right
        Ino(nodo)
    
#Metodo para recorrer todo el arbol en InOrden
#Primero recorrera el subarbol izquierdo
#Despues imprimira la raiz   
#Y al final recorrera el subarbol derecho
def Ino(nodo):
    GoLeftIno(nodo)
    print(nodo.data)
    GoRightIno(nodo)
 
print("Recorrido InOrden")    
Ino(r)


#Metodo para recorrer el nodo a su .left, siempre y cuando este no sea None
def GoLeftPos(nodo):
    if(nodo.left!=None):
        nodo=nodo.left
        Pos(nodo)

#Metodo para recorrer el nodo a su .right, siempre y cuando este no sea None
def GoRightPos(nodo):
    if(nodo.right!=None):
        nodo=nodo.right
        Pos(nodo)
        
#Metodo para recorrer todo el arbol en PostOrden
#Primero recorrera el subarbol izquierdo
#Despues recorrera el subarbol derecho 
#Al final imprimira la raiz
def Pos(nodo):
    GoLeftPos(nodo)
    GoRightPos(nodo)
    print(nodo.data)
    
print("Recorrido PostOrden")    
Pos(r)
