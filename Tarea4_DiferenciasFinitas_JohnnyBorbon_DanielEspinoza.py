#Tarea 4- Diferencias finitas - ITCR.Física Computacional I
#Johnny Borbón Valverde (2018093752)
#Daniel Espinoza Castro (2018209624)

import numpy as np
import matplotlib.pyplot as plt
import time

#Contador de Tiempo
start_time = time.time()
#Se definen las constates del problema
D=0.5
Lx=10.0
A=2.0
x0=5.0
l=1.5

#Se define la precisión de la aproximación resultante deseada
prec = 0.01

# Se definen los parámetros que crearán la malla de puntos para evaluar en cada uno el
# valor de difusión de calor
Lt = Lx
#Cantidad de puntos de cada malla
puntosmalla_x = 100
puntosmalla_t = 1000

#se define la variable de separación para los puntos de espacio y tiempo
delta_x = Lx/puntosmalla_x
delta_t = Lt/puntosmalla_t

#Se crean arreglos que contengan los puntos de espacio y tiempo respectivos
x = np.linspace(0, Lx, puntosmalla_x)
t = np.linspace(0, Lt, puntosmalla_t)

# Se crea la matriz inicial según los parámetros definidos anteriormente
pxti = np.zeros((puntosmalla_x, puntosmalla_t), float)

# Se establecen los valores iniciales de la malla, usando las condiciones de frontera 
# para el caso particular de la placa unidimensional

for i in range(0, puntosmalla_x):
    """
    Se utilizan las condiciones de frontera de manera que: 
    p(0,t)=p(Lx,t) = 0
    p(x,0)=A*np.exp((-(x[i]-x0)**2)/l)
    
    ----------------------------------------------------------
    Como ya la matriz es de ceros, se procede a calcular la condicion de frontera
    para la primer columna, cuando t=0
    
    """
    pxti[i,0] = A*np.exp((-(x[i]-x0)**2)/l)

def AproxPXT(pxt, pm_x,pm_t, prec, D, delta_x,delta_t):
    '''Calcula el valor aproximado de la difusión de calor en el punto (x, t)
 
    Parámetros de la función
    ------------------------
    pxt : matriz con los valores iniciales de difusión de calor en cada
           punto de la malla
    pm_x : número de puntos espaciales de la malla
    pm_t : número de puntos temporales de la malla
    prec : precisión requerida para el cálculo aproximado de los valores del
            potencial en la malla
 
    Salida de la función
    --------------------
    valorAproxPXT : matriz con los valores finales de difusión de calor en
                    cada punto de la malla
    '''

    # Se define el contador de iteraciones
    contador_iteraciones = 0

    # Se define una variable de control como 1 para que se pueda ejecutar el metodo iterativo 
    # Esta variable controla la continuidad del ciclo 
    #dif será el valor de la diferencia finita entre la malla anterior y la actulizada 
    dif = 1

    
    while dif > prec:
      # Se aumenta el contador de interaciones en 1 unidad por cada vez que se realiza el ciclo
      contador_iteraciones += 1

      for n in range(0, pm_t-1, 1):
        for m in range(1, pm_x-1, 1):
          # Se crea una matriz a partir de la matriz ingresada 
          pxt_anterior = pxt[m, n]
          
          # Se aplica el método de Gauss-Siedel para esta EDP particula
          pxt[m, n+1] =  pxt_anterior + (D*delta_t*(pxt[m+1,n]+pxt[m-1,n]-2*pxt[m,n]))/(delta_x**2)
         
          # Se calcula la diferencia finita de las matriz resultante de Gauss-Seidel menos la matriz anterior
          dif = np.abs([pxt[m,n+1]-pxt_anterior])[0]
        
        # Se define una condicion para que se detenga el método iterativo al máximo de 500 iteraciones
        if contador_iteraciones > 500:
          break
     
    #Se imprime la cantidad de interaciones alcanzadas al llevar a cabo el método
    valorAproxPXT = pxt
    print("Cantidad iteraciones para alcanzar precisión: ", contador_iteraciones)
    return valorAproxPXT





# Se llama la función AproxPXT y se guarda en la variable Z ya que será en dicho eje
# en donde se proyecte la difusión de calor de la placa en el gráfico
Z = AproxPXT(pxti, puntosmalla_x, puntosmalla_t, prec/1000, D, delta_x,delta_t)    

#Procedimiento de graficación
X,T = np.meshgrid(x, t)
plt.figure(figsize=(10,6))
ax = plt.axes(projection='3d')
ax.set_xlabel('Tiempo (t)')
ax.set_ylabel('Distancia (x)')
ax.set_zlabel('Difusión de calor')
ax.plot_surface(T,X, Z.T, rstride=1, cstride=1, cmap='cividis', edgecolor='none')
ax.set_title('Aproximacion de la difusion por diferencias finitas')
plt.show()

print("--- %s segundos ---" % (time.time() - start_time))