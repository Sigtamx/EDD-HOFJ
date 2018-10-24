class Nodo(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        
r=Nodo("_")
q=r
p=q

def push(data):
    global q
    global p
    if(q.next==None):
        #q=r
        p=Nodo(data)
        q.next=p
        q=p
        """print(q.data)
        print(p.data)
        print(q.next)
        print(p.next)
        print(data)
        """
        
    else:
        print("Negatorio amigo")
        p = Nodo(data)
        q.next=p
        #q=p
         


def peek():
    global q 
    
    print(q.data)
    if(q.next!=None):
        #print(q.data)
        q=q.next
        #print(q.data)
        peek()
    else:
        print("Fin de la cola")

def peekSearch(q, data):
    #global r
    #if(q.next!=None and r.data!=data):
        if(q.data==data):
            print("Dato encontrado")
        elif(q.next==None):
            print("Dato no encontrado")
        else:
            q=q.next
            peekSearch(q, data)
    #else:
        #print("Dato no encontrado")
        

def pop(Val, t, C):
    if(C<15):
        C+=1
        global r
        #print("I")
        #print(Val)
        #print(r.data)
        #print("J")
        p=t.next
        #q=r
        """if(Val==p.data):#pop para el ultimo dato
            if(q.next==p):
                print("Se destruye la raiz alv")
            else:
                q=q.next
                print("BOTA DE AGUA")
                #pop(Val)"""
        if(Val==r.data):#pop para la raiz
            global q
            q=r
            if(q.next==None):
                r.data="_"
                print("Se elimino el unico nodo existente")
            else:
                r=q.next
                print("Se destruye la raiz pero la nueva raiz es el siguiente dato")
                q=r
        
        elif(p==None and t.data!=Val):
            print("El dato no se encuentra en ningun nodo")
            #q=r
            #pop(Val, q, C)
        elif(Val==p.data):#El valor esta entre datos
            print("El valor se ha destruido")
            #p=q.next
            if(p!=None):
                p=t.next
                t.next=p.next   
                #print("Valio chota el dato")
            else:
                print(2)
        else:
            #print("Dato no encontrado?")
            t=t.next
            pop(Val, t, C)   
    else:
         print("Se ciclo esta vaina loco")
   
def Raiz():
    Dato=raw_input("Ingrese el dato con el que creara la raiz\n")
    if(Dato=="_"):
        print("Ingrese un nombre distinto por favor")
        Raiz()
    else:
        global r
        r.data=Dato
        menu()
def menu():
    global r
    global q
    if(r.data=="_"):
        print("Ingrese 1 para crear una raiz")
        print("Ingrese 2 para salir")
        opk=input()
        if(opk==1):
            Raiz()
            """Dato=input("Ingrese el dato con el que creara la raiz\n")
            if(Dato==""):
                print("Ingrese un nombre por favor")
                menu()
            else:
                r=Nodo(Dato)
                menu()"""
        if(opk==2):
            print("Fin del programa")
        elif(opk<1 or opk>2):
            print("Ingreso una opcion invalida")
            menu()
    else:   
        print("Ingrese 1 para crear un Nodo")
        print("Ingrese 2 para ver todos los nodos")
        print("Ingrese 3 para buscar un nodo manualmente")
        print("Ingrese 4 para eliminar un Nodo")
        print("Ingrese 5 para salir")
        opc=input()
        if(opc==1):
            Dato=raw_input("Ingrese el dato con el que creara al nodo\n")
            push(Dato)
            menu()
        if(opc==2):
            #global q
            #global r
            q=r
            peek()
            menu()
        if(opc==3):
            #global q
            q=r
            Dato=raw_input("Ingrese el dato que desea buscar\n")
            peekSearch(q, Dato)
            menu()
        if(opc==4):
            Dato=raw_input("Ingrese el nodo que desea eliminar\n")
            pop(Dato, q, 0)
            menu()
        if(opc==5):
            print("Fin del programa")
        if(opc<1 or opc>5):
            print("Ingreso un dato invalido")
            menu()

menu()
#val = raw_input("Ingrese un dato\n")
#val = '"' + val + '"'
#peekSearch(q, val)
 
"""    

push("Jo")
push("Jojo")
push("Jojojo")
push("Jo1")
push("Jojo1")
push("Jojojo1")
push("Jo2")
push("Jojo2")
push("Jojojo2")

q=r
#print(q.data)
peek()

 
q=r
pop("Dios", q, 0)
pop("Jo", q, 0)
pop("Jojojo",q, 0)
pop("Jojojo3", q, 0)
pop("Jojo", q, 0)
pop("Jojojo2", q, 0)

print("peek")
peek()
"""


"""
q=r
if q.next!=None:q.next = p.next
    p=Nodo(data)
    q.next=p
    q=p

"""     
    
    
"""
Metodo para crear la raiz o crear la raiz previamente a añadir nodos
r=Nodo("Raiz") < Ejemplo de crear un nodo
Crear metodo tipo push
def push(r):
    p=Nodo(data)
    Verificar si raiz esta conectado a nodo, en caso de que no quiere decir que es el primer nodo despues de la raiz
    if r.next!=None    
    q=p
    r.next = p < algo asi para enlazar la raiz al primer nodo
    q.next=p
    En caso de que no sea el primer nodo(cuando r.next no sea vacio)
    else:
    q=r < tener q en donde la raiz 
    p = Nodo(data)
    q.next = p
    Val==p.data
"""

"""
Peek crear una lista y guardar los valores de la lista enlazada en esa lista y para mostrarlos usar la lista secundaria
"""   

"""borrar el ultimo dato del arreglo
q=r
if(q.next==p)
destroy p 
else
q=q.next




p=q.next
q.next=p.next
destroy p
p=q.next
enlazar brincando un nodo q.next = p.next




eliminar raiz
q=r
r=q.next
destroy q
q=r

"""