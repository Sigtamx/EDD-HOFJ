# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 19:47:38 2018

@author: julianjavier

1. Realizar un programa que entregue el resultado de sumar 1+2+3+4+5+6+7+8+9, utilizando
recursividad

"""

""
#Se verifica que el parametro ingresado a la funcion sea menor o igual que 9, pues queremos que no sobrepase este valor
#Aumentamos el valor del parametro y con recursividad llamamos de nuevo a la funcion con el nuevo valor
#cuando el parametro deje de cumplir con la condicion de ser menor o igual que 9, se imprimira una ecuacion que calcula la suma de todos los valores
def programaUno(num):
    if(num<=9):
        num+=1
        programaUno(num)
    else:
        print(((num)*(num-1))/2)
        
print("Inicio de programa 1")
programaUno(1)
print(1+2+3+4+5+6+7+8+9)#Se muestra que el resultado de la suma es el mismo de la funcion
print("Final de programa 1")

"""

2. Realizar un programa que entregue el resultado de la siguiente ecuacion 2^n 
utilizar recursividad

"""
#Se verifica que el parametro que se usara como exponente sea mayor que 1, luego procede a multiplicar el valor inicial que es 2, por 2
#Acto seguido le resta 1 al parametro para disminuir el exponente y se llama a si mismo
#Cuando el exponente llegue a uno, la recursividad se detendra e imprimira el valor resultante
def programaDos(num, N):
    if(num>1):
        N*=2
        num-=1
        programaDos(num, N)
    else:
        print(N)

print("Inicio de programa 2")
print("Ingrese la potencia a la que desea elevar el numero 2")
n = input()    
programaDos(n, 2)    
print("Final de programa 2")


"""

3. Hacer un programa que lleve el control de versiones de un proyecto en una empresa
la estructura de datos debe controlar el numero de migraciones realizadas en el proyecto.
Utilizar una pila para introducir las migraciones una por una y
obtener las migraciones una por una empezando por la migracion mas actual y 
terminando por la migracion mas antigua.

"""
#Se crea la pila y se inicia el indice en 1
Registro=[]
indice=1

#Funcion para agregar un valor a la pila, se agrega el valor del indice, luego se aumenta dicho valor y se imprime el arreglo
def AgregarV():
    global indice
    Registro.append(indice)
    indice+=1
    print(Registro)

#Funcion para eliminar el valor tope de la pila, se elimina el valor del topo, se imprime el arreglo y se disminuye el indice   
#En caso de estar vacio, mandara un mensaje alternativo
def EliminarV():
    
    if(len(Registro)>0):
        global indice
        del Registro[indice-2]
        print(Registro)
        indice-=1
    else:
        print("Registro de migraciones vacio")

#Funcion para mostrar todos los datos dentro del arreglo, comenzando desde el tope y terminando en el primer valor ingresado        
def VisualizarV():
    print("Todas las migraciones, de la mas reciente a la mas antigua")
    for i in range(len(Registro)):
        print(Registro[len(Registro)-i-1])

#Menu donde se pueden utilizar las anteriores funciones como quiera, y para terminar la ejecucion del programa
#Al terminar de ejecutar cada funcion se llamara de nuevo al menu, aplicando aqui recursividad
#En caso de ingresar una opcion no valida, se mandara una advertencia y se le regresara al menu
def MenuV():
    print("Ingrese 1 para agregar al registro una migracion.")
    print("Ingrese 2 para eliminar el registro de la migracion mas reciente.")
    print("Ingrese 3 para visualizar todo el registro de migraciones en el proyecto.")
    print("Ingrese 4 para salir del sistema.")
    opc = input()
    if(opc==1):
        AgregarV()
        MenuV()
    if(opc==2):
        EliminarV()
        MenuV()
    if(opc==3):
        VisualizarV()
        MenuV()
    if(opc==4):
        print("Fin del programa")
    elif(opc>4 or opc<1):
        print("Ingreso una opcion invalida")
        MenuV()
print("Inicio de programa 3")
MenuV()
print("Final de programa 3")

"""

4. Hacer un programa que simule la fila de clientes de una tienda de super mercado, considerando que
solo hay una caja que esta activa. La fila solo puede tener como maximo 5 clientes!

"""
#Se inicializa la fila con 5 espacios vacios con el metodo create
fila=[]
size=5
actual=0

def crear(fila):
    for i in range(size):
        fila.append("Vacio")
    print(fila)
    
#Funcion para agregar un cliente a la fila, este ocupara el lugar mas cercano al final que este libre
#Se verifica que la posicion mas cerca del final libre no sea mayor a 5, pues solo hay 5 espacios para clientes y esto causaria un error
#Se cambia el estado del espacio de vacio a ocupado, el indice que indica el espacio libre se recorre hacia el principio de la fila
#En caso de que la fila se encuentre llena se mostrara un mensaje de advertencia
def push():
    global actual
    if(actual<5):
        fila[actual]="Ocupado"
        actual+=1
        print(fila)
    else:
         print("Fila de mercado llena")
#Funcion para sacar al cliente del frente de la fila, al primero que ingreso
#Se verifica que la fila no este vacia, ya que no se puede sacar un cliente si no hay y esto causaria un error
#Se recorreran los valores desde el principio de la fila hasta el final, ocupando asi el lugar que se dejo disponible y creando un espacio libre donde termine la fila
#En caso de que la fila se encuentre vacia se mostrara un mensaje de advertencia  
def pop():
    global actual
    if(actual>0):
        act=1
        for i in range(size):
            fila[act-1]=fila[act]
        fila[actual-1]="Vacio"
        
        actual-=1
        print(fila)
    else:
        print("Fila de mercado vacia")
#Funcion para ver si el frente de la fila esta ocupado o vacio
def peek():
    print("Frente de la fila esta")
    print(fila[0])
#Funcion para ver si la fila esta vacia, se regresa un mensaje con el estado de la fila, ya sea vacia o no vacia
def empty():
    if(actual==0):
        print("Fila vacia")
    else:
        print("Fila no vacia")
#Menu donde se podran ejecutar las demas funciones como desee
#Al terminar de ejecutar cada funcion, se llamara de nuevo al menu, aplicando la recursividad
#Se agrega opcion para terminar el programa
#En caso de ingresar una opcion que no se encuentre en el menu disponible, se mandara una advertencia y se regresara al menu        
def Menu():
    print("Ingrese 1 para agregar un cliente a la fila")
    print("Ingrese 2 para desocupar un cliente")
    print("Ingrese 3 para ver si el frente de la fila esta ocupado")
    print("Ingrese 4 para ver si la fila esta vacia")
    print("Ingrese 5 para salir")
    opc=input()
    if(opc==1):
        push()
        Menu()
    if(opc==2):
        pop()
        Menu()
    if(opc==3):
        peek()
        Menu()
    if(opc==4):
        empty()
        Menu()
    if(opc==5):
        print("Fin del programa")
    elif(opc>5 or opc<1):
        print("Ingreso una opcion invalida")
        Menu()
    
print("Inicio de programa 4")
crear(fila)
Menu()
print("Final de programa 4")
""