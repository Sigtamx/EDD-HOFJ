array=[5, 4, 7, 2, 9, 1, 3, 6, 8]
#Se crea un arreglo con unos valores cualquiera
#Se muestra el arreglo
print("Arreglo original")
print(array)

#Metodo de ordenamiento burbuja
#Se manda como parametro el arreglo y el numero 0
def Burbuja(array, n):
    #Se verifica que este 0, que es un contador para evitar que se cicle infinitamente
    #No sea mayor que la longitud del arreglo
    if n<len(array):
        #Si es menor, se aumenta en uno
        n+=1
        for i in range(len(array)-1):
            #Ciclo for que va de 0 a la longitud del arreglo menos 1
            #Se verifica si el valor en el indice actual es mayor al valor en el indice siguiente
            if(array[i]>array[i+1]):
                #De ser asi, se crea una variable auxiliar "aux"
                #Se guarda el valor del indice actual aqui
                aux=array[i]
                #Luego el valor del siguiente indice se guarda en el indice actual
                array[i]=array[i+1]
                #Por ultimo, el valor guardado en auxiliar se guarda en el siguiente indice
                array[i+1]=aux
                #Lo que se hizo fue simplemente cambiar de lugar estos datos
        #Se vuelve a llamar al arreglo para que ahora haga el mismo recorrido pero con otro dato
        Burbuja(array, n)
    else:
        #Cuando n sobrepase la longitud del arreglo, habra terminado el ordenamiento
        #Se imprimira el arreglo para mostrar esto
        print("Arreglo ordenado")
        print(array)
        
Burbuja(array, 0)