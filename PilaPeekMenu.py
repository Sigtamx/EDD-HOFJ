pila = []
size = 5

def push(Valor):
    if len(pila) < size:
        pila.append(Valor)
        print("Valor ingresado")
    else:
        print("Pila llena")
        
def peek():
    print("Ingrese la opcion deseada peek")
    print("Ingrese 1 para ver valor tope")
    print("Ingrese 2 para ver todos los valores")
    print("Ingrese 3 para buscar un valor manualmente")
    opc = input()
    if(opc==1):
        #Peek tope
        if 0 < len(pila):
            print("Tope de pila:")  
            print(pila[len(pila)-1])
            print("Indice:")
            print(len(pila)-1)
            
        else:
            print("Pila vacia")
    if(opc==2):
        #Peek All
        if 0 < len(pila):
            print("Los valores de la pila son estos")
            for Num in pila:
                print(Num)
    if(opc==3):
        #Peek Request
        if 0 < len(pila):
            print("Ingrese el valor que desea buscar:")
            i = input()
            for Num in pila:
                if (Num==i):
                    print("El valor se encuentra en el indice")
                    print(pila.index(Num))
                    Menu()
            
            print("Valor no encontrado")
        
def pop():
    if 0 < len(pila):
        print("Valor del tope de la pila:")
        print(pila[len(pila)-1])
        del(pila[len(pila)-1])
    else:
        print("Pila vacia")
    
    
def Menu():
    print("Menu de pila")
    print("Ingrese numero 1 para la opcion push")
    print("Ingrese numero 2 para la opcion pop")
    print("Ingrese numero 3 para la opcion peek")
    print("Ingrese numero 4 para salir")
    opc = input()
    if (opc==1):
        print("Ingrese el numero que desea ingresar a la pila")
        i = input()
        push(i)
        Menu()
    if (opc==2):
        pop()
        Menu()
    if (opc==3):
        peek()
        Menu()
        

Menu()

        