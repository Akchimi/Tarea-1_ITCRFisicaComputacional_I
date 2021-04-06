#Tarea 3- ITCR.Física Computacional I
#Johnny Borbón Valverde (2018093752)
#Daniel Espinoza Castro (2018209624)

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.fft import ifft

#Parámetros
tasaMuestreo = 1024
deltaT = 1

#Tamaño del arreglo de muestras
CantidadPuntos = deltaT*tasaMuestreo

puntos_tiempo = np.linspace(0, deltaT, CantidadPuntos)

#Generación de la señales

frecuencia1 = 75
amplitud1 = 50

frecuencia2 = 125
amplitud2 = 50


señal1 = amplitud1*np.sin(2*np.pi*frecuencia1*puntos_tiempo)
señal2 = amplitud2*np.sin(2*np.pi*frecuencia2*puntos_tiempo)


#Generación del ruido
ruido = np.random.normal(0, 30, CantidadPuntos)

señalOriginal = señal1 + señal2
señalRuidosa = señal1 + señal2 + ruido

#Gráfica de la señal original
fig, ax = plt.subplots(dpi=120)
ax.plot(puntos_tiempo[1:50], señalOriginal[1:50])
ax.set_title('Señal Original')
ax.set_xlabel('Tiempo')
ax.set_ylabel('Amplitud')
plt.show()

#Gráfica de la señal ruidosa
fig, ax = plt.subplots(dpi=120)
ax.plot(puntos_tiempo[1:50], señalRuidosa[1:50])
ax.set_title('Señal Ruidosa')
ax.set_xlabel('Tiempo')
ax.set_ylabel('Amplitud')
plt.show()


# Aplicación de la transformada rápida de fourier

puntos_frecuencia = np.linspace (0.0, 512, int(CantidadPuntos/2))

transformada_señal = fft(señalRuidosa)

amplitudes = (2/CantidadPuntos)*np.abs(transformada_señal[0:np.int(CantidadPuntos/2)])

fig, ax = plt.subplots(dpi=120)
ax.plot(puntos_frecuencia, amplitudes)
ax.set_title('Señal en el dominio de la frecuencia')
ax.set_xlabel('Frecuencia [Hz]')
ax.set_ylabel('Amplitud')
ax.set_xticks(np.arange(0,501,50))
plt.show()


#Función que realiza el filtrado de la señal y su gráfica


def Filtrar_Señal(transformada_señal,amplitudes,umbral):
    for i in range(len(amplitudes)):
        if amplitudes[i]<umbral:
            transformada_señal[i]=0+0j
            amplitudes[i]=0
    
    puntos_frecuencia=np.linspace(0,512,int(CantidadPuntos/2))

    fig, ax = plt.subplots(dpi=120)
    ax.plot(puntos_frecuencia, amplitudes)
    ax.set_title('Señal filtrada en el dominio de la frecuencia')
    ax.set_xlabel('Frecuencia [Hz]')
    ax.set_ylabel('Amplitud')
    ax.set_xticks(np.arange(0,501,50))
    plt.show()
    return transformada_señal


#Transformada rápida de Fourier inversa
umbral=30
transformada_señal=Filtrar_Señal(transformada_señal,amplitudes,umbral)

puntos_frecuencia = np.linspace (0.0, 512, int(CantidadPuntos/2))

transformadaInversa_señal = ifft(transformada_señal)

fig, ax = plt.subplots(dpi=120)
ax.plot(puntos_tiempo[1:50], transformadaInversa_señal[1:50])
ax.set_title('Señal Filtrada')
ax.set_xlabel('Tiempo')
ax.set_ylabel('Amplitud')
plt.show()


