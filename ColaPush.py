
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
        
push(10)
push(20)
push(30)
push(40)
push(50)
push(60)