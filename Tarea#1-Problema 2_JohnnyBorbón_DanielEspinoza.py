#Tarea 1. Problema 2 - ITCR.Física Computacional
#Johnny Borbón Valverde (2018093752)
#Daniel Espinoza Castro (2018209624)

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

#Sympy permite realizar cálculos simbólicamente
#Diff para calcular derivadas de una función con respecto a una variable simbolica
from sympy import diff
#Siymbols para introducir los simbolos que representaran las variables de la ecuacion
from sympy import symbols
#Subs permite sustituir valores por las variables de una ecuacion y evaluarlas
from sympy import Subs

#Se introducen el simbolo t que corresponde a la variable de tiempo en la ecuacion
t= symbols('t')


def Funcion_General(posicion_Inicial, aceleracion_Constante, velocidad_Inicial, parámetro_Inicial ):
   
    """
    Generar función de movimiento rectilíneo uniformemente acelerado de posicion 
    en funcion del tiempo, dados los parámetros anteriores además del parámetro
    inicial a utilizar en la funcion de Newton Raphson.
    
    Además, se calcula la derivada de la función generada, utilizando la funcion
    diff de la biblioteca Sympy.
    
    El parámetro_Inicial consiste en el primer parámetro para realizar el método 
    Newton Raphson, el cual tiene que ser un valor positivo ya que el valor
    resultante corresponde a una magnitud de tiempo y el tiempo no puede ser
    negativo y si es 0,el método diverge.
    
    """
    if parámetro_Inicial <= 0:
        print("El parámetro inicial escogido no es válido ya que el tiempo resultante no puede tener valores negativos o diverge el método Newton Raphson.")
    else: 
        
        #Se definen variables temporales
        x0 = posicion_Inicial
        v0 = velocidad_Inicial
        a = aceleracion_Constante
        
        #Se genera la funcion de movimiento de posicion del tiempo
        x = x0 + v0*t + 0.5*a*t**2
        
        #Se genera la derivada 
        derivada = x.diff(t)
        
        print("Función de Posición con respecto al tiempo:")
        print("x =" '{}'.format(x))
        print("\n")
        
        print("Derivada de la Función")
        print("dx/dt =" '{}'.format(derivada))
        print("\n")
    
        Newton_Raphson(parámetro_Inicial, x, derivada)
   

def Newton_Raphson(parámetro_Inicial, funcion, derivada):
    
    """
    Aplicar el método de Newton Raphson dado el parámetro inicial, la funcion y
    su derivada generada en la funcion Funcion_General
 
    El error empieza siendo 1 para que se pueda ejecutar el ciclo con la
    condicion de que se ejecute Newton Raphson hasta que el error sea menor a
    1%
    
    """
    t0 = parámetro_Inicial
    
    #Para encontrar el error en la primera aproximacion y determinar su incertidumbre
    #Valor que resuelve teóricamente el problema 2 (tiempo cuando x = 0m)
    valor_Real = 31.6227766
    
    #Contador
    i = 0
    
    #Lista que almacena los resultados de cada iteracion 
    aproximaciones_NR = []
    
    error = 1
    
    while error > 0.01:
        
        #Se definen variables temporales
        fx =  funcion.subs(t,t0)
        dfx= derivada.subs(t,t0)
        
        NR = t0 - fx/(dfx)
        
        print("Newton Raphson = "'{}'.format(NR))
        print("Número de iteración:", len(aproximaciones_NR))
        
        
        aproximaciones_NR.append(NR)
      
        t0 = NR
        
        #Error con respecto al valor exacto teórico
        error = abs(aproximaciones_NR[i]-valor_Real)
        print("Error Absoluto con el valor exacto", error)
        print("\n")
        

        i= i+1  
                
            
            
        
        
       
    

