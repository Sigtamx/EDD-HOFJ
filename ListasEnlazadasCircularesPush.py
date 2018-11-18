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
        
push(5)
push(10)
push(15)

print(r.data)#Imprime raiz
print((r.next).data)#Imprime dato siguiente a la raiz
print(q.data)#Imprime ultimo dato
print((q.next).data)#Imprime el dato del siguiente nodo del ultimo(osea la raiz)

