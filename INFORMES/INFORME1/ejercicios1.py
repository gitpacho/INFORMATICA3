# ----------------------------Ejercicios INFORME 1--------------------------------
"""
Recomendaciones:
 - Recuerde almacenar las respuestas tal como se pide en cada ejercicio
 - Se resuelve de manera individual, la copia será anulada.
 - No hay necesidad de re-escribir las preguntas en su archivo
 - Muestre sus procedimientos de manera clara
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
parCercano = "P2-P3" 
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
""" Seis compañeros, contratan un taxi con el objeto de movilizarse juntos a la universidad. 
El contrato es de lunes a viernes, y deben pagar al taxista $15000 por cada trayecto. 
Se prestarán dos servicios al día, uno de ida y el otro de regreso.

Sin embargo, los seis no se movilizan juntos todos los dias. Por tanto, han planteado que la tarifa
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


#Rta

parCercano = "P4-P6"

lista1=[1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]
lista2=[100, -1, 99, -1, 98, -1, 97, -1, 96, -1, 95, -1, 94, -1, 93, -1, 92, -1, 91, -1, 90, -1, 89, -1, 88, -1, 87, -1, 86, -1, 85, -1, 84, -1, 83, -1, 82, -1, 81, -1, 80, -1, 79, -1, 78, -1, 77, -1, 76, -1, 75, -1, 74, -1, 73, -1, 72, -1, 71, -1, 70, -1, 69, -1, 68, -1, 67, -1, 66, -1, 65, -1, 64, -1, 63, -1, 62, -1, 61, -1, 60, -1, 59, -1, 58, -1, 57, -1, 56, -1, 55, -1, 54, -1, 53, -1, 52, -1, 51, -1, 50, -1, 49, -1, 48, -1, 47, -1, 46, -1, 45, -1, 44, -1, 43, -1, 42, -1, 41, -1, 40, -1, 39, -1, 38, -1, 37, -1, 36, -1, 35, -1, 34, -1, 33, -1, 32, -1, 31, -1, 30, -1, 29, -1, 28, -1, 27, -1, 26, -1, 25, -1, 24, -1, 23, -1, 22, -1, 21, -1, 20, -1, 19, -1, 18, -1, 17, -1, 16, -1, 15, -1, 14, -1, 13, -1, 12, -1, 11, -1, 10, -1, 9, -1, 8, -1, 7, -1, 6, -1, 5, -1, 4, -1, 3, -1, 2, -1, 1, -1]
lista3=[2, 4, 5, 6, 8, 10, 12, 14, 15, 16, 18, 20, 22, 24, 25, 26, 28, 30, 32, 34, 35, 36, 38, 40, 42, 44, 45, 46, 48, 50, 52, 54, 55, 56, 58, 60, 62, 64, 65, 66, 68, 70, 72, 74, 75, 76, 78, 80, 82, 84, 85, 86, 88, 90, 92, 94, 95, 96, 98, 100, 102, 104, 105, 106, 108, 110, 112, 114, 115, 116, 118, 120, 122, 124, 125, 126, 128, 130, 132, 134, 135, 136, 138, 140, 142, 144, 145, 146, 148, 150, 152, 154, 155, 156, 158, 160, 162, 164, 165, 166, 168, 170, 172, 174, 175, 176, 178, 180, 182, 184, 185, 186, 188, 190, 192, 194, 195, 196, 198, 200, 202, 204, 205, 206, 208, 210, 212, 214, 215, 216, 218, 220, 222, 224, 225, 226, 228, 230, 232, 234, 235, 236, 238, 240, 242, 244, 245, 246, 248, 250, 252, 254, 255, 256, 258, 260, 262, 264, 265, 266, 268, 270, 272, 274, 275, 276, 278, 280, 282, 284, 285, 286, 288, 290, 292, 294, 295, 296, 298, 300, 302, 304, 305, 306, 308, 310, 312, 314, 315, 316, 318, 320, 322, 324, 325, 326, 328, 330, 332, 334, 335, 336, 338, 340, 342, 344, 345, 346, 348, 350, 352, 354, 355, 356, 358, 360, 362, 364, 365, 366, 368, 370, 372, 374, 375, 376, 378, 380, 382, 384, 385, 386, 388, 390, 392, 394, 395, 396, 398, 400, 402, 404, 405, 406, 408, 410, 412, 414, 415, 416, 418, 420, 422, 424, 425, 426, 428, 430, 432, 434, 435, 436, 438, 440, 442, 444, 445, 446, 448, 450, 452, 454, 455, 456, 458, 460, 462, 464, 465, 466, 468, 470, 472, 474, 475, 476, 478, 480, 482, 484, 485, 486, 488, 490, 492, 494, 495, 496, 498, 500, 502, 504, 505, 506, 508, 510, 512, 514, 515, 516, 518, 520, 522, 524, 525, 526, 528, 530, 532, 534, 535, 536, 538, 540, 542, 544, 545, 546, 548, 550, 552, 554, 555, 556, 558, 560, 562, 564, 565, 566, 568, 570, 572, 574, 575, 576, 578, 580, 582, 584, 585, 586, 588, 590, 592, 594, 595, 596, 598, 600]
listaDeListas = [lista1, lista2, lista3]

Cantidad_que_pierden = 2
Cantidad_que_ganan = 2
Cantidad_con_posibilidades = 9

estudiantes = [Cantidad_que_pierden, Cantidad_que_ganan, Cantidad_con_posibilidades]  

diccionarioPagos = {'JUAN': 42166.666666666664, 'CAMILA': 18416.666666666668, 'JOSE': 27166.666666666668, 'MARIA': 18416.666666666668, 'ESTEBAN': 24166.666666666668, 'ANGIE': 14666.666666666666} 
codigosAltosSalarios = ['025', '024', '353']