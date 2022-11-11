#11-11-2022

import pandas as pd
import numpy as np

"""Creamos el siguiente DataFrame (hoja1)"""

x = np.arange(0, 6.28, 0.01)
columna1 = x * np.sin(x) + 0.005 * np.random.rand(628)
columna2 = np.cos(x) + 0.005 * np.random.rand(628)
columna3 = x * 1/2
data = np.hstack((columna1.reshape(628,1), columna2.reshape(628,1), columna3.reshape(628,1)))
hoja1 = pd.DataFrame(data= data,
                     index= x,
                     columns= ["f1", "f2", "f3"])


""" 
 Para calcular derivadas se hace uso de su significado geometrico
 Una derivada es una pendiente de una funcion
    f'(x) = (y2-y1) / (x2 -x1)

 Ejemplo: calcular las derivadas de f1, f2 y f3
 """

derivada1 = np.diff(columna1)/np.diff(x)  #Pendientes de f1
derivada2 = np.diff(columna2)/np.diff(x)  #Pendientes de f2
derivada3 = np.diff(columna3)/np.diff(x)  #Pendientes de f2

"""
1) Crear una funcion genérica para graficar las derivadas
2) Crear un dataFrame que contenga los valores de las 3 derivadas en 
                            columns = ["der1", "der2", "der3"]
"""

#1er punto

import matplotlib.pyplot as plt
def graficaGenerica(x, y, y_prima, titulo):
    plt.figure(figsize=(8,4))
    plt.title(titulo)
    plt.plot(x,y, "b", label="funcion f(x)")
    plt.plot(x[:-1], y_prima, "r", label="derivada f '(x)")
    plt.xlabel("x")
    plt.legend()  #para mostrar los labels f(x) y f '(x)
    plt.show()

x = hoja1.index
y = hoja1["f1"]
y_prima = derivada1
graficaGenerica(x, y, y_prima, "f(x) = xsen(x)")

x = hoja1.index
y = hoja1["f2"]
y_prima = derivada2
graficaGenerica(x, y, y_prima, "f(x) = cos(x)")

x = hoja1.index
y = hoja1["f3"]
y_prima = derivada3
graficaGenerica(x, y, y_prima, "f(x) = x + 1/2")


#2do punto => pendiente crear data frame de derivadas
