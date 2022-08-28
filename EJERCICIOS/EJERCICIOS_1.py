"""
En este archivo encontramos ejercicios para introducirnos en el lenguaje, 
ejercicios introductorios para uso de variables y ejercicios con operadores.
"""

#====================== EJERCICIOS INTRODUCTORIOS ====================
#==>  EJERCICIO 1 
""" Dada una cantidad de segundos, realice un algoritmo que los convierta a unidades horas,minutos
mostrando en pantalla en formato "horas:minutos"  """

#==>  EJERCICIO 2 
""" ¿Qué radio debe tener una esfera, para que su volumen sea el mismo al de un cubo de lado 5 cm? """

#==>  EJERCICIO 3 
""" ¿Cuantas veces supera, el area de un cubo, al area de una esfera, si el lado del
cubo es 10 cm. Y el radio de la esfera 2 cm ? """

#==>  EJERCICIO 4 
""" Realice un código, que permita la conversión de millas a km y km a millas """

#==>  EJERCICIO 5 
""" Dadas las coordenadas P1(5,4,5) y P2(0,10,9).
Realice un codigo que determine la distancia entre ambos puntos """

#==>  EJERCICIO 6 
""" La calificación de informatica se encuentra en el intervalo [0,5] y se calcula tomando 4 notas, 
con porcentajes de 15%, 25%, 20% y 40%. Si un estudiante tiene las primeras 3 calificaciones definidas.
Realice un algoritmo que calcule la nota necesaria de la última nota para pasar la materia. """

#==>  EJERCICIO 7 
""" La calificación de informatica se encuentra en el intervalo [0,5] y se calcula tomando 4 notas,
 con porcentajes de 15%, 25%, 20% y 40%. Si un estudiante tiene las primeras 2 calificaciones definidas.
Realice un algoritmo que calcule la nota necesaria de las dos últimas notas para pasar la materia. """

#==>  EJERCICIO 8 
""" Cuatro compañeros, contratan un taxi con el objeto de movilizarse juntos a la universidad. 
El contrato es de lunes a viernes, y deben pagar al taxista $15000 por cada trayecto. El servicio se
prestará solo de ida.

Sin embargo, los cuatro no se movilizan juntos todos los dias. Por tanto, han planteado que la tarifa
debe dividirse entre el numero de compañeros que se movilicen en cada trayecto.En caso, de que ninguno
utilice el servicio. Deben pagar al taxista una tarifa de $10000, repartidos equitativamente entre los cuatro.
A continueación veamos el uso del servicio por parte de los compañeros en la última semana de clases:

            LUNES   MARTES  MIERCOLES   JUEVES  VIERNES
JUAN          Si        Si        No        Si    No
CAMILA        Si        Si        No        No    No
JOSE          Si        No        Si        No    No
MARIA         Si        Si        Si        No    No      

¿Cuanto debe pagar cada estudiante? """

#==>  EJERCICIO 9 
""" El salario mensual de un empleado se calcula teniendo en cuenta el numero de seguros vendidos,
    en donde el precio de cada seguro es de $120000. 
    Para los primeros 20 seguros, la comisión es del 20%.
    Para los siguientes 100 seguros las comisión es del 30%.
    Para los siguientes seguros vendidos. La comisión es de 10%.

    a) Si un empleado vende 435 seguros, ¿cual será su salario?
    b) Para un salario de $10'000.000. ¿Cuántos seguros debe vender?
    c) Si un empleado devenga $15'000.000. ¿Cuantos salarios vendió en promedio al dia? 
       Teniendo en cuenta que solo trabajaba de lunes a jueves """

#==>  EJERCICIO 10 
""" El salario de un empleado de una empresa se calcula, utilizando como base el 
salario minimo, más un apoyo del 10% en transporte, y uno de 5% por gastos varios.
Además se paga una comisión de acuerdo al numero de ventas de los siguientes productos:
           
            precio_unidad  comisión
* Zapatos:    $ 50 000        5%
* Tenis:      $ 70 000        4%  
* Camizas:    $ 40 000        6%
* Corbatas:   $ 25 000        7%
* Pantalon:   $ 35 000        5%
* Blusas:     $ 80 000        3%
* Vestidos:   $ 95 000        2%
* Medias:     $ 10 000        8%

a) Realice un algoritmo que calcule el salario del empleado teniendo en cuenta el numero de ventas realizadas 
b) Uno de los directivos, quiere que la comisión de cada uno de los productos no supere los $2000
   ¿Qué productos deben cambiar en su porcentaje de comision?
c) Otro directivo desea que la comisión de cada producto se fije en $1900, 
   ¿en cuanto se deben fijar las comisiones de los productos"""

