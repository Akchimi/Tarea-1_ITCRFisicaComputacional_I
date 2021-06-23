#Tarea 6. AGM - ITCR.Física Computacional I
#Johnny Borbón Valverde (2018093752)
#Daniel Espinoza Castro (2018209624)

import numpy as np
import matplotlib.pyplot as plt

listaCoordenadas=[[0.2554, 18.2366],
[0.4339, 15.2476],
[0.7377, 8.3137],
[1.1354, 16.5638],
[1.5820, 17.3030],
[2.0913, 9.2924],
[2.2631, 5.3392],
[2.6373, 2.6425],
[3.0040, 19.5712],
[3.6684, 14.8018],
[3.8630, 13.7008],
[4.2065, 9.8224],
[4.8353, 2.0944],
[4.9785, 3.1596],
[5.3754, 17.6381],
[5.9425, 6.0360],
[6.1451, 3.8132],
[6.7782, 11.0125],
[6.9223, 7.7819],
[7.5691, 0.9378],
[7.8190, 13.1697],
[8.3332, 5.9161],
[8.5872, 7.8303],
[9.1224, 14.5889], 
[9.4076, 9.7166],
[9.7208, 8.1154],
[10.1662, 19.1705],
[10.7387, 2.0090],
[10.9354, 5.1813],
[11.3707, 7.2406],
[11.7418, 13.6874],
[12.0526, 4.7186],
[12.6385, 12.1000],
[13.0950, 13.6956],
[13.3533, 17.3524],
[13.8794, 3.9479],
[14.2674, 15.8651],
[14.5520, 17.2489],
[14.9737, 13.2245],
[15.2841, 1.4455],
[15.5761, 12.1270],
[16.1313, 14.2029],
[16.4388, 16.0084], 
[16.7821, 9.4334],
[17.3928, 12.9692],
[17.5139, 6.4828],
[17.9487, 7.5563],
[18.3958, 3.5112],
[18.9696, 19.3565], 
[19.0928, 16.5453]]


nGenes=len(listaCoordenadas)
#nGenes=50
tamañoPoblacion=100

#Calculo de la ciudad próxima en un cromosoma a partir de un valor anterior, 
#a diferencia de la función Decodificar, esta solo calcula la distancia Euclidiana para 2 puntos
def CalculoDistEuclid(xi,yi,cola):
    distmin_actual= 100000
    posicion_min = 50
    
    for l in cola:
        xs=l[0]
        ys=l[1]
        
        deltaX=xs-xi
        deltaY=ys-yi
        
        distanciaEuclid=np.sqrt(deltaX**2+deltaY**2)
        
        
        if distanciaEuclid < distmin_actual:
            distmin_actual = distanciaEuclid
            posicion_min = cola.index(l)
    
    return posicion_min



#Se inicializa la población con las modificaciones especificadas en el enunciado
def InicializaciónModificada(tamañoPoblación, nGenes):
    poblacion = []
    
    #Para generar 'tamañoPoblación' de cromosomas
    for i in range(tamañoPoblación):
        lista_Ciudades=[]
        punto_inicio=np.random.randint(0,nGenes)
        
        lista_Ciudades_Coordenadas=[]
        lista_Ciudades_Coordenadas.append(listaCoordenadas[punto_inicio])
        cola_Coordenadas= listaCoordenadas.copy()
        cola_Coordenadas.pop(punto_inicio)
        
        #Para la creación de 1 cromosoma
        while len(cola_Coordenadas) > 0:
            
            xi=lista_Ciudades_Coordenadas[-1][0]
            yi=lista_Ciudades_Coordenadas[-1][1]
            
            #Calculo de ciudad más cercana
            nSig = CalculoDistEuclid(xi,yi,cola_Coordenadas)
                    
            #Se agrega el valor de coordenadas encontrado y 
            #se borra la coordenada ya utilizada de la cola para que no se repita
            lista_Ciudades_Coordenadas.append(cola_Coordenadas[nSig])
            cola_Coordenadas.pop(nSig)
            
        #Conversión de coordenadas a número de ciudad
        for j in lista_Ciudades_Coordenadas:
            ciudad= listaCoordenadas.index(j)
            lista_Ciudades.append(ciudad)
        poblacion.append(lista_Ciudades)
    
    #Se realizan de 3 a 10 mutaciones a la poblacion individual, menos el primer individuo
    for s in range(1,len(poblacion)):
    
        cromosoma = poblacion[s]
        
        cant_mutaciones = np.random.randint(3,11)
        
        for g in range(0,cant_mutaciones):
            
            cromosomaMutado=OperadorMutación(cromosoma, p_mut, nGenes)
    
        poblacion[s] = cromosomaMutado
        

    
    return poblacion  

