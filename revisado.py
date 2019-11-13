import numpy as np# libreria con metodos para operar matrices
import random as rn

print("ingrese el numero de variables")
n = int(input())
print("ingrese el numero de restricciones \n")
m = int(input())

matrixA = np.ones((m, n), dtype=float)#Matriz de coheficientes de restricciones 
matrixb = np.ones(m, dtype=float)#Matriz valores de restricciones
matrixZ =np.ones(n, dtype=float)#Matriz valores de coheficientes funcion objetivo

#llenar matriz de coheficientes A y b
for i in range(m):
    print("Restriccion ",i+1)
    for j in range(n):
        print("\n ingrese el valor de X"+str(j+1))
        matrixA[i][j]=float(input())
        if(j+1==n):
            print("\n Ingrese el valor de la restriccion b"+str(i+1))
            matrixb[i]=float(input())

print ("\n Ingrese la función objetivo a maximizar \n")
for i in range(n):
    print ("\n ingrese el valor de X"+str(i+1))
    matrixZ[i]=float(input())


print ("\n Matriz A \n",matrixA,"\n")
print ("\n Matriz b \n",matrixb,"\n")
print ("\n Función objetivo Matriz Z \n",matrixZ)

matrixXB = np.ones(n, dtype=float)#matriz de variables basicas
matrixCB = matrixZ[n-m:]#obtiene las variables de los coheficientes de las restricciones
print ("\n Matriz CB \n",matrixCB,"\n")
matrixB = np.identity(m)#Matriz de variables basicas o identidad en la iteracion 0
print ("\n Matriz B \n",matrixB,"\n")
matrixBINV = np.linalg.inv(matrixB)#Matriz B inversa  
print ("\n Matriz B iversa \n",matrixBINV,"\n")
matrixXB =np.dot(matrixBINV,matrixb)
print ("\n Matriz XB \n",matrixCB,"\n")

z = np.dot(matrixCB,matrixXB)
print ("\n Valor de z \n",z,"\n")

#  ----------------------ITERACION 0-------------------------------------------------
############################################################################################################
#------------------------FASE 1------------------------------------------------------

