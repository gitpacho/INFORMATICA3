""" Crear un ciclo infinito """


#while True:
#    print("ciclo ejecutado")


""" Crear un ciclo infinito, pero
protegerlo en caso de que se ejecute
más de 100 veces """

contador = 0
while True:
    print("ciclo ejecutado {}".format(contador))
    contador = contador + 1
    
    if contador > 100:
        print("Contador superado")
        print("Vamos a romper la ejecución")
        break

"""
Imprima los numeros del 20 al 50, utilizando el
ciclo while
"""
#Solución 1
contador = 20
while contador<51:
    print(contador)
    contador += 1

#Solución 2
contador2 = 20
while True:
    print(contador2)
    contador2 += 1
    if contador2 > 50:
        break

""" 
Mostrar en pantalla los primeros 10 numeros de la serie
de fibonacci
"""
(1,1,2,3, 5, 8, 13, 21, 34, 55)


print("-----fibonacci----")
n = 1
fib1 = 1
fib2 = 1
print(fib1)
print(fib2)

while n<9: # Yo prefiero colocar la condición aquí
    fibNext = fib1 + fib2
    print(fibNext)
    fib1, fib2 = fib2, fibNext
    n += 1
    

"""
Realice un programa que solicite
una contraseña, si la contraseña es
incorrecta, solicite la contraseña 
nuevamente.
en caso de que si coincida, 
termine el ciclo
"""

contraseñaUsuario = input("Ingrese una contraseña: ")
contraseñaOriginal = "1234"

while contraseñaOriginal != contraseñaUsuario:
    print("Contraseña incorrecta")
    contraseñaUsuario = input("Ingrese una contraseña: ")
    
print("Contraseña correcta")







