#Tarea 5. Problema 2 - ITCR.Física Computacional I
#Johnny Borbón Valverde (2018093752)
#Daniel Espinoza Castro (2018209624)

import numpy as np
import matplotlib.pyplot as plt

#Funcion para crear espines aleatorios
def EspinesAleatorios(nEspines):
    # Arreglo para almacenar los espines
    arregloEspines = np.random.randint(-1,1, size=nEspines)
    for i in range (nEspines):
        if arregloEspines[i]==0:
            if np.random.random()>0.5:
                arregloEspines[i]=1
            else: 
                arregloEspines[i]= -1
    return arregloEspines

                
#Funcion para calcular la Energia de Ising del sistema               
def Energia_Ising(arregloEspines, valorJ):
    energia = 0
    for i in range(len(arregloEspines)-1):
        energia += arregloEspines[i]*arregloEspines[i+1]
    return -valorJ*energia

#Funcion para calcular la magnetizacion
def Magnetizacion(arregloEspines):
    mag= 0
    for i in range(len(arregloEspines)):
        mag += arregloEspines[i]
    return mag

'''
Parte A y B
'''

# Parámetros de la simulación
kBoltz_temperatura = 1
nEspines = 100
nPasos = 4000
valorJ = 1
valorE = 0

arregloEspines= EspinesAleatorios(nEspines)
        
##################################################################
#PARA PRUEBAS
#Arreglo hacia espines arriba
#arregloEspines = np.ones([nEspines], np.int)

#Arreglo hacia espines abajo
#arregloEspines = np.ones([nEspines], np.int)*-1

##################################################################

#se definen las listas vacías
listaGrafico=[]
listaGrafico.append(np.array(arregloEspines))

#Lista que guardará los valores de magnetizacion para cada configuracion aprobada del sistema 
lista_Magnetizacion = []
lista_Magnetizacion.append(Magnetizacion(arregloEspines))

#Lista que guardará los valores de Energía para cada configuracion aprobada del sistema 
lista_Energia = []

#Variable que calculará la suma de todos los valores de energía de la lista anterior
suma_Energia = 0

suma_energia_acumulada=0
suma_magnetizacion_acumulada=0

for k in range(nPasos):
        
        #Se calcula la energía de Ising antes de que se realice un cambio de dirección de espín
        energia_I = Energia_Ising(arregloEspines, valorJ)
        
        # Se escoge la partícula a "mover"
        iPart = np.random.randint(nEspines)
        # Se da el cambio de orientación de espín
        if arregloEspines[iPart] == 1:
            arregloEspines[iPart] = -1
        else:
            arregloEspines[iPart] = 1
        
        #Energia de Ising despues del cambio sugerido
        energia_J = Energia_Ising(arregloEspines, valorJ)
    
        deltaE= energia_J - energia_I
        
        #Se calcula la probabilidad de aceptacion del cambio de orientacion
        P =np.exp(-deltaE/kBoltz_temperatura)
        
        #Se evalua si el cambio es aceptado en base a la probabilidad de aceptacion
        if deltaE > 0:
            if np.random.random()<P:
                pass
            else:
                arregloEspines[iPart] *= -1
        else:
            pass
        
        #Condición para que se guarden los valores de energía y magnetizacion cuando alcancen el equilirio (2000 pasos)
        if k >= 2000:
            #Se guarda en la lista el valor aceptado de la energía del estado cambiado
            lista_Energia.append(Energia_Ising(arregloEspines, valorJ))
            
            #Se guarda en la lista el valor aceptado de la magnetizacion del estado cambiado
            lista_Magnetizacion.append(Magnetizacion(arregloEspines))
                
                
        #Se guarda en la lista el valor nuevo del espín cambiado
        listaGrafico.append(np.array(arregloEspines))

        
arregloGraf=np.asarray(listaGrafico)

# Gráfico
fig, ax = plt.subplots(figsize = [10,10] , dpi=120)
ax.imshow(arregloGraf.T, "plasma")
ax.set_title('Simulación del Modelo Ising 1D')
ax.set_xlabel('pasos')
ax.set_ylabel('Espines')
ax.set_aspect("5")
plt.show()

