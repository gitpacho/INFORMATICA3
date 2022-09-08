""" En este archivo encontramos ejercicios con los siguientes temas: 

        * Ciclos for
        * Métodos para strings, listas y diccionarios
        * Funciones 

"""

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


#====================== MÉTODOS DE STRINGS ====================

#==> EJERCICIO 1
"A continuación se encuentra el poema el salmon"

"""
TÍTULO: EL SALMÓN
PÁRRAFO 1: DETRÁS DE UN SALMÓN, NADA UN TIBURÓN, LO CAZA EN ALASKA, CANSADOS LOS DOS. 
PÁRRAFO 2: ASUSTADO GRITA: ¡NOOO! POR FAVOR,MI VIDA ES MUY CORTA, ¡MUESTRA COMPASIÓN!.
PÁRRAFO 3: ABRIENDO SU BOCA, LO DEJA ESCAPAR, Y CORRIENTE ARRIBA, LO HA VISTO NADAR.
"""

"""a) Corrija el poema de tal manera que:
      Los indicadores de título y párrafo desaparezcan
      Corregir el uso de mayúsculas y minúsculas según las reglas gramaticales.
      El titulo esté en formato de título.
      Separar los cuatro versos de cada párrafo en renglones sucesivos
      Generar un espacio de renglon entre titulo-parrafo y párrafo-parrafo
      El título debe estar centrado.   
   b) Contar el número de veces que aparece cada vocal
      contar el numero de lineas del poema.
      Reemplazar las palabras: salmón ==> tiburón
                               tiburón ==> salmón
   c) Verificar si el contenido del poemas es: alfabetico
                                               alfanumerico
                                               decimal
                                               digitos
   d) Utilizar la indexación para extraer los elementos ubicados
      en los índices: 0, 10, 100, último índices
   e) Utilizar slicing para extraer los elementos ubicados en:
      - Indices pares.
      - Indices impares.
      - Cada quinto elemento, empezando desde el 20
      - Cada tercer elemento, pero empezando desde el indice 4 y terminando en el 62
      - Desde la mitad hacia adelante
      - Todos pero al revés
      - Cada segundo elemento, pero al revés"""


#====================== EJERCICIOS MÉTODOS DE LISTAS ====================

#==> EJERCICIO 1

""" Realice las siguientes operaciones sobre listas:
        * ["A","B","C"] Elimine el último elemento de la lista
                        Luego agregue su nombre al final de la lista                  

        * [100,200,300] Elimine el segundo elemento de la lista,
                        Luego agregue su edad como segundo elemento de la lista

        * [1,2,3,4]     Elimine el último elemento de la lista
                        Luego agrege los valores 100, 200, 300 al final de la lista
                        Elimine el segundo elemento de la lista
                        Luego inserte el valor -1 en la segunda posición de la lista
        * Contruya una sola lista con los elementos resultantes de las 3 listas anteriores."""

#==> EJERCICIO 2

""" Determine si el numero 25 está en la lista edades,
    y si es así cuantas veces aparece.
    edades = [0,1,2,3,4,5,6,7,8,9,1,0,1,1,1,2,1,3,1,4,1,5,1,6,1,7,1,8,1,9,2,0,2,1,2,2,2,3,2,4,2,5,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] """

#==> EJERCICIO 3
""" Teniendo en cuenta la lista anterior, ordene de forma ascendente,luego descendente a los elementos. 
    Pero sin alterar la lista edades original. """

#==> EJERCICIO 4
""" Cree una copia de edades y haga lo siguiente:
   * Muestre en pantalla el elemento inicial y el final
   * Remueva aquellos elementos cuyo valor es 0 o 1"""
  
#==> EJERCICIO 5
"""  Utilice slicing para extraer a partir de la lista edades:
         - Elementos ubicados en indices pares
         - Elementos ubicados en indices impares
         - Todos los elementos, pero al revés de la lista
         - Cada 70avo elemento a partir del 10
         - Cada 100avo elemento, pero al revés de la lista
         - Cada 35avo elemento, a partir de la mitad
  ¿Qué operaciones puedo hacer con listas que no puede hacer con tuplas? """
  

#====================== EJERCICIOS MÉTODOS DE DICCIONARIOS ====================

