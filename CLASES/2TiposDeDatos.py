# Declaramos los siguientes elementos y asignamos
# en variables de su elección:

# Enteros: 10, -100, 500, 200  ==> Luego restelos
#                                  de manera sucesiva

a = 10
b = -100
c = 500
d = 200
resultado = a - b - c - d
print("Resultado1 = ", resultado)

# Flotantes: 100.0, 305.2, 400.3 ==> dividalos de manera
#                                    sucesiva

A, B, C = 100.0, 305.2, 400.3
resultado = A / B / C
print("Resultado2 = ", resultado)

# Booleanos: True, False         ==> primero sumelos
#                                    luego restelos

a = True
b = False
sumaBooleanos = a + b
restaBooleanos = a - b

print(sumaBooleanos)
print(restaBooleanos)

# Strings: "Cristian", "Juanita"  ==> sumelos, restelos
#           "", '', """", "''"    ==> ¿Qué sucede? 

nombre1 = "Cristian"
nombre2 = "Juanita"
cadena1 = ""     # Si se puede
cadena2 = ''     # Si se puede
#cadena3 = """"    Esto no se puede hacer
cadena4 = "''"   # Esto si se puede hacer

print("nombre1 => ", nombre1)
print("nombre2 => ", nombre2)
print("cadena1 => ", cadena1)
print("cadena2 => ", cadena2)
print("cadena4 => ", cadena4)

suma = nombre1 + nombre2        # Si se puede (concatenación)
print("suma => ", suma)         # Si se puede (concatenación)
#resta = nombre1 - nombre2      # No se puede
#print("resta => ", resta)      # No se puede

#Busque la manera de convertir: (casteo)
# Un entero a un flotante
# Un flotante a un entero
# Un flotante y un entero a un string
# Un string a un entero y flotante
# Un booleano a un entero y flotante
# Un entero y flotante a booleano

entero = 10
flotante = 11
string = "Manizales"
string2 = "123"
booleano = True

print("E a F ==> ", entero,   float(entero))
print("F a E ==> ", flotante, int(flotante)) 
print("F a S ==> ", flotante, str(flotante))
print("E a S ==> ", entero,   str(entero))
print("S a E ==> ", string2,   int(string2))     # Solo castea si es posible
print("S a F ==> ", string2,   float(string2))   # Solo castea si es posible
