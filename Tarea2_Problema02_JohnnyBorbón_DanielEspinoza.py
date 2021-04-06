#Tarea 2. Problema 2 - ITCR.Física Computacional I
#Johnny Borbón Valverde (2018093752)
#Daniel Espinoza Castro (2018209624)

import numpy as np
import scipy.integrate as spint

#Definir la Función de presion en funcion de la altura con la temperatura en funcion de la altura incluida
def F(y,p):
    M=0.0289647
    g=9.8
    R=8.314462
    valorf=(-M*p*g)/(R*(293-(y/200)))
    return valorf            

#Estableciendo condiciones iniciales
y0=0.0
p0=101325.0
y=3000

#Para que logre hacer las 30 iteraciones, se defne n=31 para que divida 
#los valores de el intervalo de 0 a 3000 entre 30 y asi devuelva el resultado
#para cada valor de altura aumentando en 100 metros
n=31
h=np.linspace(y0, y, n)

#Contadores para recorrer las listas de los resultados
i=0 

#Se aplican los métodos utilizando la biblioteca de scipy
metodoRK45 = spint.solve_ivp(F,[y0, y], [p0],t_eval=(h), method= 'RK45')

#Para imprimir los resultados del método Runge Kutta 45
print("Método de Runge Kutta 45")

#Un ciclo para poder mostrar cada resultado de la matriz de resultados
while i < len(metodoRK45.y[0]):
    #Se extrae el valor deseado de p(y) de interés
    p45 = metodoRK45.y[0][i]
    #Se asocia cada valor de puntos deseados h, para cada respuesta del método RK45
    print(i, " En h=", h[i]," p(h)=", p45, sep="") 
    
    i+=1
    
print("\n")