'''
Parte C

'''
#Variable que calculará la suma de todos los valores de energía de la lista anterior
suma_Energia = 0

suma_energia_acumulada=0
suma_magnetizacion_acumulada=0
suma_Us=0

reps = 10

for w in range(0, reps):
    #Energia interna del sistema "U"
    U=0
    arregloEspines= EspinesAleatorios(nEspines)
    
    ##################################################################
    #PARA PRUEBAS =
    #Arreglo hacia espines arriba
    #arregloEspines = np.ones([nEspines], np.int)
    
    #Arreglo hacia espines abajo
    #arregloEspines = np.ones([nEspines], np.int)*-1

    ##################################################################

    suma_Energia = 0
    energias_eq = 0
    magnetizaciones_eq = 0
    
    lista_Energia= []
    lista_Magnetizacion = []
    lista_Energia_U = []
    
    for k in range(nPasos):
        
        #Se calcula la energía de Ising antes de que se realice un cambio de dirección de espín
        energia_I = Energia_Ising(arregloEspines, valorJ)
        
        # Se escoge la partícula a "mover"
        iPart = np.random.randint(nEspines)
        # Se da el cambio de orientación de espín
        if arregloEspines[iPart] == 1:
            arregloEspines[iPart] = -1
        else:
            arregloEspines[iPart] = 1
        
        #Energia de Ising despues del cambio sugerido
        energia_J = Energia_Ising(arregloEspines, valorJ)
    
        deltaE= energia_J - energia_I
        
        #Se calcula la probabilidad de aceptacion del cambio de orientacion
        P =np.exp(-deltaE/kBoltz_temperatura)
        
        #Se evalua si el cambio es aceptado en base a la probabilidad de aceptacion
        if deltaE > 0:
            if np.random.random()<P:
                pass
            else:
                arregloEspines[iPart] *= -1
        else:
            pass
        
        #Lista para guardar todos los valores de energía, no sólo en el equilibrio
        lista_Energia_U.append(Energia_Ising(arregloEspines, valorJ))
        
        #Condición para que se guarden los valores de energía y magnetizacion cuando alcancen el equilirio (2000 pasos)
        if k >= 2000:
            #Se guarda en la lista el valor aceptado de la energía del estado cambiado
            lista_Energia.append(Energia_Ising(arregloEspines, valorJ))
            energias_eq += lista_Energia[-1]
 
            
            #Se guarda en la lista el valor aceptado de la magnetizacion del estado cambiado
            lista_Magnetizacion.append(Magnetizacion(arregloEspines))
            magnetizaciones_eq += lista_Magnetizacion[-1]
    
                
        #Se guarda en la lista el valor nuevo del espín cambiado
        listaGrafico.append(np.array(arregloEspines))
        
        
    suma_energia_acumulada += energias_eq/len(lista_Energia)
    suma_magnetizacion_acumulada += magnetizaciones_eq/len(lista_Magnetizacion)
    
    #Se calcula la energía interna de cada sistema
    for i in lista_Energia_U:
        suma_Energia += i
        U = suma_Energia/len(lista_Energia_U)
        
    suma_Us += U
    
#Promedio de energías y magnetizacion
prom_Ener=suma_energia_acumulada/reps
prom_Mag=suma_magnetizacion_acumulada/reps
prom_Us= suma_Us/reps

print("Promedio de Energía después de ", reps, "repeticiones:", prom_Ener)
print("Promedio de Magnetización después de ", reps, "repeticiones:", prom_Mag)
print("Promedio de Energía Interna después de ", reps, "repeticiones:", prom_Us)


'''
Parte E y F

'''

kBoltzman_temperatura=0.001
grafico_KBT = []
grafico_U = []
grafico_magnet = []
grafico_C = []
energiaCuad = 0