#Se decodifica el cromosoma y se obtiene la distancia euclideana para todo el recorrido de todas las ciudades
def Decodificar(cromosoma):
    distanciaEuclid=0
    listaX=[]
    listaY=[]
    for i in range(len(cromosoma)):
        num=int(cromosoma[i])
        coord_x=listaCoordenadas[num][0]
        coord_y=listaCoordenadas[num][1]
        listaX.append(coord_x)
        listaY.append(coord_y)
        
    #calculo para que la ruta sea cerrada, distancia de la ultima ciudad a la primera
    deltaX_i=listaX[nGenes-1]-listaX[0]
    deltaY_i=listaY[nGenes-1]-listaY[0]
    distancia_i=np.sqrt(deltaX_i**2+deltaY_i**2)
    
    for j in range(0,nGenes-1):
        deltaX=listaX[j]-listaX[j+1]
        deltaY=listaY[j]-listaY[j+1]
        distanciaEuclid+=np.sqrt(deltaX**2+deltaY**2)

    
    distanciaEuclid+=distancia_i
    return distanciaEuclid
        
#Funcion que evalua el individuo y calcula el valor de ajuste   
def EvaluarIndividuo(distanciaEuclidiana):
    Fajuste=1/distanciaEuclidiana
    return Fajuste
    

#Operador mutacion que intercambia la posicion de 2 genes del cromosoma 
def OperadorMutación(cromosoma, p_mut, nGenes):
    cromosomaMutado = np.copy(cromosoma)
    
    nAleatorio=np.random.random()
    
    Pos1=np.random.randint(0,nGenes)
    Pos2=np.random.randint(0,nGenes)
    
    if nAleatorio<p_mut:
        cromosomaMutado[Pos1] = cromosoma[Pos2]
        cromosomaMutado[Pos2] = cromosoma[Pos1]
        
    return cromosomaMutado
    
##Encuentra todos los valores de ajuste para una generación dada
def ValoresF_Poblacion(poblacion):
    lista_Fajuste=[]
    for i in range(len(poblacion)):
        cromosoma=poblacion[i]
        distanciaEuclidiana= Decodificar(cromosoma)
        F_ajuste=EvaluarIndividuo(distanciaEuclidiana)
        lista_Fajuste.append(F_ajuste)
        
    lista_FajusteTotal.append(lista_Fajuste)
    return  


#Encuentra el mejor camino para todas las generaciones
def encontrarCamino(lista_FajusteTotal,lista_PoblacionesTotales):
    Fmaximo=0
    for i in range(nGeneraciones):
        for j in range (tamañoPoblacion):
            Factual=lista_FajusteTotal[i][j]
            if Factual>Fmaximo:
                Fmaximo=Factual
                Imax=i
                Jmax=j
            else:
                pass
            
    #print('El F maximo es: ',Fmaximo) #Print para ver cual es el F maximo de la lista de todos los F ajuste
    
    mejor_camino=lista_PoblacionesTotales[Imax][Jmax]
    
    #Estas 3 lineas de codigo siguientes eran para verificar que mi mejor camino diera correctamente el F maximo anterior
    #distancia=Decodificar(mejor_camino)
    #Fajuste=EvaluarIndividuo(distancia)
    #print('Mi F maximo es: ',Fajuste) 

    return mejor_camino

