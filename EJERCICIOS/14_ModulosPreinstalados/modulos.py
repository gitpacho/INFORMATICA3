#IMPORTANTE!

#1)Para ejecutar las siguientes lineas instale primero los modulos (random, math, calendar, matplotlib, numpy, tqdm ...)
#2)Los modulos se instalan en la terminal con: pip install <modulo> 
#3)Si los problemas persisten utilice google colab, que no requiere instalar los modulos

import math
"""
imprimir las variables pi y euler,
ejecutar al menos una funcion de ese modulo
"""

print("pi => ", math.pi)
print("euler => ", math.e)
print("seno(3.14/2) => ", math.sin(math.pi/2))


import random
"""
imprimir 10 numeros aleatorios. opciones: flotante del 0 al 1
imprimir 10 numeros aleatorios. opciones: 1,2,3,4,5
imprimir 10 caracteres aleatorios. opciones: "a", "b", "c"
"""
print("numero aleatorio [0,1)")
for i in range(10):
    numeroAleatorio = random.random()
    print(numeroAleatorio)

print("numero aleatorio 1,2,3,4,5")
for i in range(10):
    numeroAleatorio = random.choice([1,2,3,4,5])
    print(numeroAleatorio)

print("caracter aleatorio a,b,c")
for i in range(10):
    caracterAleatorio = random.choice(["a", "b", "c"])
    print(caracterAleatorio)


import tqdm
"""
Ejecutar un for con una barra de progreso
"""
for i in tqdm.tqdm(range(10000000)):
    10 * 5
print("proceso Terminado")


import calendar
"""
Imprimir un calendario
"""
print(calendar.calendar(2022))


import numpy  #pip install numpy
import matplotlib.pyplot as plt #pip install matplotlib
"""
Utilizar la estructura basica de numpy: un arreglo
luego graficar usando matplotlib (arreglo vs arreglo**2)
"""

arreglo1 = numpy.array([1,2,3,4,5])
arreglo2 = numpy.linspace(1, 50, 100)
arreglo3 = arreglo2 ** 2

plt.figure()
plt.plot(arreglo2, arreglo3)
plt.show()