while kBoltzman_temperatura <= 5:
    nEspines = 100
    nPasos = 4000
    valorJ = 1
    valorE = 0
    
    arregloEspines= EspinesAleatorios(nEspines)

    
    #Ciclo principal
    #Lista de espines a graficar en 1D
    listaGrafico = []
    listaGrafico.append(np.array(arregloEspines))
    
    #Lista que guardará los valores de magnetizacion para cada configuracion aprobada del sistema 
    lista_Magnetizacion = []
    lista_Magnetizacion.append(Magnetizacion(arregloEspines))
    
    #Lista que guardará los valores de Energía para cada configuracion aprobada del sistema
    lista_Energia_U = []
    
    #Lista que guardará los valores de Energía en el equilibrio
    lista_Energia = []
    
    #Variable que calculará la suma de todos los valores de energía de la lista anterior
    suma_Energia = 0
    
    suma_energia_acumulada=0
    suma_magnetizacion_acumulada=0
    suma_Us=0
    
    reps = 10
    
    U=0
    
    arregloEspines= EspinesAleatorios(nEspines)
    
    ##################################################################
    #PARA PRUEBAS
    #Arreglo hacia espines arriba
    #arregloEspines = np.ones([nEspines], np.int)
    
    #Arreglo hacia espines abajo
    #arregloEspines = np.ones([nEspines], np.int)*-1

    ##################################################################

    suma_Energia = 0
        
      
    for k in range(nPasos):
        
        #Se calcula la energía de Ising antes de que se realice un cambio de dirección de espín
        energia_I = Energia_Ising(arregloEspines, valorJ)
        
        # Se escoge la partícula a "mover"
        iPart = np.random.randint(nEspines)
        # Se da el cambio de orientación de espín
        if arregloEspines[iPart] == 1:
            arregloEspines[iPart] = -1
        else:
            arregloEspines[iPart] = 1
        
        #Energia de Ising despues del cambio sugerido
        energia_J = Energia_Ising(arregloEspines, valorJ)
    
        deltaE= energia_J - energia_I
        
        #Se calcula la probabilidad de aceptacion del cambio de orientacion
        P =np.exp(-deltaE/kBoltzman_temperatura)
        
        #Se evalua si el cambio es aceptado en base a la probabilidad de aceptacion
        if deltaE > 0:
            if np.random.random()<P:
                pass
            else:
                arregloEspines[iPart] *= -1
        else:
            pass
        
        #Lista para guardar todos los valores de energía, no sólo en el equilibrio
        lista_Energia_U.append(Energia_Ising(arregloEspines, valorJ))
        
        #Condición para que se guarden los valores de energía y magnetizacion cuando alcancen el equilirio (2000 pasos)
        if k >= 2000:
            #Se guarda en la lista el valor aceptado de la energía del estado cambiado
            lista_Energia.append(Energia_Ising(arregloEspines, valorJ))
            
            #Se guarda en la lista el valor aceptado de la magnetizacion del estado cambiado
            lista_Magnetizacion.append(Magnetizacion(arregloEspines))
        
        #Se guarda en la lista el valor nuevo del espín cambiado
        listaGrafico.append(np.array(arregloEspines))
        
    
    #Se calcula la energía interna de cada sistema
    for i in lista_Energia_U:
        suma_Energia += i
        U = suma_Energia/len(lista_Energia_U)


    #Fin del ciclo
    #arregloGraf=np.asarray(listaGrafico)
    grafico_magnet.append(lista_Magnetizacion[-1])
    grafico_U.append(U)
    grafico_KBT.append(kBoltzman_temperatura)
        
    kBoltzman_temperatura += 0.1


#Gráfico kbt vs U

fig, ax = plt.subplots(figsize = [10, 10], dpi=120)
ax.plot(grafico_KBT,grafico_U)
ax.set_title('Gráfico de Kbt vs U')
ax.set_xlabel('Kbt')
ax.set_ylabel('U')
plt.show()

#Gráfico Kbt vs Magnetización 
fig, ax = plt.subplots(figsize = [10, 10], dpi=120)
ax.plot(grafico_KBT, grafico_magnet)
ax.set_title('Gráfico de Kbt vs Magnetización')
ax.set_xlabel('Kbt')
ax.set_ylabel('Magnetización')
plt.show()

'''
Parte G

'''

