cola=[]
index=0
size=5

def create():
    for I in range(size):
        cola.append(0)
    return cola
    
create()


def push(Val):
    global index
    if index < size:
        cola[index] = Val;
        print(cola[index])
        #print(index)
        index+=1
    else:
        print("****************Cola llena****************")
        
def pop():
    global index
    if index>0:
        print("Numero eliminado:")
        print(cola[0])
        ind=0
        for I in range(size-1):
            cola[ind]=cola[ind+1]
            ind+=1     
        cola[index-1]=0  
        index-=1
    else:
        print("****************Cola vacia****************")        
        
push(10)
push(20)
push(30)
push(40)
push(50)
push(60)
pop()
pop()
pop()
pop()
pop()
pop()
