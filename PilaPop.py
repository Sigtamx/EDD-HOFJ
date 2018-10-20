pila = []
size = 5

def push(Valor):
    if len(pila) < size:
        pila.append(Valor)
        print("Valor ingresado")
    else:
        print("Pila llena")
          
def pop():
    if 0 < len(pila):
        print("Valor del tope de la pila:")
        print(pila[len(pila)-1])
        del(pila[len(pila)-1])
    else:
        print("Pila vacia")

push(5)
push(10)
push(15)
push(20)
push(25)
push(30)
pop()
pop()
pop()
pop()
pop()
pop()
pop()