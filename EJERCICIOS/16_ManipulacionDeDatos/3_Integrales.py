#16-11-2022

#----------- Integrales numericas-------------

#Se resuelve utilizando el metodo del trapecio (calculando areas)

"""Calcular la integral para f(x) = 2x², en los limites x = [0,5]
La integral debe dar (2/3)x³ [x=0,x=5] = 83.33333333333333
"""

import numpy as np
import matplotlib.pyplot as plt

def graficaGenerica(x,y):
    plt.figure()
    plt.plot(x,y,"o")
    plt.show()

x = np.arange(0,5.5, 0.5)
y = 2 * (x ** 2)


integral_numerica = np.trapz(y,x)
print("teorico = 83.33333333333333")
print("numerico=", integral_numerica)

graficaGenerica(x,y)









