import pandas as pd
import numpy as np

"""
Utilizamos el data frame del archivo anterior
 """
x = np.arange(0.01, 1.01, 0.01)
columna1 = x * np.sin(x) + 0.2 * np.random.rand(100)
columna2 = np.cos(x) + 0.1 * np.random.rand(100)
columna3 = x * 1/2
data = np.hstack((columna1.reshape(100,1), columna2.reshape(100,1), columna3.reshape(100,1)))
hoja1 = pd.DataFrame(data= data,
                     index= np.arange(0.01, 1.01, 0.01),
                     columns= ["F1", "F2", "F3"])


#------- Metodo numerico para calcular derivadas---------------
""" 
 Para calcular derivadas se hace uso de su significado geometrico
 Una derivada es una pendiente de una funcion
    f'(x) = (y2-y1) / (x2 -x1)
 """

derivada1 = np.diff(columna1)/np.diff(x)  #Pendientes de f1
derivada2 = np.diff(columna2)/np.diff(x)  #Pendientes de f2
derivada3 = np.diff(columna3)/np.diff(x)  #Pendientes de f2

"""
1) Crear una funcion genérica para graficar las derivadas
2) Crear un dataFrame que contenga los valores de las 3 derivadas en 
                            columns = ["der1", "der2", "der3"]
"""


import matplotlib.pyplot as plt

def graficaGenerica(x, y, y_prima):
    plt.figure(figsize=(8,4))
    plt.plot(x,y, "b", label="f(x)")
    plt.plot(x[:-1],y_prima, "r", label="f'(x)")
    plt.xlabel(x)
    plt.show()

x = hoja1.index
y = hoja1["F1"]
y_prima = derivada1


graficaGenerica(x, y, y_prima)






