class Nodo(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        
r=Nodo("")
q=r
p=q

def push(data):
    global q
    global p
    if(r.data==""):
        print("Raiz creada con dato " + str(data))
        r.data=data
    elif(q.next==None):
        print("Dato " + str(data) + " ingresado")
        p=Nodo(data)
        q.next=p
        q=p
        
def pop(Val, t):
    global r
    global q
    p=t.next
    if(Val==r.data):
        t=r
        if(t.next==None):
            r.data=""
            print("Se elimino el unico nodo existente")
        else:
            print("Se destruye la raiz pero la nueva raiz es el siguiente dato")
            r=t.next
            t=r     
    elif(p==None and t.data!=Val):
        print("El dato " + str(Val) + " no se encuentra en ningun nodo")
    elif(Val==p.data):
        print("El valor " + str(Val) + " se ha destruido")
        p=t.next
        t.next=p.next
    else:
        t=t.next
        pop(Val, t)
        
push(5)
push(15)
push(10)
print(r.data)
print((r.next).data)
print(q.data)

pop(15, r) #Se elimina un nodo cualquiera
pop(8, r) #Se intenta eliminar un nodo que no existe
pop(5, r) #Se elimina la raiz y se recorre
pop(10, r) #Se elimina el unico nodo