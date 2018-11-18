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
     
push(5)
push(15)
push(10)
print(r.data)
print((r.next).data)
print(q.data)
