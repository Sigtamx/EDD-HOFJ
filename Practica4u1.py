
#Se crea el metodo para mostrar los 100 primeros valores naturales sin iteradores
def naturales(n):
    #Se verifica que el valor sea menos o igual a 100, ya que solo queremos que vaya hasta 100
    if(n<=100):
        #En caso de que se cumpla esto, se imprimira el numero y se llamara de nuevo al metodo
        #Con la diferencia de que se le mandara como parametro el numero aumentado en uno
        #Asi cambiando el valor que se imprime y llegando al limite
        print(n)
        naturales(n+1)
        
    else:
        #Una vez supera 100, habra terminado el programa
        print("Fin")
        
m=1
#Se crea el metodo para mostrar el factorial de un valor que el usuario ingresara
def factorialRecursivo(n):
    #Se manda a llamar la variable global m, que nos servira como auxiliar
    global m
    #Se verifica que el valor ingresado sea mayor a 1
    #Cualquier numero elevado a la potencia 1 es ese mismo valor
    if(n>1):
        #Si esto es verdadero, la variable auxiliar m se multiplicara por el parametro
        #Luego se ira decrementando de uno en uno el parametro, repitiendo estos pasos
        #Se llama de nuevo al metodo, aplicando recursividad
        m*=n
        n-=1
        factorialRecursivo(n)
    else:
        #Una vez que el parametro ya no es mayor que 1, se detiene e imprime el valor resultante
        print(m)
        print("Fin")
           
Display=1
k=0
#Se crea el metodo para mostrar el valor fibonacci que se encuentra en la posicion que ingresa el usuario
def fiboRecursivo(n):
    global Display
    global k
    #Se verifica que n sea mayor que 1, ya que entonces se terminara la ejecucion del programa
    if(n>1):
        #Display es el valor que se mostrara, k es una variable auxiliar
        #Display se iguala a la suma de Display y K, esto significa que se le aumenta el valor de k
        #K ahora debe cambiar de valor, y este valor es el nuevo display menos el antiguo k
        #n se disminuye uno para ir cerrando la ejecucion
        #Se llama de nuevo al metodo
        Display=Display+k
        k=Display-k
        n-=1
        fiboRecursivo(n)
    else:
        #Se imprime el valor que se encuentra en la posicion que ingreso el usuario
        print("El valor que se encuentra en esa posicion es:")
        print(Display)
        print("Fin")

#Menu donde se podran acceder a los anteriores metodos
def Menu():
    print("Ingrese 1 para desplegar los primeros 100 numeros naturales")
    print("Ingrese 2 para deslegar el factorial de un valor que usted ingresara")
    print("Ingrese 3 para desplegar el valor fibonacci de un valor que usted ingresara")
    print("Ingrese 4 para salir del programa")
    #Se le pide al usuario que ingrese una opcion, la cual lo mandara a cierto metodo
    opc = input()
    if(opc==1):
        #Se llama al metodo y cuando este termine, se llama de nuevo al menu, aplicando recursividad
        naturales(0)
        Menu()
    if(opc==2):
        #Se llama al metodo y cuando este termine, se llama de nuevo al menu, aplicando recursividad
        print("Ingrese el numero para usar factorial:")
        n = input()
        factorialRecursivo(n)
        Menu()
    if(opc==3):
        #Se llama al metodo y cuando este termine, se llama de nuevo al menu, aplicando recursividad
        print("Ingrese el numero para usar fibonacci:")
        n = input()
        fiboRecursivo(n)
        Menu()
    if(opc==4):
        #En caso de ingresar 4, se termina el programa
        print("Fin del programa")
    elif(opc>4 or opc<1):
        #Si se detecta una opcion numerica que no se encuentra disponible
        #Se imprime una advertencia y se manda de regreso al menu
        print("Ingreso una opcion invalida")
        Menu()

Menu()  