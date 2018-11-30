array=[]

def Crear(size=50):
    for i in range(1, size):
        array.append(i)
    return array

array=Crear()
print(array)

#Recorre el arreglo valor por valor hasta encontrar el objetivo
def Lineal(Val, array):
    Mitad=len(array)/2
    print(array)
    if(len(array)==1 and array[0]!=Val):
        print("Valor " + str(Val) + " no encontrado dentro del arreglo")
    elif(array[Mitad]==Val):
        print("Valor encontrado")
        return Val
    elif(array[Mitad]>Val):
        a=[]
        for i in range(Mitad):
            a.append(array[i])
        Lineal(Val, a)
    elif(array[Mitad]<Val):
        a=[]
        for i in range(Mitad, len(array)):
            a.append(array[i])
        Lineal(Val, a)
    #else:
     #   for i in array:
      #      if(i==Val):
       #         print("Valor encontrado")
        #        return Val
         #   else:
          #      print("Valor no encontrado en el arreglo ordenado")

    #Si no lo encuentra le informara de esto al usuario
    
Lineal(25, array)
Lineal(49, array)
Lineal(1, array)
Lineal(150, array)