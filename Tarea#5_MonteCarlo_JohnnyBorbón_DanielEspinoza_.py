#Tarea 5. Problema 1 - ITCR.Física Computacional I
#Johnny Borbón Valverde (2018093752)
#Daniel Espinoza Castro (2018209624)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#Parte A

def CaminoAleatorio(lista_Pos, nIter):
    """
    Genera un par ordenado aleatorio respecto al punto aanterior
    """
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
    
#Parte B  
R=0.05 #cambiar
l=5*(10**(-5))
Nteorico= R/l #Elevado al cuadrado?
    
c=299792458
#Parte C
ValorArbitrario=10
nTotal=0
tTotal=0

for i in range(0,ValorArbitrario+1):
    lista_posiciones= [[0.],[0.],[0.]]
    Ltotal=0
    nPasos=1
    continuar=True
    while continuar==True:
        lista_posiciones,L= CaminoAleatorio(lista_posiciones, nPasos)
        Ltotal+=L
        if  np.abs(lista_posiciones[0][nPasos])<R and np.abs(lista_posiciones[1][nPasos])<R and np.abs(lista_posiciones[2][nPasos])<R:
            continuar=True
            nPasos+=1
        else:
            continuar=False
    nTotal+=nPasos
    tTotal+=Ltotal/c

nPromedio=nTotal/ValorArbitrario #Promedio de pasos que toma cada iteración
tpromedio=(tTotal/ValorArbitrario)*(1/60)*(1/60)*(1/24)*(1/365.25)

print("El N teorico es: ", Nteorico)    
print("El promedio de pasos será", nPromedio, "con ",ValorArbitrario, " Corridas")
print("El foton va a durar: ",tpromedio,"")
print(lista_posiciones)

# Gráfica
ax = plt.axes(projection="3d")
ax.plot(lista_posiciones[0], lista_posiciones[1],lista_posiciones[2], c='m', lw=0.5)
ax.set_title('Caminos aleatorio de un fotón')
plt.show()

"""
continuar=True
while continuar==True:
    lista_posiciones= CaminoAleatorio(lista_Pos, nPasos)
    if  lista_posiciones[0][nPasos-1]<R or lista_posiciones[1][nPasos-1]<R or lista_posiciones[2][nPasos-1]<R:
        continuar=True
        nPasos+=1
    else:
        continuar=False

print("El N teorico es: ",Nteorico)      
print("El N practico es: ",nPasos)
"""
