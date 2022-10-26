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
imprimir 10 numero aleatorio. opciones: 1,2,3,4,5
imprimir 10 caracter aleatorio. opciones: "a", "b", "c"
"""
print("numero aleatorio [0,1)")
for i in range(10):
    numeroAleatorio = random.random()
    print(numeroAleatorio)


print("numero aleatorio [1,2,3,4,5]")
for i in range(10):
    numeroAleatorio = random.choice([1,2,3,4,5])
    print(numeroAleatorio)

print("caracter aleatorio a,b,c")
for i in range(10):
    caracterAleatorio = random.choice(["a", "b", "c"])
    print(caracterAleatorio)


import tqdm

for i in tqdm.tqdm(range(200000000)):
    10 * 5
print("proceso Terminado")