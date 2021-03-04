from sympy import integrate
from sympy.abc import w

#Como el movil se mueve a aceleración constante la función a integrar será una recta
#Se crea una función que calcula la pendiente y otra para el intercepto de la recta 
#a partir de los parametros

def CalcPend(t1,t2,v1,v2):
    m=(v2-v1)/(t2-t1)
    return m

def CalcInter(t,v,m):
    b=v-m*t
    return b

#Se crea una función que calcula el h parte la funcion basado en la cantidad de puntos deseados
#Calcula el h, y evalua las imagenes en la función y almacena los datos de imagenes


def CalcImg(a,b,m,bEc,N):
    imagenes=[]
    h=(b-a)/(N-1)
    cont=0
    while cont<N:
        x=a+cont*h
        y=m*x+bEc
        imagenes.append(y)
        cont+=1
    return imagenes

#Ahora hay que programar el método de newton-cotes: Simpson, de acuerdo al esquema
#matemático visto en clase
    
def NCSimp(a,b,N,imagenes):
    h=(b-a)/(N-1)
    suma=0
    cont=0
    while cont<N:
        if cont==0 or cont==(N-1):
            x=imagenes[cont]
            suma+=x
        elif cont%2!=0:
            x=4*imagenes[cont]
            suma+=x
        elif cont%2==0:
            x=2*imagenes[cont]
            suma+=x
        cont+=1
    resultado=(h/3)*suma
    print('El resultado es:',resultado )
    return resultado

def CalcError(a,b,m,bEC,resultado):
    f=m*w+bEC
    resultadoINT= integrate(f,(w,a,b))
    error= resultadoINT-resultado
    print('La diferencia entre el valor exacto y el reportado es:', error)


a=float(input("Ingrese el valor del límite inferior de la integral: "))
b=float(input("Ingrese el valor del límite superior de la integral: "))
N=float(input("Ingrese la cantidad de puntos que desea usar: "))

if N%2!=0 and N>=3:
    m=CalcPend(0,100,0.5,1.0)
    bEC=CalcInter(0,0.5,m)
    imagenes=CalcImg(a,b,m,bEC,N)
    resultado= NCSimp(a,b,N,imagenes)
    CalcError(a,b,m,bEC,resultado)
else:
    print("Error: la cantidad de puntos debe ser impar y mayor a 3")
    
    