#Gráfica de los valores de ajuste
def GráficasEvolución(lista_FajusteTotal):
    #Procesamiento de los valores de ajuste obtenidos
    arregloValoresAjuste = np.asarray(lista_FajusteTotal)
    promedioAjuste = np.mean(arregloValoresAjuste,1)
    valoresMaximosAjuste = np.max(arregloValoresAjuste,1)
    
    #Graficos de la evolucion de los valores de ajuste
    fig,ax = plt.subplots(dpi=120)
    ax.plot(promedioAjuste, label ='ajuste promedio')
    ax.plot(valoresMaximosAjuste, label = 'ajuste máximo')
    
    ax.set_title('Evolución de los valores de ajuste de la población')
    ax.set_xlabel('generaciones')
    ax.set_ylabel('valores de ajuste')
    ax.legend(loc='best')
    plt.show()


#Se inicializan listas para guardar todas las generaciones, todos sus valores de ajuste
    
lista_FajusteTotal=[]
lista_PoblacionesTotales=[]
#lista_Fajuste=[]


nGeneraciones=300
p_mut=0.47

#Se genera la poblacion inicial
poblacion = InicializaciónModificada(tamañoPoblacion, nGenes)

#Se general los F de ajuste para la oblación inicial y se guarda la población inicial
ValoresF_Poblacion(poblacion)
lista_PoblacionesTotales.append(poblacion)



#Se empiezan a generar mutaciones en la población, cada vez que toda una población fue mutada (generación) 
#se guarda en una lista, y se muta la ultima generación, así sucesivamente hasta que se alcanzan las generaciones deseadas 
for i in range(nGeneraciones):
    poblacionMutada=[]
    poblacion=lista_PoblacionesTotales[i]
    for j in range(len(poblacion)):
        cromosoma=poblacion[j]
        cromosomaMutado=OperadorMutación(cromosoma, p_mut, nGenes)
        poblacion[j]=cromosomaMutado
        poblacionMutada.append(cromosomaMutado)
    lista_PoblacionesTotales.append(poblacionMutada)    
    ValoresF_Poblacion(poblacion)
    
  
    
#Ya finalizadas las mutaciones y teniendo todos los valores de F para todas las generaciones y
#todos los cromosomas para todas las generaciones podemos encontrar el mejor camino
mejor_camino=encontrarCamino(lista_FajusteTotal,lista_PoblacionesTotales)
longitud_mejor_camino=Decodificar(mejor_camino)
print("La longitud del mejor camino es: ",longitud_mejor_camino)

#Graficamos los valores de ajuste
GráficasEvolución(lista_FajusteTotal)


   
#Graficar la ruta del mejor cromosoma
CoordsMejorCamino=[]
CoordsMejorCaminoX=[]
CoordsMejorCaminoY=[]
for i in mejor_camino:
    CoordsMejorCamino.append(listaCoordenadas[int(i)])
for j in range(len(CoordsMejorCamino)):
    CoordsMejorCaminoX.append(CoordsMejorCamino[j][0])
    CoordsMejorCaminoY.append(CoordsMejorCamino[j][1])
    
#Para que en la gráfica el camino sea cerrado agreagamos al final la posición inicial
CoordsMejorCamino.append(CoordsMejorCamino[0])
CoordsMejorCaminoX.append(CoordsMejorCaminoX[0])
CoordsMejorCaminoY.append(CoordsMejorCaminoY[0])

 
fig,ax=plt.subplots(dpi=120)
ax.plot(CoordsMejorCaminoX,CoordsMejorCaminoY, "c-")
ax.plot(CoordsMejorCaminoX,CoordsMejorCaminoY, "ro")
ax.set_title('Mejor ruta')
ax.set_xlabel('Coordenada x')
ax.set_ylabel('Coordenada y')
ax.legend(["Ruta","Ubicación"])
plt.show()    

#Guardar las coordenadas del mejor cromosoma
np.savetxt('caminoMásCorto_AGM.txt',CoordsMejorCamino)
#Esto da una lista de 51 valores en lugar de 50 debido a que en las lineas de la 298 a 300
#Se pone el punto inicial al final del array para que el camino sea cerrado