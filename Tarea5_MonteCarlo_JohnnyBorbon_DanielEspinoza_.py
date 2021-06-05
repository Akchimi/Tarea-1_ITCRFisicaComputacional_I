#Tarea 5. Problema 1 - ITCR.Física Computacional I
#Johnny Borbón Valverde (2018093752)
#Daniel Espinoza Castro (2018209624)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#Parte A

def CaminoAleatorio(lista_Pos, nIter):
    
    paso_l=5*(10**(-5))
    
    xPos = (np.random.random()-0.5)*2
    yPos = (np.random.random()-0.5)*2
    zPos = (np.random.random()-0.5)*2
    
    L=np.sqrt((xPos)**2+(yPos)**2+(zPos)**2) 
    
    deltaX= (1/L)*xPos*paso_l
    deltaY= (1/L)*yPos*paso_l
    deltaZ= (1/L)*zPos*paso_l
    
    nuevaxPos = (lista_Pos[0][nIter-1] + deltaX)
    nuevayPos = (lista_Pos[1][nIter-1] + deltaY)
    nuevazPos = (lista_Pos[2][nIter-1] + deltaZ)

    lista_Pos[0].append(nuevaxPos)
    lista_Pos[1].append(nuevayPos)
    lista_Pos[2].append(nuevazPos)
    

    return lista_Pos,paso_l
    
#Parte B Calculo teorico de la cantidad de pasos N de acuerdo a lo mencionado en el trabajo escrito.
R=0.2
l=5*(10**(-5))
Nteorico= (R/l)**2
    
#Parte C y D Estimación de la cantidad promedio de pasos N y el tiempo promedio que le toma al fotón recorrer la trayectoria
c=299792458 #Velocidad de la luz
ValorArbitrario=10
#Se inicializan los valores de N y t
nTotal=0
tTotal=0

for i in range(0,ValorArbitrario+1):
    lista_posiciones= [[0.],[0.],[0.]] #Se inicializa la lista de posiciones en el origen
    Ltotal=0 #Se inicializa la distancia total recorrida por el fotón
    nPasos=1
    continuar=True
    while continuar==True:
        lista_posiciones,L= CaminoAleatorio(lista_posiciones, nPasos)
        Ltotal+=L #Se suma la distancia recorrida por el foton en este paso
        #En el siguiente ciclo se revisa si cada coordenada para este paso es menor al valor de R para decidir si dar el siguiente paso o no
        if  np.abs(lista_posiciones[0][nPasos])<R and np.abs(lista_posiciones[1][nPasos])<R and np.abs(lista_posiciones[2][nPasos])<R:
            continuar=True
            nPasos+=1 #Para esta condición del if se suma 1 paso al contador de pasos pues el fotón aun no escapa la distancia R
        else:
            continuar=False #Si el fotón alcanza la distancia R en alguna coordenada se detiene el ciclo que genera los pasos aleatorios
    nTotal+=nPasos #Se suman los pasos del camino aleatorio al total de pasos realizados para la cantidad de iteraciones deseadas
    tTotal+=Ltotal/c #Se calcula y se suma el tiempo que dura en realizarse todos los pasos de esta iteración

nPromedio=nTotal/ValorArbitrario #Promedio de pasos que toma cada iteración
tpromedio=(tTotal/ValorArbitrario)*(1/60)*(1/60)*(1/24)*(1/365.25) #Promedio de tiempo que dura en recorrer la distancia R

#Se imprimen los resultados
print("El N teorico es: ", Nteorico)    
print("El promedio de pasos será", nPromedio, "con ",ValorArbitrario, " Corridas")
print("El foton va a durar: ",tpromedio," años en escapar la región R")

#Parte E Gráfica
ax = plt.axes(projection="3d")  
ax.plot(lista_posiciones[0], lista_posiciones[1],lista_posiciones[2], c='m', lw=0.5)
ax.set_title('Caminos aleatorio de un fotón')
plt.show()