kBoltzman_temperatura=0.001
grafico_KBT = []
grafico_U = []

grafico_C = []


while kBoltzman_temperatura <= 5:
    nEspines = 100
    nPasos = 4000
    valorJ = 1
    valorE = 0


    suma_Us=0
    
    suma_U_2_reps = 0
    
    reps = 10
    
    for w in range(0, reps):
        #Energia interna del sistema "U"
        U=0
        arregloEspines= EspinesAleatorios(nEspines)
        
        ##################################################################
        #PARA PRUEBAS
        #Arreglo hacia espines arriba
        #arregloEspines = np.ones([nEspines], np.int)
        
        #Arreglo hacia espines abajo
        #arregloEspines = np.ones([nEspines], np.int)*-1
    
        ##################################################################
        
        #Ciclo principal
        #Lista de espines a graficar en 1D
        listaGrafico = []
        listaGrafico.append(np.array(arregloEspines))
        
        
        #Lista que guardará los valores de Energía para cada configuracion aprobada del sistema 
        lista_Energia = []
        lista_EnergiaU2 = []
        
        suma_Energia = 0
        
        
        
        for k in range(nPasos):
            
            #Se calcula la energía de Ising antes de que se realice un cambio de dirección de espín
            energia_I = Energia_Ising(arregloEspines, valorJ)
            
            # Se escoge la partícula a "mover"
            iPart = np.random.randint(nEspines)
            # Se da el cambio de orientación de espín
            if arregloEspines[iPart] == 1:
                arregloEspines[iPart] = -1
            else:
                arregloEspines[iPart] = 1
            
            #Energia de Ising despues del cambio sugerido
            energia_J = Energia_Ising(arregloEspines, valorJ)
        
            deltaE= energia_J - energia_I
            
            #Se calcula la probabilidad de aceptacion del cambio de orientacion
            P =np.exp(-deltaE/kBoltzman_temperatura)
            
            #Se evalua si el cambio es aceptado en base a la probabilidad de aceptacion
            if deltaE > 0:
                if np.random.random()<P:
                    pass
                else:
                    arregloEspines[iPart] *= -1
            else:
                pass
            
            if k >= 2000:
                #Se guarda en la lista el valor aceptado de la energía del estado cambiado
                lista_Energia.append(Energia_Ising(arregloEspines, valorJ))
                
                lista_EnergiaU2.append(Energia_Ising(arregloEspines, valorJ))
            

                
            #Se guarda en la lista el valor nuevo del espín cambiado
            listaGrafico.append(np.array(arregloEspines))
        
        suma_Energia = 0
        sum_energiasCuad = 0
            
    
        #Se calcula la energía interna de cada sistema
        for i in lista_Energia:
            suma_Energia += i
        U = suma_Energia/len(lista_Energia)
            
            
        for y in lista_EnergiaU2:
            sum_energiasCuad += y**2
            
        sum_energiasCuad_prom = sum_energiasCuad/len(lista_EnergiaU2)
        
        suma_Us += U
        suma_U_2_reps += sum_energiasCuad_prom
        
    #Promedio Energía Interna U
    prom_U = suma_Us/reps
    
    #Fluctuaciones de Energía U_2
    U_2 = (1/reps)*suma_U_2_reps
    
    
    #Calor Específico
    #El primer calor específico debería ser 0 
    if kBoltzman_temperatura == 0.001:
        C = 0
    else:
        C= (1/nEspines**2)*(U_2-prom_U**2)/(kBoltzman_temperatura**2)
        
        
    #Fin del ciclo
    #arregloGraf=np.asarray(listaGrafico)
    grafico_U.append(U)
    grafico_KBT.append(kBoltzman_temperatura)
    grafico_C.append(C)
        
    kBoltzman_temperatura += 0.1


#Gráfico de Kbt vs C
fig, ax = plt.subplots(dpi=120)
ax.plot(grafico_KBT, grafico_C)
ax.set_title('Gráfico de Kbt vs Calor específico del sistema')
ax.set_xlabel('Kbt')
ax.set_ylabel('Calor especifico')
plt.show()