#==>  EJERCICIO 11 
""" Un auto acelera de manera uniforme 0.5 km/s², 
a) ¿cuantas horas deben pasar para alcanzar la velocidad de la luz?
b) ¿qué distancia se habrá recorrido? (suponga que es posible alcanzar la velocidad de la luz) """

#==>  EJERCICIO 12 
""" Un proyectil es lanzado verticalmente hacia arriba, calcule la velocidad inicial que debe tener para 
alcanzar una altura dada. """

#==>  EJERCICIO 13 
""" Un proyectil es lanzado siguiendo una trayectoria parabólica, calcule el ángulo y la velocidad inicial
que debe tener para alcanzar una distancia horizontal y vertical dada. """

#==>  EJERCICIO 14 
""" Un atleta inicia su entrenamiento, desde el punto de partida de una pista, a una velocidad constante de 3m/s. 
Diez segundos después otro atleta empieza su recorrido a una velocidad constante de 5m/s. ¿Cuánto tiempo 
habrá pasado para que el segundo atleta alcance al primero? """

#==>  EJERCICIO 15 
""" Dos automoviles realizan una carrera. El primero de ellos acelera a razón constante de 3m/s², el segundo 
a razón de 5m/s². Si el segundo de ellos empieza su recorrido 10 segundos después que el primero ha empezado.
¿Cuanto tiempo habrá transcurrido cuando ambos se encuentran? """

#====================== EJERCICIOS OPERADORES ====================
#==> Ejercicio 1 
""" Realice las siguientes operaciones mentalmente. Intente determinar la respuesta, luego verifique en python

   1 + 3 - 5      "cristian" + "Unal"     [1,2,3] + [4,5,6]    True and False          5 > 3          1 in [1,2,3]
   13 / 2         "Unal" * 5              [1,2] * 4            1 and 2                 2 != 2            "A" in ("A", "B", "C")   
   19 // 6                                (1,2,3) + (4,5,6)    5 and True              3 == "3"          1 not in ["A", "B", "C"]    
   31 % 3                                 (1,2) * 4            False and 5             5 > True          "A" in {"A", "B", "C"} 
   2 ** 5                                                      [] and "resultado"      True < 0
   16 ** 0.5                                                   True and (2,3,4)        True != False
                                                               False or True           "abc" < "bcd"
                                                               0 or 5
                                                               True or 5
                                                               "resultado" or False
   """

#==> EJERCICIO 2 
""" ¿Qué operaciones puede realizar con los anteriores operadores?
¿Qué tipos de datos se pueden utilizar con cada uno de los operadores? """

#==> EJERCICIO 3 
""" De los operadores *, /, +. ¿Cual tiene mayor prioridad?
=> 3 / 2 * 5  compare con 3 * 2 / 5
=> 3 / 2 + 5  compare con 3 + 2 / 5
=> 3 * 2 + 5  compare con 3 + 2 * 5  """

#==> EJERCICIO 4 
""" De los operadores *, **. ¿Cual tiene mayor prioridad?
=> 3 * 2 ** 5  compare con 3 ** 2 * 5
=> 2 * 2 ** 3  compare con 2 ** 2 * 3
=> 2 ** 2 ** 3 ¿Qué sucede en este caso? """

#==> EJERCICIO 5 
""" De los operadores *, /, //, % ¿cual tiene mayor prioridad?:
=> 13 // 6 * 2 compare con 27 // 6 * 2
=> 13 / 6 // 2 compare con 13 // 6 / 2
=> 13 * 6 % 2 compare con 13 % 6 * 2 """

#==> EJERCICIO 6 
""" Realice las siguientes operaciones, y determine:
¿Cuál es el orden de prioridades de los operadores not, and, or?
=> not True and False
=> True and not False
=> True and False or False
=> True or False and False """

#==> EJERCICIO 7
""" Intente determinar mentalmente la salida de las siguientes operaciones
 1 and 2 and 3     1 or 2 or 3
 1 and 0 and 3     1 or 0 or 3
 0 and 2 and 3     0 or 1 or 2
 """