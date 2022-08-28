"""
En este archivo encontramos ejercicios con los siguientes temas: 
funciones integradas de python, uso de condicionales y ciclo while
"""

#====================== EJERCICIOS FUNCIONES INTEGRADAS ====================
#==> Ejercicio 1 
"""   (Intente no utilizar la sentencia if)
      a) Pedir al usuario que ingrese su edad, luego imprimir en pantalla si es mayor o menor de edad
      b) Pedir al usuario que ingrese su salario, luego imprimir si su salario es alto o bajo, (salario alto > $ 5000000)
      c) Pedir al usuario que ingrese 3 notas, luego avisar si aprueba o reprueba la materia
"""   

#==> Ejercicio 2 
"""   a) Determine el numero de metodos que tienen los strings, enteros, flotantes, listas, diccionarios,
      b) Determine el tipo de variable resultado de las siguientes operaciones:
         "123" + 3
         3 + "123"
         [] + []
         [1] + [1,2,3]
         (1,) + (1,2,3) 
         (1,2,3) + (1,)
         {"a", "b"} | {"c"}
         {"a", "b"} & {"a", "c"}
         False and 2
         True and 5
         False or 0
         True or 5
         1 and True"""

#==> Ejercicio 3 
""" Redondear los siguientes flotantes teniendo en cuenta cifras significativas. Round(<numero>, <decimales>)
      a) 2.572      0 cifras decimales
      b) 3.789      2 cifras decimales
      c) 0.392      1 cifra decimal
      d) 10.123913  4 cifras decimales
      e) 14.2293    2 cifras decimales
      f) 78.2569    1 cifra decimal"""

#==> Ejercicio 4 
"""Realizar las siguientes conversiones:
     a) Los decimales 512, 8, 128         ==>   a binario, octal, hexadecimal,
     b) Los binarios 1000, 10, 101        ==>   a decimal
     c) Los octales 563, 8, 64            ==>   a decimal
     d) Los hexadecimales ABC, 10A2, 9FF  ==>   a decimal"""

#==> Ejercicio 5 
"""Formatear (format(<numero>, <regla>)) los siguientes elementos:

      a) 0.52941, 2.389, 3.5, 200000 ==> entero
                                         flotante 2 decimales, 
                                         flotante 5 decimales,
                                         notación científica 1 decimal,
                                         notación científica 2 decimales, 

      b) "INFORMATICA 3" ==> En un ancho de linea de 20 palabras
                             alinear el string a la derecha
                             alinear el string a la izquierda
                             alinear el string en el centro

      c) Enteros 128, 64, 226  ==>  binario
                                    octal
                                    hexadecimal"""

#==> Ejercicio 6 
""" Crear las siguientes secuencias: 
       a) 1,2,3,4,5,6,...500
       b) 2,4,6,8,10,12...200
       c) 100, 99, 98, ..., 0
       d) -100, -95, -90, ... 100
       Use range(<inicio>, <fin>, <salto>), para visualizarlo utilice list(<secuencia>)"""

#==> Ejercicio 7 
"""Cree secuencias enumeradas utilizando las anteriores secuencias,
    para ello utilice la funcion integrada enumerate(<secuencia>),
    para visualizarlas utilice list(<secuencia_numerada>)"""

#==> Ejercicio 8 
"""A los siguientes iterables, calcule, el tamaño, la suma de elementos, valor mínimo y máximo
      ==> [200 300 1 2 3 4 231 21 54 6 76, 4, 32, 432, 654, 8, 435, 432]
      ==> (2, 4, 6, 8, 10 ...,  10000)
      ==> range(302, 10001, 3)
      ==> 'abcdefghijklmnopqrstuvwxyz'
"""

#====================== EJERCICIOS CONDICIONALES ====================
#==> Ejercicio 1 
"""Dados 2 numeros, desarrolle un programa que determine,
¿qué número es menor?.Desarrolle su programa de dos maneras:
 * En el primero utilice la sentencia if.
 * En el segundo no la utilice."""

#==> Ejercicio 2 
"""Pida al usuario ingresar 3 numeros. Luego determine ¿cuál número 
es el mayor?."""

#==> Ejercicio 3 
"""Desarrolle un programa que calcule el descuento salarial que hace
una empresa a sus empleados, por motivos de pandemia. El programa 
debe devolver el salario recibido por el trabajador y el descuento 
realizado."""

"""Si el empleado gana menos de $ 900.000 se le descuenta el 15%, luego
si devenga hasta $2.500.000 se le descuenta el 20%. Por último si 
gana por encima de este último valor se le descuenta el 25% de su 
salario."""

#==> Ejercicio 4 
"""Los estudiantes del curso de matematicas obtuvieron las siguientes 
calificaciones definitivas (cada una de las notas equivale al 25%):

         Nota1  Nota2  Nota3  Nota4
Camila    1.0    2.3    5.0    5.0
Maria     5.0    3.5    2.5    3.2
José      2.2    4.0    3.2    4.1
Daniela   5.0    0.5    1.0    0.2
Esteban   4.0    5.0    0.0    0.0

El director del grupo preparará una salida académica, en caso de 
que se hayan cumplido las siguientes condiciones:
   * El 60% del grupo debe aprobar la materia
   * Por lo menos dos notas del grupo, deben tener un promedio mayor a 3.0
   * El promedio de los que perdieron la materia debe ser mayor a 2

¿habrá salida académica?"""

#==> Ejercicio 5 
"""Una contraseña de un programa, debe incluir:
       * Alfabeto en mayuscula
       * Alfabeto en minuscula
       * Números
       * Caracteres especiales
       * Por lo menos 8 caracteres en total
Determine si al ingresar una contraseña, esta cumple con todas las 
anteriores condiciones. """


#====================== EJERCICIOS CICLO WHILE ====================
#==> EJERCICIO 1 
"""Desarrolle un ciclo while infinito, con un mensaje que informe, cada vez que el ciclo es repetido."""

#==> EJERCICIO 2 
"""Realice un ciclo while con un numero secreto. Cada vez que se ejecuta un ciclo, el programa pide
adivinar el numero, en caso de no ser acertado se debe mostrar un mensaje diciendo: "Estás atrapado". 
Y en caso contrario terminar el ciclo y avisar que el numero es correcto."""

#==> EJERCICIO 3 
"""Realice un programa, que determine el número mayor para una cantidad indeterminada de numeros. (Utilice el ciclo while)"""

#==> EJERCICIO 4 
"""Realice un programa que lea una secuencia de números, y cuente cuántos números son pares y cuántos son impares. 
El programa termina cuando se ingresa el número cero."""

#==> Ejercicio 5 
"""Utilizando el ciclo while, imprima las siguientes secuencias de numeros:
=> 2,4,5,8,10,11,14,16,17,20 ...598, 599
=> 2,4,8,16,32,64,128, .. 1048576
=> 1,1,2,3,5,8, ... 2178309"""