#==> EJERCICIO 1
""" Cree el siguiente diccionario =>
    Calificaciones = {"Juan": 5.0, "David": 2.4, "Maria": 2.9, "Esteban": 2.2, "Daniela": 2.0, "Mario": 3.1, "Juanita": 2.1, "José": 3.0, "Sebastian": 2.3, "Cristian": 2.0, "Alberto": 3.9, "Angélica": 4.2, "Angel": 2.0, "Marly": 2.5, "Mariana": 4.5, "Josefina": 2.7}
     
       a) Extraiga los keys y values del diccionario, almacenelos en las variables claves, valores, respectivamente
       b) Corrija en el diccionario las calificaciones de Marly (4.3), Angel (3.1) y Juanita (3.5)
       c) Elimine a les estudiantes Josefina y Juan.
       d) Cree una copia y llamela reprobados, elimine todos aquellos con calificación mayor o igual a 3
       e) Muestre en pantalla la mejor calificación, para ello utilice indexing
       f) Muestre en pantalla la peor calificación, para ello utilice indexing 
       g) Utilice indexing para agregar dos nuevos estudiantes: Marco(3.0) Alejandra(5.0)"""


#==> EJERCICIO 2
""" Utilizando diccionarios cree una base de datos de empleados de una empresa,
la base de datos se debe llamar empleadosMabe. Debe contener la siguiente información

Cod   Nombre               Cargo          Salario   
0001   Cristian Pachon     Ingeniero      $ 3.200.000
0002   Daniela Pineda      Programador    $ 4.300.000
0003   Esteban Murcia      Programador    $ 4.600.000
0004   Jose Guzman         Ingeniero      $ 3.900.000
0005   Camilo Rodriguez    Ensamblador    $ 1.200.000
0006   Mariana Londoño     Ensamblador    $ 1.100.000
0007   Estefania Muños     Ensamblador    $ 1.700.000
0008   Cristian Rodriguez  Ingeniero      $ 3.100.000
0009   Natalia Alzate      Ensamblador    $ 2.200.000
0010   Juan Sanabria       Diseñador      $ 5.100.000
0011   Juanita Calderon    Ensamblador    $ 1.300.000
0012   Laura Quintero      Administrador  $ 2.500.000
0013   Viviana Quesada     Guardia        $ 1.500.000

A partir de la base de datos, busque una manera de:
    a) Encontrar la persona con mayor salario
    b) Encontrar la persona con menor salario
    c) Calcular el gasto total de la empresa por motivo salarios
    d) Calcular el promedio de lo que ganan los programadores
    e) Calcular el promedio de lo que ganan los ensambladores"""


#====================== EJERCICIOS DE FUNCIONES ====================

#==> EJERCICIO 1
"""Desarrolle las siguientes funciones: 

PARAMETRO DE ENTRADA     VALOR DE RETORNO       PROBLEMA
 * edad                     * booleano            * Función que determine si una persona es mayor de edad
 * nombre y salario         * string              * Función que reciba el nombre y salario de trabajador, y luego retorne una cadena con el mensaje: "hola <nombre>, su salario es <salario>"
 * numero                   * entero              * Función que calcule la suma de los digitos de un numero 
 * mensaje                  * booleano            * Función que determine si un mensaje tiene vocales o no
 * numero                   * lista               * Función que devuelva todos los divisores de un numero
 * numero                   * booleano            * Función para determinar si un número es primo
"""

#==> EJERCICIO 2
""" Realice una función que reciba una contraseña y que retorne un string que informe si la contraseña es válida o inválida
    Las condiciones de validez son las siguientes: 
          a) Debe contener Alfabeto en mayuscula
          b) Debe contener Alfabeto en minuscula
          c) Debe contener Números
          d) Debe contener Caracteres especiales
          e) Debe contener Por lo menos 8 caracteres en total"""

#==> EJERCICIO 3
""" Desarrolle una función que calcule el índice da masa 
   corporal de un deportista, como parametro de Entrada
   reciba la altura (m) y peso (Kg). Como salida, devuelva el IMC
   que se calcula como se muestra. IMC (indice de masa corporal) = peso / estatura²

   Si su IMC es mayor a 30. Muestre en pantalla,
   un mensaje advirtiendo sobrepeso"""

#==> EJERCICIO 4
"""Cree una función que retorne el salario de un vendedor de seguros, si este se calcula 
   tomando un salario base de $2000000. Más una comisión por cada seguro, teniendo en cuenta
   que el porcentaje varía teniendo en cuenta la tabla. El precio de cada seguro es de $300000
      
     Seguros [unidades]    comision
      [50-110)               10%
      [110, 200)             20%
      [200, 500)             25%
      [500, infinito]        30%

   Utilice la función para calcular el salario de los siguientes empleados

                 Unidades vendidas
   vendedor1          41
   vendedor2          110
   vendedor3          200
   vendedor4          520
"""

