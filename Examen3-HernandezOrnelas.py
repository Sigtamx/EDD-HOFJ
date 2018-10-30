class Nodo(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
r=Nodo("_")
q=r
p=q

def push(data):
    global q
    global p
    global r
    #Se verifica si es el primer dato que se ingresara
    if(r.data=="_"):
        #De ser asi, se reescribira el nodo ya creado con el nuevo valor
        r.data=data
    elif(q.next==None):
        #En caso de que no sea asi, se creara un nodo nuevo con este valor
        #Y se haran los enlaces necesarios para mantener la estructura
        p=Nodo(data)
        q.next=p
        p.prev=q
        q=p
        
def peekDerIzq(q):
    #Se imprime el valor en el puntero q
    print(q.data)
    #Si el nodo siguiente al puntero q no esta vacio
    if(q.next!=None):
        #Se recorre el puntero q a ocupar su posicion y el metodo se ejecuta
        q=q.next
        peekDerIzq(q)
    else:
        #Si el siguiente nodo esta vacio, se habra terminado el recorrido
        print("Fin de la cola")
        
def peekIzqDer(p):
    #Se imprime el valor en el puntero p
    print(p.data)
    #Si el nodo previo al puntero p no esta vacio
    if(p.prev!=None):
        #Se recorrera el puntero p a su espacio anterior y se llamara a la funcion de nuevo
        p=p.prev
        peekIzqDer(p)
    else:
        #En caso de que este vacio el nodo anterior, se habran acabado los nodos y el recorrido
        print("Fin de la cola")
        
def peekSearch(q, data):
    #Si el dato en el puntero q es igual al dato que el usuario busca
    #Le informara que el dato que busca se encontro
    if(q.data==data):
        print("Dato " + str(data) + " encontrado")
    elif(q.next==None):
        #En caso de que el enlace next del puntero q este vacio
        #Esto significa que no hay mas valores y no se encontro el dato
        print("Dato " + str(data) + " no encontrado")
    else:
        #Si no se encuentra el dato y no se han terminado de recorrer todos
        #El puntero se recorrera un nodo a la vez hasta encontrar el dato o llegar al final
        q=q.next
        peekSearch(q, data)
        
def pop(Val, t):
    global r
    p=t.next
    #Se verifica si el valor que quiere eliminar el usuario es la raiz
    if(Val==r.data):
        #En caso de que asi sea, se verifica si el valor siguiente esta vacio
        global q
        q=r
        if(q.next==None):
            #Si esta vacio quiere decir que no hay mas nodos
            r.data="_"
            print("Se elimino el unico nodo existente")
        else:
            #Si hay un dato en el siguiente nodo, se recorre la raiz a dicho dato
            print("Se destruye la raiz(Dato "+str(r.data)+")\nPero la nueva raiz es el dato "+ str((r.next).data))
            r=q.next
            q=r
            r.prev=None
    elif(p==None and t.data!=Val):
        #En caso de que se terminen los datos y no lo encontro el metodo
        #Quiere decir que no se encuentra en la lista
        print("El dato "+ str(Val)+" no se encuentra en ningun nodo")
    elif(Val==p.data):
        #En caso de que el valor sea igual al puntero p
        #Esto significara que el valor se encontro y se eliminaran los enlaces hacia este nodo
        print("El valor "+ str(Val)+" se ha eliminado")
        p=t.next
        (p.next).prev=t
        t.next=p.next  
    else:
        #En caso de que nada de esto se cumpla, se recorrera el puntero t
        #Asi recorriendo todos los nodos existentes actualmente
        t=t.next
        pop(Val, t)  
            
            
#El conjunto de datos siguiente debe ser incluido en una lista doblemente enlazada:
    #1, 2, 3, 4, 5, 6, 7, 8, 9
    
push(1)
push(2)
push(3)
push(4)
push(5)
push(6)
push(7)
push(8)
push(9)
#Leer la lista de izquierda a derecha
peekIzqDer(p)

#Leer la lista de derecha a izquierda
peekDerIzq(r)

#Insertar: 10, 11, 13
push(10)
push(11)
push(13)

#Eliminar: 8, 1
pop(8, r)
pop(1, r)

#Leer raiz
print(r.data)

#Leer final de la lista lado derecho y lado izquierdo
print(r.data)
print(p.data)

#Buscar: 0, 7, 8, 1
peekSearch(r, 0)
peekSearch(r, 7)
peekSearch(r, 8)
peekSearch(r, 1)

#Verificacion de que se eliminaron y agregaron datos correctamente
#peekDerIzq(r)
#peekIzqDer(p)