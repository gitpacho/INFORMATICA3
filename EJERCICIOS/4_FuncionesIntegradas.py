#02-09-2022

#----------- Funciones de entrada (input) y salida print --------------

"""  
 - Solicitar una clave y luego responder en pantalla si es correcta o no. 
                                                     clave = "Unal2022"
 - Solicitar un numero y luego responder en pantalla si es mayor a 18 
 """


#clave_real = "Unal2022"
#clave_usuario = input("Ingrese su clave: ")
#print((clave_usuario == clave_real and "La clave es correcta") or "La clave es incorrecta")

#numero = 18
#numero_usuario = int(input("Ingrese un número :  "))
#print((numero_usuario > numero   and "Mayor a 18") or "No es mayor a 18")



#--------- funciones de formateo de valores numericos => format(valor, tipo)

#formato cientifico
numero = 1028091280
formato_cientifico = format(numero, "e")
print(formato_cientifico)
formato_cientifico = format(numero, ".2e")
print(formato_cientifico)

"""  exprese el numero 0.000 000 029 213 en formato cientifico con 3 decimales """

numero = 0.000000029213
print("original = ", numero, "cientifico =", format(numero, ".3e"))

#formato flotante
numero = 12.1392
print(format(numero, ".2f"))

numero1 = 0.045
numero2 = 12.531

""" - formatear numero1 a flotante con un decimal
    - formatear numero2 a entero"""


#-----------------Funciones de Ayuda (help, dir, type) --------------

""" 
 Determine el tipo de dato de los siguientes mostrados (type)
  * {"1", "2"}
  * {1:2}.items()
  * range(1,10)
  * "1"
  * 1
  * (1,)

 
 ¿qué funcionalidades tienen los tipos de datos: int, float, str, set?
 """

entero = 1
flotante = 2.54
cadena = "hola"
conjunto = {1,2,3,4}

print("----Funcionalidades enteros -------")
for funcion in dir(entero):
  print(funcion)

print("----Funcionalidades cadenas -------")
for funcion in dir(cadena):
  print(funcion)



#----------------- funciones de conversion (bin, oct, hex, int)-----------------

""" 
 Convertir a binario, octal y hexadecimal los siguientes numeros:
 1, 8, 513 
 """

print("numero 1 a bin, oct, hex ==>", bin(1), oct(1), hex(1))
print("numero 8 a bin, oct, hex ==>", bin(8), oct(8), hex(8))
print("numero 513 a bin, oct, hex ==>", bin(513), oct(513), hex(513))

"""Convertir a decimal los numeros: 0b1000000001 0o1001 0x201"""

print(int("0b1000000001", 2))
print(int("0o1001", 8))
print(int("0x201", 16))





#------- Funciones para secuencias --------------

#secuencia => rango, lista, tupla .....


"""Crear una secuencia con los numeros del 1 al 10"""
secuencia1 = [1,2,3,4,5,6,7,8,9,10]
secuencia2 = (i for i in [1,2,3,4,5,6,7,8,9,10])
secuencia3 = range(1, 11, 1)     # el primer valor si se toma, el segundo valor no se toma
print(list(secuencia3))

""" 
 Cree las siguientes secuencias
--->   2,4,6,8,10,12 .... 50
--->   0,3,6,9,12,15,18 .... 200
--->   10, 9, 8 , 7, 0
--->   numeros multiplos del 2 y 3 entre 100 y 3 ==> 96,90,84....6
--->   numeros multiplos de 15 entre 1000 al 900

"""
print(list(range(2,51,2)))
print(list(range(0, 201, 3)) + [200])
print(list(range(10,-1,-1)))
print(list(range(96,5,-6)))
print(list(range(990,899,-15)))

""" 
Luego calcule el tamaño, maximo, minimo y la suma de los elementos de la última secuencia creada
len(), min(), max(), sum()
"""

#------------ funciones de mapeo (map) y filtrado (filter)

secuencia = range(990,-1,-15)

""" 
mapear la anterior secuencia de la siguiente manera:
     a) Multiplicar cada elemento por 3.1
     b) Convertir los números a cadenas
     c) Transformar los numeros al residuo entre 5 """
""" 
 Filtrar la anterior secuencia de la siguiente manera:
     a) Retener solo los números pares
     b) Retener solo los numeros que al sumarles 5 sean pares
     c) Retener solo los números cuyo primer digito sea par
 """

# solucion mapeado punto a
def multiplicacion(elemento): #Puede devolver lo que interese hacer, no necesariamente True o False
  return elemento * 3.1
print(list(map(multiplicacion, secuencia)))


# solucion filtrado punto a
def esPar(elemento): #debe devolver True or False
  return elemento % 2 == 0
print(list(filter(esPar, secuencia)))