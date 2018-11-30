array=[5,1,12,24,2,8,3,9]
aBurb=array
aQuick=array
aShell=array
aMerge=array

from random import randint
from time import time

def Crear(size=150, max=150):
    return [randint(0, max) for i in range(size)]

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
    
#print(Burbuja(aBurb, 0))

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
#print QuickSort(array, 0, len(array)-1)           
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

#print(ShellSort(aShell, len(array)/2))
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

#print(MergeSort(aMerge))
Prueba=800
n=[80]
tablas={'Burbuja':[], 'QuickSort':[], 'ShellSort':[], 'MergeSort':[]}

BurbujaTot=0
QuickTot=0
ShellTot=0
MergeTot=0

for Test in range(n[0]):
   B=Crear(Prueba, Prueba)
   print(B)
   t0=time()
   Burbuja(B, 0)
   t1=time()
   tablas['Burbuja'].append(t1-t0)
   
   t0=time()
   QuickSort(B, 0, len(B)-1)
   t1=time()
   tablas['QuickSort'].append(t1-t0)
   
   t0=time()
   ShellSort(B, len(B)/2)
   t1=time()
   tablas['ShellSort'].append(t1-t0)
   
   t0=time()
   MergeSort(B)
   t1=time()
   tablas['MergeSort'].append(t1-t0)
   
for i in range(n[0]):
    BurbujaTot+=tablas['Burbuja'][i]
    QuickTot+=tablas['QuickSort'][i]
    ShellTot+=tablas['ShellSort'][i]
    MergeTot+=tablas['MergeSort'][i]
    #BurbujaTot/=n[0]
    #QuickTot/=n[0]
    #ShellTot/=n[0]
    #MergeTot/=n[0]
       
print "Pruebas\tBurbuja\tQuickSort\tShellSort\tMergeSort"
print 60*"_"
for i,Test in enumerate(n):
    print "%d\t%0.5f\t%0.5f\t\t%0.5f  \t%0.5f"%(
            Test, BurbujaTot, QuickTot, ShellTot, MergeTot)
            #Test, tablas['Burbuja'][i], tablas['QuickSort'][i],
            #tablas['ShellSort'][i], tablas['MergeSort'][i])
