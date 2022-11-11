import pandas as pd
import numpy as np

"""
Creamos un dataFrame con 3 columnas: ["F1", "F2", "F3"]
                         100 indices: [0.01, 0.02 ..0.99, 1] (valores de x)

F1(x) = xsin(x) + 0.2*random(x)
F2(x) = cos(x) +  0.1*random(x) 
F3(x) = x + 1/2
 """

x = np.arange(0.01, 1.01, 0.01)
columna1 = x * np.sin(x) + 0.2 * np.random.rand(100)
columna2 = np.cos(x) + 0.1 * np.random.rand(100)
columna3 = x * 1/2
data = np.hstack((columna1.reshape(100,1), columna2.reshape(100,1), columna3.reshape(100,1)))

hoja1 = pd.DataFrame(data= data,
                     index= np.arange(0.01, 1.01, 0.01),
                     columns= ["F1", "F2", "F3"]
)


import matplotlib.pyplot as plt

"""
Graficar F1(x), F2(x), F2(x)
"""

def graficaGenerica(x, y, marca):
    plt.figure()  #Para crear lienzo vacio
    plt.plot(x, y, marca)
    plt.show()    #Para mostrar la figura

x = hoja1.index
y = 

















