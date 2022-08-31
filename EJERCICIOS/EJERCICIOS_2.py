"""
En este archivo encontramos ejercicios con los siguientes temas: 
funciones integradas de python, uso de condicionales y ciclos while y for
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



#====================== EJERCICIOS CICLO FOR ====================

#==> EJERCICIO 1 
""" Utilice el ciclo for para recorrer los siguientes iterables, luego imprimalos:
     a) Posiciones = range(10) ,      
     b) Edades = range(10,30,2)
     c) Tamaños = range(1,11, 3)
     d) letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
     e) Estudiantes = ["Cristian", "José", "María", "Juanita", "Marly"]
     f) Calificaciones = (5, 5, 5, 2, 4) """

#==> EJERCICIO 2 
""" Imprimir los siguientes numeros (utilice el iterable que más le convenga):
     a) 2, 3, 4, 5, 6, 7, 8, 9, 10
     b) 3, 6, 9, 12, ... 300
     c) 5, -5, 20, 25, 100, 0, -1, 21, 32, 57, 26
     d) 1, -1, 1, -1, 1, -1, 1, 
     e) "Z", "Y", "X", "W" , ... "B", "A"
     f) "A", 1, "B", 2, "C", 3 """

#==> EJERCICIO 3
""" Realice los siguientes programas:
      a) Programa que calcule los primeros 100 terminos de la serie de fibonacci
      b) Programa que determine todos los divisores de un numero n
      c) Programa que determine si un número n es primo
      d) Programa que sume los digitos de un numero cualquiera. Ejemplo: numero=> 8791, rta=> 25 
      e) Programa que sume los digitos pares de un numero cualquiera """

#==> EJERCICIO 4 
""" El rendimiento de los empleados de una empresa es el siguiente:

--------------  Emplea_1  Emplea_2  Emplea_3  Emplea_4  Emplea_5  Emplea_6  Emplea_7  Emplea_8  Emplea_9  Emplea_10  Emplea_11  Emplea_12  Emplea_13  Emplea_14  Emplea_15  Emplea_16  Emplea_17  Emplea_18  Emplea_19  Emplea_20  Emplea_21  Emplea_22  Emplea_23  Emplea_24  Emplea_25  Emplea_26  Emplea_27 
Rendimiento --    "C"       "B"      "B"        "B"        "C"      "B"      "A"        "C"       "B"        "A"        "C"       "B"        "B"        "B"         "B"        "A"       "B"        "A"         "A"        "C"       "B"        "B"        "B"         "B"         "C"       "A" 

Donde "A" es alto, "B" aceptable  y "C"  insuficiente. 
Determine ¿cuales empleados pueden solicitar un aumento salarial y cuáles pueden ser despedidos? """

#==> EJERCICIO 5 
""" El rendimiento deportivo de un grupo de atletas es el siguiente:

-------------- Deportista_1  Deportista_2  Deportista_3  Deportista_4  Deportista_5  Deportista_6  Deportista_7  Deportista_8  Deportista_9  Deportista_10  Deportista_11  Deportista_12  Deportista_13  Deportista_14  Deportista_15  Deportista_16  Deportista_17  Deportista_18  Deportista_19  Deportista_20  Deportista_21  Deportista_22  Deportista_23  Deportista_24  Deportista_25  Deportista_26  Deportista_27 
Rendimiento --    "A"           "B"           "C"            "B"            "B"           "B"          "C"           "B"             "A"           "C"          "B"          "A"             "C"             "B"          "B"              "B"           "B"             "A"           "B"            "A"           "A"             "C"             "B"             "B"          "B"            "B"            "C"             
Edad ---------     42            60            18             20             35            25           60            30              19            42           21           17              39              30           28               34            27              23            23             20            25             "40"             31             32            45             26             17             

Donde "A" es alto, "B" aceptable  y "C"  insuficiente. Determine:
  => ¿Cuántos atletas tienen un rendimiento alto, aceptable e insuficiente?
  => ¿Cuántos atletas mayores de 40 años, tienen rendimiento alto?
  => ¿Cuantos atletas menores de 25, tienen un rendimiento insuficiente?
  => ¿Cuales deportistas entre 30 y 40 años tienen rendimiento aceptable?
  => ¿Cuales deportistas menores de 30 tienen rendimiento alto
  => ¿Cuales deportistas mayores de 35 tienen rendimiento insuficiente?
(Intente utilizar un solo ciclo para resolver las preguntas) """

#==> EJERCICIO 6 
""" El costo de las entradas a cine es el siguiente:
                          ----------- 2D ------------        ---------- 3D -------------      
                          ----NIÑO----  ----ADULTO---        ---NIÑO----  ----ADULTO----
 precio (Lunes a viernes)     $5000          $8000              $8000         $12000
 precio (Sabado, domingo)     $7000          $9000              $9000         $15000

Cada una de las ventas de boletas en una semana, se registraron de la siguiente manera:
("3D_3NIÑOS_MARTES", "3D_2ADULTOS_MARTES")
("2D_3NIÑOS_MARTES", "2D_1ADULTOS_MARTES")
("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES")
("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES")
("3D_0NIÑOS_MARTES", "3D_1ADULTOS_MARTES")
("2D_2NIÑOS_MARTES", "2D_1ADULTOS_MARTES")
("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES")
("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES")
("3D_0NIÑOS_MARTES", "3D_3ADULTOS_MARTES")
("3D_3NIÑOS_MARTES", "3D_4ADULTOS_MARTES")
("2D_2NIÑOS_MARTES", "2D_4ADULTOS_MARTES")
("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES")
("3D_1NIÑOS_MARTES", "3D_1ADULTOS_MARTES")
("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES")
("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES")
("2D_1NIÑOS_MIERCOLES", "2D_1ADULTOS_MIERCOLES")
("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES")
("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES")
("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES")
("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES")
("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES")
("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES")
("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES")
("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES")
("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES")
("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES")
("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES")
("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES")
("2D_1NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES")
("2D_2NIÑOS_VIERNES", "2D_1ADULTOS_VIERNES")
("3D_1NIÑOS_VIERNES", "3D_1ADULTOS_VIERNES")
("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES")
("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES")
("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES")
("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES")
("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES")
("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES")
("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO")
("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO")
("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO")
("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO")
("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO")
("2D_1NIÑOS_SABADO", "2D_4ADULTOS_SABADO")
("2D_1NIÑOS_SABADO", "2D_4ADULTOS_SABADO")
("3D_1NIÑOS_SABADO", "3D_1ADULTOS_SABADO")
("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO")
("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO")
("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO")
("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO")
("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO")
("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO")
("2D_1NIÑOS_DOMINGO", "2D_3ADULTOS_DOMINGO")
("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO")

    a) Determine el numero de boletas vendidas para niños, entre semana.
    b) Determine las ventas (dinero) de adultos que fueron los fines de semana a 3D.
    c) Determine el numero de boletas vendidas totales.
    d) Determine las ventas (dinero) totales. """