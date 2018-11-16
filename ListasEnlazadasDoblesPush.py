class Nodo(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None       

r=Nodo("_")
q=r
p=q

def Raiz():
    Dato=raw_input("Ingrese el dato con el que creara la raiz\n")
    if(Dato=="_" and q.next==None):
        print("Ingrese un nombre distinto por favor")
        Raiz()
    else:
        global r
        r.data=Dato
        
def push(data):
    global q
    global p
    if(q.next==None):
        p=Nodo(data)
        q.next=p
        p.prev=q
        q=p


        
Raiz()
for i in range(1, 5):
    push(i)

def Verificacion(t):
    print(t.data)
    if(t.next!=None):
        t=t.next
        Verificacion(t)
    else:
        print("Fin")

Verificacion(r)