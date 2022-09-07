"""
Determine si un numero es mayor a 18, 
utilizando el condicional IF
"""

numero = 18
if numero > 18:
    print("Numero es mayor a 18")

"""
Determine si un numero es mayor o no a 18, 
utilizando el condicional IF-ELSE
"""
numero = 18
if numero > 18:
    print("Numero es mayor a 18")
else:
    print("Numero no es mayor a 18")


"""
Pedir a el usuario que ingrese 3 numeros,
luego, imprimir el numero mayor y el menor
"""

numero1 = int(input("Ingrese primer numero: "))
numero2 = int(input("Ingrese segundo numero: "))
numero3 = int(input("Ingrese tercer numero: "))

mayor = 0

if (numero1 >= numero2) and (numero1 >= numero3):
    mayor = numero1
elif (numero2 >= numero1) and (numero2 >= numero3):
    mayor = numero2
elif (numero3 >= numero1) and (numero3 >= numero2):
    mayor = numero3

print("El numero mayor es {}".format(mayor))











