#Tarea 4- Series Fourier- ITCR.Física Computacional I
#Johnny Borbón Valverde (2018093752)
#Daniel Espinoza Castro (2018209624)

import numpy as np
import scipy.integrate as spint
import matplotlib.pyplot as pLt
import time 

#Contador de Tiempo
start_time = time.time()

#Se definen las constates del problema
D=0.5
Lx=10.0
A=2.0
x0=5
l=1.5

#Se definen parámetros para la creación de valores de tiempo y espacio
cantidad_puntos=15
#Se define el índice de la sumatoria con el que se quiere trabajar
n=10

#Se definen los valores de tiempo para trabajar
t=np.linspace(0,Lx,cantidad_puntos)
#Se definen los valores de x para trabajar
x=np.linspace(0,Lx,cantidad_puntos)

def Ecuacion_X(x,n,Lx):
    """
    Se define la parte espacial de la ecuación de difusión X(x) sin el valor del
    coeficiente respectivo, ya que se calculará más adelante
    """
    sep_Espacial=np.sin(n*np.pi*x/Lx)
    return sep_Espacial

def Ecuacion_T(t,n,D,Lx):
    """
    Se define la parte temporal de la ecuación de difusión T(t) sin el valor del
    coeficiente respectivo, ya que se calculará más adelante
    """
    sep_Temporal=np.exp(-D*t*((n*np.pi/Lx)**2))
    return sep_Temporal

def Coeficientes(x,x0,l,n,A,Lx):
    """
    Se define la expresión "ecuacion_En" que será la parte de la integral a realizar y
    se multplica posteriormente por las constantes respectivas para obtener los coeficientes de "En" 
    para cada n respectivo, de la solución por series de Fourier
    """
    ecuacion_En=lambda x: ((np.exp(-(((x-x0)**2)/l)))*np.sin(n*np.pi*x/Lx))
    integral_En,err=spint.quad(ecuacion_En,0,Lx)

    En=integral_En*(2*A/Lx)
    
    return En

#Se define un arreglo de rho, donde se guardarán las soluciones de las sumatorias para 
#cada valor de t y x según corresponda
p=np.zeros((len(t),len(x)))

#Se definen ciclos que recorran para cada valor de tiempo, todos los valores de espacio
#y que realice las sumatoria respectiva a la solucion del problema en cada punto, para todos los valores de n
for m in range(0,len(t)):
    for j in range(0,len(x)):
        for i in range(1,n):
            p[m,j]+= Coeficientes(x[j],x0,l,i,A,Lx)*Ecuacion_T(t[m],i,D,Lx)*Ecuacion_X(x[j],i,Lx)
            
#Creacion del gráfico
X, T = np.meshgrid(x, t)
pLt.figure(figsize=(10,6))
ax = pLt.axes(projection='3d')
ax.set_xlabel('Tiempo (t)')
ax.set_ylabel('Distancia (x)')
ax.set_zlabel('Difusión de calor')
ax.plot_surface(T,X, p, rstride=1, cstride=1, cmap='cividis', edgecolor='none')
ax.set_title('Aproximacion de difusión por Series de Fourier')
pLt.show()

print("--- %s segundos ---" % (time.time() - start_time))