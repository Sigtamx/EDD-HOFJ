
array=[]

def Crear(size=50):
    for i in range(1, size):
        array.append(i)
    return array

array=Crear()
print(array)

#Recorre el arreglo valor por valor hasta encontrar el objetivo
def Lineal(Val, array):
    for i in array:
        if(Val==i):
            #Regresa el valor del indice donde se encuentra el objetivo
            print("Valor encontrado en indice: " + str(array.index(Val)))
            return array.index(Val)
    #Si no lo encuentra le informara de esto al usuario
    print("Valor no encontrado en el arreglo ordenado")
    
Lineal(15, array)

print("Mejor caso:")
Lineal(1, array)
print("Peor caso:")
Lineal(49, array)
