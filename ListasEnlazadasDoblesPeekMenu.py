#Clase que crea al nodo con sus campos data, next y prev
class Nodo(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

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
        
#Metodo para crear nodos y enlazarlos en la lsita
def push(data):
    global q
    global p
    #Si el campo de la variable frontal(q) esta vacio, se agrega un nodo aqui
    if(q.next==None):
        #Se crea y posteriormente se enlaza el nodo con el nodo previo
        p=Nodo(data)
        q.next=p
        p.prev=q
        q=p
        
#Metodo para leer la lista de izquierda a derecha
def peekIzqDer(I):
    #Se le manda como parametro la raiz para que se recorran desde este mismo
    #Imprime el dato que se encuentra en el nodo parametro
    print(I.data)
    #Despues de esto verifica si hay un nodo despues de si mismo
    if(I.next!=None):
        #De ser asi, recorrera el nodo al siguiente y se llamara a si mismo
        I=I.next
        peekIzqDer(I)
    else:
        #En caso de que ya no haya mas nodos, habra terminado el recorrido
        print("Fin de la cola")

#Metodo para leer la lista de derecha a izquierda        
def peekDerIzq(D):
    #Se le manda como parametro la variable auxiliar q
    #q siempre esta al final del arreglo, por lo tanto al recorrerlo en reversa
    #Mostrara todos los nodos
    print(D.data)
    #Imprime el dato del nodo en el que se encuentra
    #Verifica si hay un nodo que le preceda
    if(D.prev!=None):
        #De ser asi, se recorrera hacia atras y se llamara a si mismo
        D=D.prev
        peekDerIzq(D)
    else:
        #En caso contrario, llego al principio de la lista y termino el recorrido
        print("Fin de la cola")
        
#Metodo para buscar un dato entre todos los nodos
def peekSearch(S, data):
    #Se manda la raiz como parametro S para recorrer la lista desde el principio
    #Verifica si el dato en el nodo S es igual al dato buscado
    if(S.data==data):
        #De ser asi, solo mencionara que lo encontro
        print("Dato encontrado")
    elif(S.next==None):
        #Si no hay mas nodos frente a S, quiere decir que se termino el recorrido
        #Y no se encontro el dato entre los nodos existentes
        #Por lo tanto el dato no esta en la lsita
        print("Dato no encontrado")
    else:
        #Si aun hay nodos por recorrero y no se ha encontrado el dato
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
    #Se guarda en P el valor siguiente de t
    #Se verifica si el valor a eliminar esta en la raiz
    if(Val==r.data):#pop para la raiz
        #De ser asi se movera al nodo q donde r para auxiliar con los movimientos
        t=r
        #Acto seguido se verifica si no hay nodo siguiente
        if(t.next==None):
            #En caso de esto, quiere decir que el nodo eliminado era el unico
            #Se regresa a su valor vacio para activar el menu inicial
            r.data="_"
            print("Se elimino el unico nodo existente")
        else:
            #En caso de que haya mas nodos, la raiz se guarda en el siguiente de t
            #Basicamente, t y r apuntan a la raiz
            #Entonces, r se mueve al siguiente nodo
            #Luego se elimina el enlace de r hacia atras, y t se apunta al nuevo r
            #Ahora nada apunta a la raiz original, por lo tanto eliminandola 
            #Y creando una raiz nueva en el siguiente nodo
            r=t.next
            r.prev=None
            print("Se destruye la raiz pero la nueva raiz es el siguiente dato")
            t=r     
    elif(p==None and t.data!=Val):
        #En caso de que el dato no se encuentre en la raiz
        #Se verifica si el siguiente nodo esta vacio y que el dato no se enccuentre en el nodo actual
        #Si se cumplen ambas, se habra terminado el recorrido y no se habra encontrado el dato
        #Por lo tanto, el dato no se encuentra en la lsita
        print("El dato no se encuentra en ningun nodo")
    elif(Val==p.data):
        #Se verifica si el dato a eliminar se encuentra en el nodo siguiente
        #De ser asi, se hara lo siguiente
        print("El valor se ha destruido")
        #El dato a eliminar esta en p
        #El dato anterior a p, enlaza su next al next de p
        #Haciendo un puente sobre p, excluyendolo
        p=t.next
        t.next=p.next
        #Se verifica que haya un nodo despues del nodo a eliminar
        if(p.next!=None):
            #En caso de que si, el enlace prev del nodo siguiente de p, se enlaza con t
            #t es en este caso el nodo anterior al eliminado
            #De esta manera, los enlaces se reestablecieron excluyendo al nodo que contiene al valor
            (t.next).prev=t
        else:
            #Si no hay un nodo despues del eliminado, se igualara a None
            #El enlace next del nodo previo al nodo eliminado
            q=p.prev
            t.next=None
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
    #Por lo tanto se le manda a este pequeño menu que solo le da dos opcioens
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
        print("Ingrese 2 para ver todos los nodos de izquierda a derecha")
        print("Ingrese 3 para ver todos los nodos de derecha a izquierda")
        print("Ingrese 4 para buscar un nodo manualmente")
        print("Ingrese 5 para eliminar un Nodo")
        print("Ingrese 6 para salir")
        opc=input()
        if(opc==1):
            #En caso de seleccionar push, se le pedira el dato a ingresar al usuario
            #Luego se llamara al metodo push con el dato como parametro
            #Para terminar se llamara al menu de nuevo, para que pueda usar otras opciones
            Dato=raw_input("Ingrese el dato con el que creara al nodo\n")
            push(Dato)
            menu()
        if(opc==2):
            #Si selecciona recorrer de izquierda a derecha
            #Se llamara al recorrido izq-der con la raiz como parametro
            #Esto hara que lo recorra desde el primer nodo hasta el ultimo
            peekIzqDer(r)
            menu()
        if(opc==3):
            #Si selecicona recorrer de derecha a izquierda
            #Se llamara al recorrido der-izq con el ultimo nodo como parametro
            #Asi recorrera desde el nodo final hasta la raiz
            peekDerIzq(q)
            menu()
        if(opc==4):
            #En caso de seleccionar buscar un nodo manualmente
            #Se le pedira al usuario que ingrese el dato que desea buscar
            #Luego se llamara al metodo Search con la raiz como parametro
            #Asi se recorrera desde el principio hasta el final
            Dato=raw_input("Ingrese el dato que desea buscar\n")
            peekSearch(r, Dato)
            menu()
        if(opc==5):
            #Si selecciona eliminar un nodo, se le pedira el dato que desea eliminar
            #Se mandara el dato y la raiz como parametros, asi recorrera todos los nodos
            Dato=raw_input("Ingrese el nodo que desea eliminar\n")
            pop(Dato, r)
            menu()
        if(opc==6):
            #Si selecciona salir, simplemente no se ejecutaran mas metodos y terminara la ejecucion
            print("Fin del programa")
        if(opc<1 or opc>6):
            #Si selecciona una opcion distinta a las establecidas, mostrara un error
            print("Ingreso un dato invalido")
            menu()

menu()

