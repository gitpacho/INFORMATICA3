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

derivada1 = np.diff(columna1)/np.diff(x)
derivada2 = np.diff(columna2)/np.diff(x)
derivada3 = np.diff(columna3)/np.diff(x)

"""
1) Crear una funcion generica para graficar las derivadas
2) Crear un dataFrame que contenga los valores de las 3 derivadas en 
                            columns = ["der1", "der2", "der3"]
"""


