#30-09-2022


""" 
crear la siguientes listas

lista1 = [1,2,3,4,5,6,7,8]
lista2 = list(range(20)) + ["a", "b", "c", 100]
lista3 = ["cruel", "mundo", "hola", 1, 100, 200, 500]

Realice lo siguiente:

*Agregar al final de lista1, los elementos => 1,2,3,4
*Agregar al comienzo de lista1, los elementos => 0,0,2,4
*Eliminar los 3 ultimos elementos de lista1
*Eliminar los 2 primeros elementos de lista1

*Sume todos los elementos de lista 2 que pueden operarse algebraicamente
*Organice lista2 de forma ascendente
*Elimine todos los elementos de lista2 original que son enteros 

*Sume todos los elementos de lista3 que pueden operarse algebraicamente
 sin alterar ni cambiar lista3 original
*Haga una copia de lista3 de la siguiente manera
 lista3Copia = lista3
 y agregue 3 nuevos elementos sobre esta nueva lista.
 ¿qué sucede con la lista3 original?
*Encuentre una manera de alterar la copia sin afectar la lista original

INDEXADO => Extraer el elemento inicial de lista1  (de dos maneras)
            Extraer el elemento final de lista1  (de dos maneras)
            Extraer el elemento del medio de lista2 (de dos maneras)
SLICING  => Extraer los primeros 3 elementos de lista1, lista2 y lista3
             y colocarlos en una nuevaLista
            Extraer cada 2 elementos de lista 2
            Extraer todos los elementos de lista3 al revés
            Extraer los elementos de lista3 ubicados en indices impares

"""



### ===============> SOLUCION

lista1 = [1,2,3,4,5,6,7,8]
lista2 = list(range(20)) + ["a", "b", "c", 100]
lista3 = ["cruel", "mundo", "hola", 1, 100, 200, 500]

print("Agregar al final de lista1, los elementos => 1,2,3,4")
lista1.append(1)
lista1.append(2)
lista1.append(3)
lista1.append(4)
print(lista1)


print("*Agregar al comienzo de lista1, los elementos => 0,0,2,4")
lista1.insert(0, 4)
lista1.insert(0, 2)
lista1.insert(0, 0)
lista1.insert(0, 0)
print(lista1)

print("*Eliminar los 3 ultimos elementos de lista1")
lista1.pop(-1)  # Si se elimina el ultimo elemento no es necesario colocar el indice

lista1.pop(-1)  # Si se elimina el ultimo elemento no es necesario colocar el indice
lista1.pop(-1)  # Si se elimina el ultimo elemento no es necesario colocar el indice
print(lista1)


print("*Eliminar los 2 primeros elementos de lista1")
lista1.pop(0)  #El 0 representa el indice cero, cuyo elemento es 0 en esta ista   
lista1.pop(0)  #El 0 representa el indice cero, cuyo elemento es 0 en esta ista
print(lista1)

print("Sume todos los elementos de lista 2 que pueden operarse algebraicamente")
lista2.remove("a")
lista2.remove("b")
lista2.remove("c")
resultado = sum(lista2)
print(lista2, resultado)

print("*Organice lista2 de forma ascendente")
lista2.sort(reverse = True) #Por defecto organiza de manera ascendente, para hacerlo descendente hay que utilizar el parametro reverse
print(lista2)


print("*Elimine todos los elementos de lista2 original que son enteros ")
lista2 = list(range(20)) + ["a", "b", "c", 100]
listaApoyo = []
for elemento in lista2:
  if type(elemento) == str:
    listaApoyo.append(elemento)
  else:
    pass
lista2 = listaApoyo
print(lista2)



print("""
*Sume todos los elementos de lista3 que pueden operarse algebraicamente
 sin alterar ni cambiar lista3 original
""")

lista3Copia = lista3.copy()

print("""
*Haga una copia de lista3 de la siguiente manera
 lista3Copia = lista3
 y agregue 3 nuevos elementos sobre esta nueva lista.
 ¿qué sucede con la lista3 original?
""")
lista3Copia = lista3  # Esto no es una verdadera copia, esto es un nuevo apodo a
                      # a la lista3 original
lista3Copia.append("Cristian")
lista3Copia.append("Elias")
lista3Copia.append("Pachon")

print(lista3, "original sin afectar \"supuestamente\"")
print(lista3Copia, "copia afectada \"solamente\"")

lista1 = [1,2,3,4,5,6,7,8]
lista2 = list(range(20)) + ["a", "b", "c", 100]
lista3 = ["cruel", "mundo", "hola", 1, 100, 200, 500]
print("Extraer el elemento inicial de lista1")
print(lista1[0], lista1[-8])

print("Extraer el elemento final de lista1  (de dos maneras)")
print(lista1[7], lista1[-1])

print("Extraer el elemento del medio de lista2 (de dos maneras)")
print(lista2[11], lista2[-13])

print("""Extraer los primeros 3 elementos de lista1, lista2 y lista3
             y colocarlos en una nuevaLista""")
print(lista1[0:3] + lista2[0:3] +lista3[0:3])

print("Extraer cada 2 elementos de lista 2")
print(lista2[::2])

print("Extraer todos los elementos de lista3 al revés")
print(lista3[::-1])

print("Extraer los elementos de lista3 ubicados en indices impares")
print(lista3[1::2])
print(lista3)
