class Nodo(object):
    def __init__(self, data):
        self.data = data
        self.next = None

r=Nodo("")
q=r
p=r

def push(data):
    global q
    global p
    global r
    if(r.data==""):
        r.data=data
    elif(q.next==None):
        q.next=r
    if(q.next==r):
        p=Nodo(data)
        q.next=p
        q=p
        q.next=r

def pop(Val, t):
    global r
    global q
    p=t.next
    if(Val==r.data):
        t=r
        if(t.next==r):
            r.data="_"
            print("Se elimino el unico nodo existente")
        else:
            r=t.next
            print("Se destruye la raiz pero la nueva raiz es el siguiente dato")
            t=r   
            q.next=r
    elif(p==r and t.data!=Val):
        print("El dato no se encuentra en ningun nodo")
    elif(Val==p.data):
        print("El valor se ha destruido")
        p=t.next
        t.next=p.next
    else:
        t=t.next
        pop(Val, t)        
        
push(5)
push(10)
push(15)

print(r.data)#Imprime raiz
print((r.next).data)#Imprime dato siguiente a la raiz
print(q.data)#Imprime ultimo dato
print((q.next).data)#Imprime el dato del siguiente nodo del ultimo(osea la raiz)


pop(0, r)#Intenta eliminar un nodo no existente
pop(10, r)#Se elimina un nodo cualquiera
pop(5, r)#Se elimina la raiz
pop(15, r)#Se elimina el ultimo nodo