#Clase que crea al nodo con sus campos data y next
class Nodo(object):
    def __init__(self, data):
        self.data = data
        self.next = None

#Se crea un nodo con un espacio vacio para mejorar la interfaz del menu
#Asi, el usuario solo podra seleccionar las opciones que tienen sentido al inicio
#(No tiene sentido que quiera eliminar un nodo si no ha creado ninguno)
#Se crean variables auxiliares que facilitaran la lectura, agregado y eliminado de nodos        

r=Nodo("_")
q=r
p=q

#Metodo para renombrar la raiz, haciendo creer al usuario que se esta creando desde cero
def Raiz():
    Dato=raw_input("Ingrese el dato con el que creara la raiz\n")
    if(Dato=="_" and q.next==None):
        #Se verifica que este ingresando un nombre distinto al auxiliar
        print("Ingrese un nombre distinto por favor")
        Raiz()
    else:
        #En caso de que sea distinto, se reescribe el nombre y se llama al menu
        global r
        r.data=Dato
        menu()
        
#Metodo para crear nodos y enlazarlos en la lista
def push(data):
    global q
    global p
    global r
    #Si el campo de la variable frontal(q) esta vacio, se enlaza a la raiz
    #Esto sirve al crear el primer nodo despues de la raiz
    if(q.next==None):
        q.next=r
    if(q.next==r):
        #Se crea y posteriormente se enlaza el nodo previo al nodo nuevo
        #Y el nodo nuevo a la raiz
        p=Nodo(data)
        q.next=p
        q=p
        q.next=r
        
#Metodo para leer la lista 
def peek(I):
    #Se le manda como parametro la raiz para que se recorran desde este mismo
    #Imprime el dato que se encuentra en el nodo parametro
    print(I.data)
    #Despues de esto verifica que el siguiente dato no sea la raiz
    if(I.next!=r):
        #De ser asi, recorrera el nodo al siguiente y se llamara a si mismo
        I=I.next
        peek(I)
    else:
        #En caso de que el siguiente dato sea la raiz, habria llegado al final de la lista
        print("Fin de la lista")

#Metodo para buscar un dato entre todos los nodos
def peekSearch(S, data):
    #Se manda la raiz como parametro S para recorrer la lista desde el principio
    #Verifica si el dato en el nodo S es igual al dato buscado
    if(S.data==data):
        #De ser asi, solo mencionara que lo encontro
        print("Dato encontrado")
    elif(S.next==r):
        #Si el nodo frente a S es la raiz, quiere decir que se termino el recorrido
        #Y no se encontro el dato entre los nodos existentes
        #Por lo tanto el dato no esta en la lista
        print("Dato no encontrado")
    else:
        #Si aun hay nodos por recorrer y no se ha encontrado el dato
        #Se recorrera el nodo para ver otro dato y se llama a si mismo
        S=S.next
        peekSearch(S, data)
        
#Metodo para eliminar nodos de la lista
def pop(Val, t):
    #El parametro t es el nodo raiz, se manda asi para no afectar a la raiz real
    #Se manda como parametro el valor que se quiere eliminar y el parametro t
    #Aqui se llama al nodo raiz, ya que se usara para el unico caso de que
    #El nodo a eliminar sea el de la raiz
    global r
    global q
    p=t.next
    #Se guarda en p el valor siguiente de t
    #Se verifica si el valor a eliminar esta en la raiz
    if(Val==r.data):
        #De ser asi se movera al nodo t donde r para auxiliar con los movimientos
        t=r
        #Acto seguido se verifica si el enlace next es el mismo
        #Esto quiere decir que es el unico dato
        if(t.next==r):
            #En caso de esto, quiere decir que el nodo eliminado era el unico
            #Se regresa a su valor vacio para activar el menu inicial
            r.data="_"
            print("Se elimino el unico nodo existente")
        else:
            #En caso de que sea un nodo distinto, la raiz se guarda en el siguiente de t
            #Basicamente, t y r apuntan a la raiz
            #Entonces, r se mueve al siguiente nodo y t lo sigue
            #Ahora nada apunta a la raiz original, por lo tanto eliminandola 
            #Y creando una raiz nueva en el siguiente nodo
            #Se enlaza el .next del ultimo nodo con la nueva raiz para preservar la estructura
            r=t.next
            print("Se destruye la raiz pero la nueva raiz es el siguiente dato")
            t=r   
            q.next=r
    elif(p==r and t.data!=Val):
        #En caso de que el dato no se encuentre en la raiz
        #Se verifica si el siguiente nodo es la raiz y que el dato no se encuentre en el nodo actual
        #Si se cumplen ambas, se habra terminado el recorrido y no se habra encontrado el dato
        #Por lo tanto, el dato no se encuentra en la lista
        print("El dato no se encuentra en ningun nodo")
    elif(Val==p.data):
        #Se verifica si el dato a eliminar se encuentra en el nodo siguiente
        #De ser asi, se hara lo siguiente
        #El dato a eliminar esta en p
        #El dato anterior a p, enlaza su next al next de p
        #Haciendo un puente sobre p, excluyendolo
        print("El valor se ha destruido")
        p=t.next
        t.next=p.next
    else:
        #En caso de que no se haya encontrado el dato y aun haya nodos por recorrer
        #t se movera al nodo siguiente y se llamara a si mismo para continuar recorriendo
        t=t.next
        pop(Val, t)   
   
