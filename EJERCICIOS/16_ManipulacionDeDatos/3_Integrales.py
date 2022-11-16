#16-11-2022

#----------- Integrales numericas-------------

#Se resuelve utilizando el metodo del trapecio (calculando areas)

"""
    Ejercicio: 
    Calcular la integral para f(x) = 2x², en los limites x = [0,5]
    La integral debe dar (2/3)x³ [x=0,x=5] = 83.33333333333333
"""

import numpy as np
import matplotlib.pyplot as plt

def graficaGenerica(x,y):
    plt.figure()
    plt.plot(x,y,"o")
    plt.show()

limite_inferior = 0
limite_superior = 5
salto = 0.001
x = np.arange(limite_inferior, limite_superior + salto, salto)
y = 2 * (x ** 2)

integral_numerica = np.trapz(y,x)
print("teorico = 83.33333333333333")
print("numerico=", integral_numerica)

#graficaGenerica(x,y)



"""
Ejercicio:  
 a) graficar f1,f2,f3 en un mismo lienzo
 b) calcular las integrales de f1, f2 y f3 del dataFrame hoja1

"""
import pandas as pd
x = np.arange(0, 6.28, 0.01)
columna1 = x * np.sin(x) + 0.005 * np.random.rand(628)
columna2 = np.cos(x) + 0.005 * np.random.rand(628)
columna3 = x * 1/2
data = np.hstack((columna1.reshape(628,1), columna2.reshape(628,1), columna3.reshape(628,1)))
hoja1 = pd.DataFrame(data= data,
                     index= x,
                     columns= ["f1", "f2", "f3"])

print(hoja1)

plt.figure(figsize=(12,4))
for i in range(1,4):
    plt.subplot(1,3, i)
    x = hoja1.index
    y = hoja1.iloc[:,i-1]
    plt.plot(x, y)
plt.show()


for i in range(0,3):
    x = hoja1.index
    y = hoja1.iloc[:,i]
    integral_numerica = np.trapz(y,x)
    print("integral f{} = ".format(i+1), integral_numerica)








