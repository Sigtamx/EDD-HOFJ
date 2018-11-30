from random import randint
from time import time

#Creacion de arreglo
def Crear(size=150, max=150):
    return [randint(0, max) for i in range(size)]

#Metodo de ordenamiento Burbuja
def Burbuja(array, n):
    if n<len(array):
        n+=1
        for i in range(len(array)-n):
            if(array[i]>array[i+1]):
                aux=array[i]
                array[i]=array[i+1]
                array[i+1]=aux
        Burbuja(array, n)
    return array
    
#Metodo de ordenamiento QuickSort
def QuickSort(array, MarcIzq, MarcDer):
    Izq = MarcIzq
    Der = MarcDer
    Pivote = array[int((MarcIzq+MarcDer)/2)]
    while Izq <= Der:
        while array[Izq] < Pivote:
            Izq += 1
            
        while array[Der] > Pivote:
            Der -= 1
            
        if Izq <= Der:
            aux = array[Izq]
            array[Izq] = array[Der]
            array[Der] = aux
            Izq += 1
            Der -= 1

    if Der > MarcIzq:
        QuickSort(array,MarcIzq,Der)
        
    if Izq < MarcDer:
        QuickSort(array,Izq,MarcDer)     
        
    return array    


#Metodo de ordenamiento ShellSort           
def ShellSort(array, Mitad):
    if(Mitad==1):
        for i in range(len(array)):
            if i+Mitad<len(array):
                if(array[i]>array[Mitad+i]):
                    aux=array[i]
                    array[i]=array[Mitad+i]
                    array[Mitad+i]=aux
        Mitad=0  
        for i in range(len(array)-1):
            if(i<len(array)):
                if(array[i]>array[i+1]):
                    aux=array[i]
                    array[i]=array[i+1]
                    array[i+1]=aux
    elif(Mitad>1):            
        for i in range(len(array)):
            if i+Mitad<len(array):
                if(array[i]>array[Mitad+i]):
                    aux=array[i]
                    array[i]=array[Mitad+i]
                    array[Mitad+i]=aux
            else:
                Mitad/=2
                break
        ShellSort(array, Mitad)
    return array

#Metodo de ordenamiento Merge
def Merge(Izq, Der):
    Final=[]
    I=0
    D=0
    while I<len(Izq) and D<len(Der):
        if Izq[I]<Der[D]:
            Final.append(Izq[I])
            I+=1
        else:
            Final.append(Der[D])
            D+=1
    if I==len(Izq):
        Final.extend(Der[D:])
    else:
        Final.extend(Izq[I:])
    return Final        
def MergeSort(array):
    if len(array)<=1:
        return array
    
    left=MergeSort(array[:len(array)/2])
    right=MergeSort(array[len(array)/2:])

    return Merge(left, right)

#Numero de datos que tendran los arreglos de prueba
Prueba=800
#Cantidad de pruebas que se haran
n=[80]
#Se guardan en tablas los 4 metodos
tablas={'Burbuja':[], 'QuickSort':[], 'ShellSort':[], 'MergeSort':[]}

#Se inicializa el total de tiempo que les toma para completar las 80 pruebas en 0s
BurbujaTot=0
QuickTot=0
ShellTot=0
MergeTot=0

#Ciclo que realizara las 80 pruebas
for Test in range(n[0]):
   #Se crea el arreglo llamado "B"
   #Se muestra el arreglo en desorden
   B=Crear(Prueba, Prueba)
   #Se guarda en cuatro distintos arreglos el arreglo original, para asi todos los metodos ordenen el mismo arreglo
   BBurb=B
   BQuick=B
   BShell=B
   BMerge=B
   print(B)
   #Se toma el tiempo previo a la ejecucion del metodo y se guarda en t0
   #Se ejecuta el metodo
   #Se toma el tiempo justo despues de terminada la ejecucion y se guarda en t1
   #Se guarda en la tabla correspondiente el resultado de restar el tiempo posterior menos el tiempo previo a la ejecucion para obtener cuanto tiempo se tardo en ordenar el arreglo
   t0=time()
   Burbuja(BBurb, 0)
   t1=time()
   tablas['Burbuja'].append(t1-t0)

   #Se toma el tiempo previo a la ejecucion del metodo y se guarda en t0
   #Se ejecuta el metodo
   #Se toma el tiempo justo despues de terminada la ejecucion y se guarda en t1
   #Se guarda en la tabla correspondiente el resultado de restar el tiempo posterior menos el tiempo previo a la ejecucion para obtener cuanto tiempo se tardo en ordenar el arreglo
   t0=time()
   QuickSort(BQuick, 0, len(B)-1)
   t1=time()
   tablas['QuickSort'].append(t1-t0)

   #Se toma el tiempo previo a la ejecucion del metodo y se guarda en t0
   #Se ejecuta el metodo
   #Se toma el tiempo justo despues de terminada la ejecucion y se guarda en t1
   #Se guarda en la tabla correspondiente el resultado de restar el tiempo posterior menos el tiempo previo a la ejecucion para obtener cuanto tiempo se tardo en ordenar el arreglo
   t0=time()
   ShellSort(BShell, len(B)/2)
   t1=time()
   tablas['ShellSort'].append(t1-t0)

   #Se toma el tiempo previo a la ejecucion del metodo y se guarda en t0
   #Se ejecuta el metodo
   #Se toma el tiempo justo despues de terminada la ejecucion y se guarda en t1
   #Se guarda en la tabla correspondiente el resultado de restar el tiempo posterior menos el tiempo previo a la ejecucion para obtener cuanto tiempo se tardo en ordenar el arreglo   
   t0=time()
   MergeSort(BMerge)
   t1=time()
   tablas['MergeSort'].append(t1-t0)
   

#Se recorreran las tablas completas y se iran sumando los tiempos en las variables de tiempo total de cada metodo
for i in range(n[0]):
    BurbujaTot+=tablas['Burbuja'][i]
    QuickTot+=tablas['QuickSort'][i]
    ShellTot+=tablas['ShellSort'][i]
    MergeTot+=tablas['MergeSort'][i]

#Se crea una tabla donde se mostraran las sumas de los tiempos que se realizo en ordenar 800 datos 80 veces con los cuatro metodos de ordenamiento
print "Pruebas\tBurbuja\tQuickSort\tShellSort\tMergeSort"
print 60*"_"
for i,Test in enumerate(n):
    print "%d\t%0.5f\t%0.5f\t\t%0.5f  \t%0.5f"%(
            Test, BurbujaTot, QuickTot, ShellTot, MergeTot)
            #Test, tablas['Burbuja'][i], tablas['QuickSort'][i],
            #tablas['ShellSort'][i], tablas['MergeSort'][i])