#Metodo menu, donde el usuario podra interactuar de manera controlada con los metodos
def menu():
    global r
    global q
    #Si la raiz tiene el dato vacio, quiere decir que el usuario no ha creado nada
    #Por lo tanto se le manda a este pequeño menu que solo le da dos opciones
    #Crear una raiz o salir del programa
    if(r.data=="_"):
        print("Ingrese 1 para crear una raiz")
        print("Ingrese 2 para salir")
        opk=input()
        #Si decide crear una raiz para la lista, se llamara al metodo raiz
        if(opk==1):
            Raiz()
        #Si decide salir, simplemente finalizara el programa
        if(opk==2):
            print("Fin del programa")
        #En caso de ingresar una opcion no disponible, se mostrara un error
        elif(opk<1 or opk>2):
            print("Ingreso una opcion invalida")
            menu()
    else:   
        #Despues de crear una raiz, se podra acceder al menu completo
        #Con las opciones de crear nodos, ver todos los nodos
        #Buscar un nodo por medio del dato que contiene
        #Eliminar un nodo por medio del dato que contiene y salir del programa
        print("Ingrese 1 para crear un Nodo")
        print("Ingrese 2 para ver todos los nodos")
        print("Ingrese 3 para buscar un nodo manualmente")
        print("Ingrese 4 para eliminar un Nodo")
        print("Ingrese 5 para salir")
        opc=input()
        if(opc==1):
            #En caso de seleccionar push, se le pedira el dato a ingresar al usuario
            #Luego se llamara al metodo push con el dato como parametro
            #Para terminar se llamara al menu de nuevo, para que pueda usar otras opciones
            Dato=raw_input("Ingrese el dato con el que creara al nodo\n")
            push(Dato)
            menu()
        if(opc==2):
            #Si selecciona recorrer todos los nodos
            #Se llamara al recorrido con la raiz como parametro
            #Esto hara que lo recorra desde el primer nodo hasta el ultimo
            peek(r)
            menu()
        if(opc==3):
            #En caso de seleccionar buscar un nodo manualmente
            #Se le pedira al usuario que ingrese el dato que desea buscar
            #Luego se llamara al metodo Search con la raiz como parametro
            #Asi se recorrera desde el principio hasta el final
            Dato=raw_input("Ingrese el dato que desea buscar\n")
            peekSearch(r, Dato)
            menu()
        if(opc==4):
            #Si selecciona eliminar un nodo, se le pedira el dato que desea eliminar
            #Se mandara el dato y la raiz como parametros, asi recorrera todos los nodos
            Dato=raw_input("Ingrese el nodo que desea eliminar\n")
            pop(Dato, r)
            menu()
        if(opc==5):
            #Si selecciona salir, simplemente no se ejecutaran mas metodos y terminara la ejecucion
            print("Fin del programa")
        if(opc<1 or opc>5):
            #Si selecciona una opcion distinta a las establecidas, mostrara un error
            print("Ingreso un dato invalido")
            menu()

menu()

