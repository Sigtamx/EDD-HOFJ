array=[5, 4, 7, 2, 9, 1, 3, 6, 8]
#Se crea un arreglo con unos valores cualquiera
#Se muestra el arreglo
print("Arreglo original")
print(array)

#Metodo de ordenamiento QuickSort
#Se manda como parametro el arreglo y la mitad del arreglo, que se suara como pivote
def QuickSort(array, Mitad):
    #Se tiene k, que servira para ordenar la segunda mitad del arreglo
    #Ya que si el arreglo es de longitud impar, la mitad no sera exacta
    Impar=0
    #Se verifica si el arreglo es impar, de ser asi se aumenta k 
    if(Mitad*2!=len(array)):
        Impar=1
    #El valor en el medio del arreglo se guarda en pivote
    Pivote=array[Mitad]
    
    #print(array)
    
    #Ciclo for que se recorrera tantas veces como la mitad del arreglo
    for i in range(Mitad):
        #Se verifica si el pivote es menor que el valor en el subarreglo antes de si mismo
        if(Pivote<array[i]):
            #De ser asi, se cambian de lugar
            aux=Pivote
            array[array.index(Pivote)]=array[i]
            array[i]=aux
            #Despues de hacer este cambio, se vuelve a llamar a QuickSort
            QuickSort(array, Mitad)
            
        elif(array[i]>array[i+1]):
            #Si el pivote no es mayor, se verifica cual es mayor entre estos valores
            #Si un numero es mayor que el siguiente, entonces se cambian de lugar
            aux=array[i]
            array[i]=array[i+1]
            array[i+1]=aux
    #CIclo for que se recorrera tnntas veces como la mitad del arreglo
    for i in range(Mitad):
        #Se verifica si el pivote es mayor que el valor en el subarreglo despues de si mismo
        #Aqui es donde se usa la auxiliar k, ya que sin ella se podria desbordar
        #O podria no compararse con el ultimo valor del arreglo
        if(Pivote>array[i+Mitad+Impar]):
            #De ser asi, cambiaran de lugar
            aux=Pivote
            array[array.index(Pivote)]=array[i+Mitad+Impar]
            array[i+Mitad+Impar]=aux
            #Despues de hacer este cambio, se vuelve a llamar a QuickSort
            QuickSort(array, Mitad)

#Se ejecuta el arreglo y se manda como parametros el arreglo y la mitad de su longitud
QuickSort(array, len(array)/2)
#Se imprime el arreglo ordenado
print("Arreglo ordenado")
print(array)