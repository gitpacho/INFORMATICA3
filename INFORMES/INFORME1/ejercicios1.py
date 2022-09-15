# ----------------------------Ejercicios INFORME 1--------------------------------
"""
Recomendaciones:
 - Recuerde almacenar las respuestas tal como se pide en cada ejercicio
 - Se resuelve de manera individual, la copia será anulada.
 - No hay necesidad de re-escribir las preguntas en su archivo
""" 


#------------------------ EJERCICIO 1 --------------------------------
"""
Dados los siguientes puntos geométricos:
"P1" ==> (2, 2, 3)              "P6"  ==> (1, 0.5, 1)
"P2" ==> (2, 3, 4)              "P7"  ==> (3, 2, 0.5)
"P3" ==> (1, 1, 3)              "P8"  ==> (3, 1, 2)
"P4" ==> (0.5, 0.5, 2)          "P9"  ==> (0, 0, 0)
"P5" ==> (1, 2, 1)              "P10" ==> (2, 0, 0.5) 

Determine el par de puntos que se encuentran más cercanos.
Almacene la respuesta en un string llamado parCercano. Ejemplo:
parCercano = "P1-P9" 
"""

#------------------------ EJERCICIO 2 --------------------------------
"""
Cree las siguientes listas utilizando el ciclo while: 
   lista1 = [1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1]
   lista2 = [100, -1, 99, -1, 98, -1, 97, -1, 96, -1, ... 3, -1, 2, -1, 1, -1]
   lista3 = [2, 4, 5, 6, 8, 10,12, 14,15, 16,18, 20, 22, 24, 25 ... 592, 594, 595 ,596 ,598, 600]

Después de lograr los listados, almacenelos de la siguiente manera:
listaDeListas = [lista1, lista2, lista3]
"""

#------------------------ EJERCICIO 3 --------------------------------
"""
La calificación de informatica se encuentra en el intervalo [0,5] y se calcula tomando 5 notas, 
con porcentajes de 10%, 20%, 15%, 20% y 35%. La materia se aprueba por encima de 3.0

Los siguientes estudiantes tienen las primeras 4 calificaciones definidas.

cod      Nombre          Nota1   Nota2  Nota3  Nota4  Nota 5
01    Miguel Pineda        1.0    1.1    2.3    1.1     ?
02    Maria Gonzalez       3.1    3.1    1.2    3.0     ?
03    Jose Nuñez           5.0    4.0    2.5    5.0     ?
04    Angelica Lozano      3.1    1.0    2.6    1.0     ?
05    Camilo Suarez        3.2    4.0    1.1    3.0     ?
06    Mariana Rosero       5.0    5.0    5.0    3.9     ?
07    Esteban Quesada      3.4    4.0    2.6    3.2     ?
08    Julia Quintero       2.0    2.2    2.1    4.2     ?
09    Mauricio Lizcano     3.7    4.1    4.7    4.0     ?
10    Angie Gomez          4.1    4.7    4.4    5.0     ?
11    Camilo Restrepo      5.0    5.0    1.0    3.2     ?
12    Mauricio Velazquez   5.0    4.2    2.1    5.0     ?
13    Esteban Rodriguez    3.2    4.1    2.2    3.3     ?

   Determine cuantos estudiantes pierden aúnque obtengan la mejor nota5
   Determine cuantos estudiantes ganan aunque obtengan la peor nota5
   Determine cuantos estudiantes tienen posibilidades de pasar

   Almacene sus resultados en una lista llamada estudiantes, tal como se muestra:
   estudiantes = [Cantidad_que_pierden, Cantidad_que_ganan, Cantidad_con_posibilidades]
"""



#------------------------ EJERCICIO 4 --------------------------------
""" Cuatro compañeros, contratan un taxi con el objeto de movilizarse juntos a la universidad. 
El contrato es de lunes a viernes, y deben pagar al taxista $15000 por cada trayecto. 
Se prestarán dos servicios al día, uno de ida y el otro de regreso.

Sin embargo, los cuatro no se movilizan juntos todos los dias. Por tanto, han planteado que la tarifa
debe dividirse entre el numero de compañeros que se movilicen en cada trayecto.En caso, de que ninguno
utilice el servicio. Deben pagar al taxista una tarifa de $10000, repartidos equitativamente entre todos.
A continueación veamos el uso del servicio por parte de los compañeros en la última semana de clases:

                            IDA                             |                       REGRESO
            LUNES   MARTES  MIERCOLES   JUEVES  VIERNES     |    LUNES   MARTES  MIERCOLES   JUEVES  VIERNES
JUAN          Si        Si        Si      Si      No        |      Si        Si        Si      No       No
CAMILA        Si        No        Si      No      Si        |      Si        No        No      No       No
JOSE          Si        No        Si      Si      No        |      Si        No        Si      Si       No
MARIA         Si        Si        Si      No      No        |      No        No        Si      No       No
ESTEBAN       Si        No        No      Si      Si        |      No        No        No      Si       No
ANGIE         Si        No        Si      No      No        |      Si        No        Si      No       No

¿Cuanto debe pagar cada estudiante? 

Almacene el resultado dentro de un diccionario llamado "diccionarioPagos"
las claves deben ser los nombres de los estudiantes (en strings)
y los valores deben ser el dinero total que pagó cada uno al terminar la semana (en flotantes)
"""


#------------------------ EJERCICIO 5 --------------------------------
""" El salario de un empleado de una empresa se calcula, utilizando como base  
$1200000, más un apoyo del 10% en transporte, y uno de 5% por gastos varios.
Además se paga una comisión de acuerdo al numero de ventas de los siguientes productos:
           
            precio_unidad  comisión
* Zapatos:    $ 50 000        5%
* Tenis:      $ 70 000        4%  
* Camisa:     $ 40 000        6%
* Corbata:    $ 25 000        7%
* Pantalon:   $ 35 000        5%
* Blusas:     $ 80 000        3%
* Vestidos:   $ 95 000        2%

 Determine el codigo de los 3 empleados con mayor salario en la empresa
 Almacene los códigos en una lista llamada: codigosAltosSalarios

                |                     UNIDADES VENDIDAS        
CODIGO_EMPLEADO |  zapatos tenis camisas corbatas pantalones blusas vestidos 
     001        |    20      22     30      2        40        20      3    
     002        |    31      14     32      15       13        20      11   
     010        |    24      32     40      9        12        50      13   
     020        |    42      12     33      24       22        32      23   
     021        |    51      21     25      10       19        14      2    
     022        |    22      31     51      21       35        15      11   
     023        |    21      36     22      32       39        32      15   
     024        |    22      33     41      21       43        31      36   
     025        |    33      31     20      42       33        42      35   
     031        |    22      47     5       28       37        31      32   
     032        |    24      38     33      21       41        31      16   
     033        |    21      18     32      37       39        22      12   
     041        |    33      31     21      21       33        39      25   
     042        |    25      39     20      48       15        30      32   
     043        |    27      32     29      28       37        35      16   
     121        |    24      12     31      21       39        32      13   
     122        |    31      31     50      22       13        30      21   
     123        |    23      35     35      39       31        19      19   
     351        |    26      36     39      27       35        32      16   
     352        |    25      31     21      21       25        37      15   
     353        |    23      34     35      32       37        20      49   
     368        |    31      14     29      39       25        37      16   
     369        |    26      31     31      27       37        32      41   
     461        |    40      42     23      11       21        15      19   
     466        |    27      31     39      21       31        32      25   
     469        |    38      32     19      29       35        50      16    
"""