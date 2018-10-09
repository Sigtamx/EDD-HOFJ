"""
Desplegar y calcular valor fibonacci de un numero dado por el usuario con recursividad
"""

Display=1
k=0
def fiboRecursivo(n):
    global Display
    global k
    if(n>1):
        
        Display=Display+k
        k=Display-k
        n-=1
        fiboRecursivo(n)
    else:
        print("El valor que se encuentra en esa posicion es:")
        print(Display)
        print("Fin")
        
print("Ingrese el numero para usar fibonacci:")
n = input()
fiboRecursivo(n)


"""
Desplegar y calcular valor fibonacci de un numero dado por el usuario con iteraciones
"""

def fiboIterativo(n):
    m=1
    k=0
    for i in range(n-1):
        m=(m+k)
        k=m-k
    print("El valor que se encuentra en esa posicion es:")
    print(m)
    print("Fin")
    
print("Ingrese el numero para usar fibonacci:")
n = input()
fiboIterativo(n)