#==> EJERCICIO 5
"""El precio de venta de los artículos de una empresa es el siguiente:
   Codigo      Precio unitario
    A001          $ 31 000
    A011          $ 25 000
    A032          $ 43 000
    A125          $ 55 000
    B001          $ 10 000
    B005          $ 20 000
    P009          $ 30 000
    P019          $ 49 000
    R001          $ 60 000
    W307          $ 90 000
    Z052          $ 35 000
    Z025          $ 27 000
    Z278          $ 65 000

Las ventas a lo largo de un día se ha registrado en la siguiente 
base de datos:
ventas = ["A032-52Unidades", "B001-29Unidades", "A125-15Unidades", "A032-22Unidades", "P009-25Unidades", "B005-20Unidades", "B001-19Unidades", "P009-31Unidades", "B005-22Unidades", "W307-15Unidades", "A011-31Unidades", "P019-18Unidades", "A011-20Unidades", "R001-20Unidades", "P019-19Unidades", "A001-12Unidades", "A125-20Unidades", "R001-31Unidades", "Z052-52Unidades", "W307-31Unidades", "Z025-42Unidades", "Z052-10Unidades", "Z278-30Unidades", "Z025-24Unidades", "Z278-21Unidades", "A001-31unidades"]

Cree una función que reciba la base de datos 
y luego retorne el dinero recaudado a lo largo del día"""

#==> EJERCICIO 6
"""Se tiene el rendimiento académico de los estudiantes
   de un colegio como se muestra:

   Código      Nombre          Algebra Electricidad Optica Organica Cuantica Deportes Artes  
    0001   Natalia Bermudez       3.3       3.2       2.9     3.1      4.0     3.7     3.2
    0002   Jose Rodriguez         5.0       5.0       5.0     5.0      5.0     5.0     5.0    
    0003   Emilio Pineda          4.2       1.0       2.0     3.0      2.9     2.2     1.0
    0004   Camila Quiceno         5.0       3.0       2.9     4.0      3.1     5.0     1.9
    0005   Elisabeth Diaz         2.9       1.1       2.0     2.5      3.1     0.5     2.2
    0006   Andres Pineda          3.9       5.0       1.0     0.2      2.8     5.0     5.0
    0007   Esteban Buitrago       4.1       4.2       4.5     4.8      4.0     4.4     4.2
    0008   Juanita Quintero       3.2       2.3       2.9     2.1      1.9     3.2     3.0
    0009   Estefania Chacón       2.2       1.0       0.8     2.2      2.9     3.1     1.0   
    0010   Daniel Arbelaez        3.1       1.2       0.3     1.9      2.6     5.2     5.0  
    0011   María Martínez         4.2       3.9       5.0     4.5      3.8     2.0     5.0
    0012   Marco Rosero           3.0       2.9       2.5     2.2      3.1     3.5     5.0
    0013   Cristian Quesada       2.5       1.9       2.0     3.0      2.5     1.1     2.9
    0014   Sofia Bueno            2.2       5.0       5.0     3.1      3.2     3.5     0.0
    0015   Laura Tobón            1.1       2.0       2.8     1.2      3.1     2.9     3.1    
    0016   Victor Urrego          3.2       0.0       0.0     0.0      0.0     0.0     0.0
    0017   Juan Quevedo           4.1       4.0       4.2     4.3      3.9     5.0     4.5
    0018   Sebastian Castillo     3.5       3.1       3.2     3.3      4.0     1.9     5.0
    0019   Jose Rubiano           4.1       4.5       5.0     5.0      5.0     5.0     5.0
    0020   Fabio Cardenas         3.2       5.0       5.0     0.0      0.0     0.0     0.0 

    Para resolver este problema primero almacene esta información en un
    elemento de python, ya sea lista,tupla, diccionario, lista de listas, lista de enteros, strigs...,  diccionario de listas...
    o cómo prefiera. Luego realice diferentes funciones para:

    a) Realice una función que reciba un codigo de estudiante, y luego imprima un reporte de todas sus notas y su promedio. 
    b) Realice una función que reciba el nombre de una materia y luego imprima el promedio de dicha materia
    c) Realice una función que devuelva una lista con los nombres de los estudiantes que aprobaron todas sus materias.
    d) Realice una función que devuelva una lista con los nombres de los estudiantes que reprobaron todas sus materias.
    e) Realice una función que reciba un numero de materias ganadas y devuelva una lista con los nombres de los estudiantes que aprobaron esa cantidad de materias
    f) Realice una función que reciba un numero de materias perdidas y devuelva una lista con los nombres de los estudiantes que reprobaron esa cantidad de materias"""