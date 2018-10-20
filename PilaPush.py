pila = []
size = 5

def push(Valor):
    if len(pila) < size:
        pila.append(Valor)
        print("Valor ingresado")
    else:
        print("Pila llena")
        
    
push(5)
push(10)
push(15)
push(20)
push(25)
push(30)