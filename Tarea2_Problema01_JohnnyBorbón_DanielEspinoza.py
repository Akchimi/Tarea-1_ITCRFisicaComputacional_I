#Tarea 2. Problema 1 - ITCR.Física Computacional I
#Johnny Borbón Valverde (2018093752)
#Daniel Espinoza Castro (2018209624)

def F(y,p):
    """
    Definir la función que describe la variación de la presión con la altura 
    sobre el nivel del mar incluyendo la variación de la temperatura con
    respecto a la altura
    """
    #Se definen las constantes establecidas
    M=0.0289647
    g=9.8
    R=8.314462
    #Sustituir los valores en la función donde "p" es presión y "y" la altura
    valorf=(-M*p*g)/(R*(293-(y/200)))   
    return valorf

#Método de RK4
def RK4(f,x0,y0,h):
    """
    Definir el método de Runge Kutta 4 con las variables dadas que se 
    sustituirán mas adelante
    """
    #Se definen los valores de k
    k1=h*f(x0,y0) 
    k2=h*f(x0+h/2, y0+k1/2)
    k3=h*f(x0+h/2, y0+k2/2)
    k4=h*f(x0+h, y0+k3)
    
    #Se construye el método con los valores de k
    y=y0+(k1+2*k2+2*k3+k4)/6
    return y

#Estableciendo condiciones iniciales
y0=0.0
p0=101325.0
y=3000.0
h=100
cont=0

print("Método de Runge Kutta de orden 4")

#Se imprime el valor de la presión a altura = 0m
print(cont,")"," En h=",y0," p(h)=", p0, sep="") 

while y0<3000:
    #Se llama el método de RK4 para crear una iteracion nueva
    NuevaP=RK4(F,y0,p0,h)
    p0=NuevaP
    y0+=h
    cont+=1
    #Se imprime el resultado de dicha iteración
    print(cont,")"," En h=",y0," p(h)=", p0, sep="") 

#resultadoRK4=RK4(F,y0-100,p0,y,n)   
#print(resultadoRK4)
#print("-------RK4-------")
#print("En h=",y," p(h)=", resultadoRK4, sep="")