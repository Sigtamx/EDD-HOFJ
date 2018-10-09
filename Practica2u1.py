"""
Desplegar y calcular factorial de un numero dado por el usuario con recursividad
"""

m=1
def factorialRecursivo(n):
    global m
    if(n>1):
        m*=n
        n-=1
        factorialRecursivo(n)
    else:
        print(m)
        print("Fin")
        
print("Ingrese el numero para usar factorial:")
n = input()
factorialRecursivo(n)

"""
Desplegar y calcular factorial de un numero dado por el usuario con iteraciones
"""

def factorialIterativo(n):
    m=n
    for i in range(n-1):
        m*=(n-1)
        n-=1
    print(m)
    print("Fin")
    
print("Ingrese el numero para usar factorial:")
n = input()
factorialIterativo(n)