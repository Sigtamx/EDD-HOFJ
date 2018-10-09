"""
Desplegar los primeros 100 numeros naturales sin iteradores
"""
n=0
def naturales(n):
    if(n<=100):
        print(n)
        naturales(n+1)
    else:
        print("Fin")

naturales(n)