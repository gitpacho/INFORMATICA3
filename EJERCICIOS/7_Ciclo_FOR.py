# 09-09-2022
# EJERCICIOS BASICOS- CICLO FOR

alturas = [10,20, 50, 80, 1, 50]
pesos = (70, 60, 55, 62, 45, 90)
mensaje = "Hola Mundo Cruel"
secuencia = range(1, 11, 1)

print("\n\nIterable 1")
for altura in alturas:
    print(altura, end="-")
print("\n\niterable 2")
for peso in pesos:
    print(peso, end="-")
print("\n\nIterable 3")
for letra in mensaje:
    print(letra, end="-")
print("\n\nIterable 4")
for i in secuencia:
    print(i, end="-")

"""Utilizar ciclo for para recorrer los anteriores iterables
sin necesidad de definirlos en las variables alturas,pesos,mensaje,
rango,"""


print("\n\n-----Recorrido de iterables sin necesidad de definirlos----")

print("\n\nIterable 1")
for altura in [10,20, 50, 80, 1, 50]:
    print(altura, end="-")

print("\n\niterable 2")
for peso in (70, 60, 55, 62, 45, 90):
    print(peso, end="-")

print("\n\nIterable 3")
for letra in "Hola mundo cruel":
    print(letra, end="-")

print("\n\nIterable 4")    # Esta es la manera más usada y tiene mucha practicidad
for i in range(1,10):
    print(i, end="-")


"""
Utilizando el ciclo for generar las siguientes secuencias:
     * 10,11,12,13,14,15,16, .. 20
     * 3, 6, 9, 12, 15, 18, 21, 24, 27, 30
     * 3, 6, 9, 12, 15, 18, 21, 24, 27, 33, 36, 39, 42, 45
     * numeros pares del 200 al 400
     * las primeras 20 potencias de 2
     * Numeros del 1 al 10
     * a b c d e f g h i j k l m n o p q r s t u v w x y z
     * 1 2 3 4 8 11 21 100 21 32
"""

print("\n\nSecuencia => 10, 11, 12, 13, 14, 15, 16, .. 20")
for i in range(10, 21):
    print(i, end = " ")

print("\n\nSecuencia =>  3, 6, 9, 12, 15, 18, 21, 24, 27, 30")
for i in range(3, 31, 3):
    print(i, end = " ")


print("\n\nSecuencia =>  3, 6, 9, 12, 15, 18, 21, 24, 27, 33, 36, 39, 42, 45")

for i in range(3, 46, 3):
    if i != 30:
        print(i, end = " ")

#print("\n")
#for i in range(3, 46, 3):
#    if i == 30:
#        continue
#    print(i, end = " ")



print("\n\nNúmeros pares del 200 al 400==>")
for i in range(200, 401, 2):
    print(i, end = " ")

print("\n\nlas primeras 20 potencias de 2 ==>")

for i in range(1,21):
     print(2**i, end = " ")




"""
Programa que determine si un número n es primo
"""

print("\n\nDETERMINE SI ES PRIMO")     