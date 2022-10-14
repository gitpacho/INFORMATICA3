nombre_compleo = ""   #Por favor ingrese su nombre COMPLETO en la cadena

# ----------------------------Ejercicios INFORME 2--------------------------------
"""
Recomendaciones:
 - Recuerde almacenar las respuestas tal como se pide en cada ejercicio
 - Se resuelve de manera individual, la copia será anulada.
 - No hay necesidad de escribir las preguntas en su archivo ejercicios2.py
 - Muestre sus procedimientos de manera clara
"""

# ------------------------ EJERCICIO 1 --------------------------------
"""El precio de venta de los artículos de una empresa es el siguiente:

       Producto            Precio unitario
         A001                 $ 31 000
         A011                 $ 25 000
         A032                 $ 43 000
         A125                 $ 55 000
         B001                 $ 10 000
         B005                 $ 20 000
         P009                 $ 30 000
         P019                 $ 49 000
         R001                 $ 60 000
         W307                 $ 90 000
         Z052                 $ 35 000
         Z025                 $ 27 000
         Z278                 $ 65 000

Las ventas a lo largo de un día se ha registrado en la siguiente lista:

ventas = ["A032-52Unidades", "B001-29Unidades", "A125-15Unidades", "A032-22Unidades", "P009-25Unidades", "B005-20Unidades", "B001-19Unidades", "P009-31Unidades", "B005-22Unidades", "W307-15Unidades", "A011-31Unidades", "P019-18Unidades", "A011-20Unidades", "R001-20Unidades", "P019-19Unidades", "A001-12Unidades", "A125-20Unidades", "R001-31Unidades", "Z052-52Unidades", "W307-31Unidades", "Z025-42Unidades", "Z052-10Unidades", "Z278-30Unidades", "Z025-24Unidades", "Z278-21Unidades", "A001-31unidades","A032-32Unidades","B001-22Unidades","A125-11Unidades","A032-12Unidades","P009-19Unidades","B005-11Unidades","B001-19Unidades","P009-21Unidades","B005-22Unidades","W307-15Unidades","A011-31Unidades","P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-12Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","Z278-30Unidades","Z025-24Unidades","Z278-11Unidades","A001-91unidades"]

Determine:
    a) Unidades vendidas de cada producto, almacene la respuesta en un diccionario llamado  unidadesPorProducto, cuyas claves sean los productos, y cuyos valores sean el numero de unidades vendidas por producto
    b) Dinero recaudado por cada producto, almacene la respuesta en un diccionario  llamado ventasPorProducto, cuyas claves sean los productos, y cuyos valores sean el dinero recaudado por producto
    c) Dinero total recaudado, almacene la respuesta en una variable llamada  ventasTotal, con el dinero total recaudado

Presente la respuesta en una lista llamada reporteVentas de la siguiente manera:
    reporteVentas = [unidadesPorProducto, ventasPorProducto, ventasTotal]
"""

# ------------------------ EJERCICIO 2 --------------------------------
"""
El diccionario calificaciones posee información de las calificaciones de un grupo de estudiantes,
Contiene el codigo del estudiante, su Nombre, y sus notas(Fisica, Ingles, Deportes, Artes, Musica)

calificaciones = {
                      "001": {"Nombre": "Cristian Pachon",      "Fisica":  2.0,   "Ingles": 2.2,   "Deportes": 4.2,   "Artes": 4.0,  "Musica": 0.5},
                      "002": {"Nombre": "Daniela Pineda",       "Fisica":  2.2,   "Ingles": 1.0,   "Deportes": 4.0,   "Artes": 3.1,  "Musica": 4.0},
                      "003": {"Nombre": "Esteban Murcia",       "Fisica":  2.9,   "Ingles": 4.2,   "Deportes": 3.1,   "Artes": 0.0,  "Musica": 3.1},
                      "004": {"Nombre": "Jose Guzman",          "Fisica":  2.0,   "Ingles": 4.0,   "Deportes": 4.0,   "Artes": 0.2,  "Musica": 0.0},
                      "005": {"Nombre": "Camilo Rodriguez",     "Fisica":  2.2,   "Ingles": 0.2,   "Deportes": 0.2,   "Artes": 1.0,  "Musica": 0.2},
                      "006": {"Nombre": "Mariana Londoño",      "Fisica":  2.0,   "Ingles": 5.0,   "Deportes": 1.0,   "Artes": 1.3,  "Musica": 1.0},
                      "007": {"Nombre": "Estefania Muños",      "Fisica":  5.0,   "Ingles": 1.2,   "Deportes": 1.2,   "Artes": 1.9,  "Musica": 1.3},
                      "008": {"Nombre": "Cristian Rodriguez",   "Fisica":  0.2,   "Ingles": 2.9,   "Deportes": 1.0,   "Artes": 4.2,  "Musica": 1.9},
                      "009": {"Nombre": "Natalia Alzate",       "Fisica":  5.0,   "Ingles": 2.3,   "Deportes": 2.9,   "Artes": 2.9,  "Musica": 0.2},
                      "010": {"Nombre": "Juan Sanabria",        "Fisica":  4.2,   "Ingles": 5.0,   "Deportes": 4.2,   "Artes": 4.2,  "Musica": 3.9},
                      "011": {"Nombre": "Juanita Calderon",     "Fisica":  4.5,   "Ingles": 4.2,   "Deportes": 4.0,   "Artes": 0.5,  "Musica": 4.2},
                      "012": {"Nombre": "Laura Quintero",       "Fisica":  4.2,   "Ingles": 4.5,   "Deportes": 4.2,   "Artes": 0.0,  "Musica": 0.5},
                      "013": {"Nombre": "Viviana Quesada",      "Fisica":  0.5,   "Ingles": 0.5,   "Deportes": 2.3,   "Artes": 4.2,  "Musica": 0.0},
                      "014": {"Nombre": "Camila Alzate",        "Fisica":  4.1,   "Ingles": 3.1,   "Deportes": 2.5,   "Artes": 4.3,  "Musica": 3.2},
                      "015": {"Nombre": "Leonidas Sanabria",    "Fisica":  4.2,   "Ingles": 4.2,   "Deportes": 4.2,   "Artes": 2.5,  "Musica": 4.3},
                      "016": {"Nombre": "Juana Diaz",           "Fisica":  4.1,   "Ingles": 0.0,   "Deportes": 4.5,   "Artes": 4.2,  "Musica": 2.5},
                      "017": {"Nombre": "Laura Playonero",      "Fisica":  1.2,   "Ingles": 3.1,   "Deportes": 0.5,   "Artes": 4.5,  "Musica": 3.2},
                      "018": {"Nombre": "Viviana Restrepo",     "Fisica":  0.5,   "Ingles": 0.2,   "Deportes": 4.1,   "Artes": 4.1,  "Musica": 4.5},
                      "019": {"Nombre": "Elias Rodriguez",      "Fisica":  2.2,   "Ingles": 0.5,   "Deportes": 0.2,   "Artes": 0.2,  "Musica": 4.1},
                      "020": {"Nombre": "Mariana Pacheco",      "Fisica":  2.0,   "Ingles": 2.2,   "Deportes": 4.0,   "Artes": 4.2,  "Musica": 0.5},
                      "021": {"Nombre": "Estefany Muñoz",       "Fisica":  2.2,   "Ingles": 1.0,   "Deportes": 3.1,   "Artes": 4.0,  "Musica": 4.0},
                      "022": {"Nombre": "Cristian Fernandez",   "Fisica":  2.9,   "Ingles": 4.2,   "Deportes": 0.0,   "Artes": 3.1,  "Musica": 3.1},
                      "023": {"Nombre": "Jessika Arias",        "Fisica":  2.0,   "Ingles": 4.0,   "Deportes": 4.0,   "Artes": 0.0,  "Musica": 0.2},
                      "024": {"Nombre": "Juan Mendoza",         "Fisica":  4.5,   "Ingles": 4.2,   "Deportes": 4.0,   "Artes": 4.2,  "Musica": 0.5},
                      "025": {"Nombre": "Maria Calderon",       "Fisica":  2.2,   "Ingles": 0.2,   "Deportes": 0.2,   "Artes": 0.2,  "Musica": 1.0},
                      "026": {"Nombre": "Laura Lozada",         "Fisica":  2.0,   "Ingles": 5.0,   "Deportes": 1.0,   "Artes": 1.0,  "Musica": 1.3},
                      "027": {"Nombre": "Yessica Quesada",      "Fisica":  1.2,   "Ingles": 5.0,   "Deportes": 1.9,   "Artes": 1.2,  "Musica": 1.3},
                      "028": {"Nombre": "Jennifer Alzate",      "Fisica":  2.9,   "Ingles": 0.2,   "Deportes": 4.2,   "Artes": 1.0,  "Musica": 1.9},
                      "029": {"Nombre": "Karen Sanabria",       "Fisica":  0.0,   "Ingles": 4.1,   "Deportes": 4.2,   "Artes": 4.5,  "Musica": 2.5},
                      "030": {"Nombre": "Fernando Rodriguez",   "Fisica":  0.5,   "Ingles": 2.2,   "Deportes": 0.2,   "Artes": 0.2,  "Musica": 4.1},
                      "031": {"Nombre": "Nina Londoño",         "Fisica":  4.2,   "Ingles": 4.2,   "Deportes": 2.5,   "Artes": 4.2,  "Musica": 4.3},
                      "032": {"Nombre": "Favio Munera",         "Fisica":  5.0,   "Ingles": 2.3,   "Deportes": 2.9,   "Artes": 2.9,  "Musica": 0.2},
                      "033": {"Nombre": "Lindsey Roy",          "Fisica":  4.2,   "Ingles": 5.0,   "Deportes": 4.2,   "Artes": 4.2,  "Musica": 3.9},
                      "034": {"Nombre": "Nathalia Hernandez",   "Fisica":  4.2,   "Ingles": 4.5,   "Deportes": 0.0,   "Artes": 4.2,  "Musica": 0.5},
                      "035": {"Nombre": "Juan Gaviria",         "Fisica":  0.5,   "Ingles": 0.5,   "Deportes": 4.2,   "Artes": 2.3,  "Musica": 0.0},
                      "036": {"Nombre": "Fabio Urrego",         "Fisica":  4.1,   "Ingles": 3.1,   "Deportes": 4.3,   "Artes": 2.5,  "Musica": 3.2},
                      "037": {"Nombre": "Fernanda Quintero",    "Fisica":  0.5,   "Ingles": 0.2,   "Deportes": 4.1,   "Artes": 4.1,  "Musica": 4.5},
                      "038": {"Nombre": "Camila Queiroz",       "Fisica":  1.2,   "Ingles": 3.1,   "Deportes": 4.5,   "Artes": 0.5,  "Musica": 3.2},
                      "039": {"Nombre": "Ursula Alzate",        "Fisica":  2.2,   "Ingles": 4.0,   "Deportes": 4.2,   "Artes": 0.5,  "Musica": 2.0},
                      "040": {"Nombre": "Aureliano Buendia",    "Fisica":  1.0,   "Ingles": 3.1,   "Deportes": 4.0,   "Artes": 4.0,  "Musica": 2.2},
                }

    Utilice diccionario estudiantes, para determinar:

    a) El promedio obtenido por cada estudiante, almacene la respuesta en un diccionario llamado promediosPorEstudiante, cuyas claves son los nombres de los estudiantes y los valores sus respectivos promedios (flotantes de 2 decimales)
    b) El promedio obtenido por cada materia, almacene la respuesta en un diccionario llamado promediosPorMateria, cuyas claves son los nombres de las materias y los valores sus respectivos promedios
    c) Estudiantes con promedio mayor o igual a 3, almacene la respuesta en una lista llamada estudiantesAprobados, que contenga los nombres de los estudiantes que aprueban
    d) Estudiantes con promedio menor a 3, almacene la respuesta en una lista llamada estudiantesReprobados, que contenga los nombres de los estudiantes que reprueban

    Presente la respuesta en una lista de la siguiente manera:
        reporteEstudiantes = [promediosPorEstudiante, promediosPorMateria, estudiantesAprobados, estudiantesReprobados]
"""

# ------------------------ EJERCICIO 3 --------------------------------
""" El costo de las entradas a cine es el siguiente:

                          ----------- 2D ------------        ---------- 3D -------------
                          ----NIÑO----  ----ADULTO---        ---NIÑO----  ----ADULTO----
 precio (Lunes a viernes)     $5000          $8000              $8000         $12000
 precio (Sabado, domingo)     $7000          $9000              $9000         $15000

Cada una de las ventas de boletas en una semana, se registraron de la siguiente manera:

[
   ("2D_3NIÑOS_LUNES", "2D_1ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),("3D_0NIÑOS_LUNES", "3D_1ADULTOS_LUNES"),("2D_2NIÑOS_LUNES", "2D_1ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),("3D_0NIÑOS_LUNES", "3D_3ADULTOS_LUNES"),("3D_3NIÑOS_LUNES", "3D_4ADULTOS_LUNES"),("2D_2NIÑOS_LUNES", "2D_4ADULTOS_LUNES"),("2D_1NIÑOS_MARTES",
    "2D_4ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_2ADULTOS_MARTES"),("2D_3NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_3ADULTOS_MARTES"),
   ("3D_3NIÑOS_MARTES", "3D_4ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_1NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_2ADULTOS_MARTES"),("2D_3NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),(
       "2D_2NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_3ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_4ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_1NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_2ADULTOS_MARTES"),
   ("2D_3NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_3ADULTOS_MARTES"), ("3D_3NIÑOS_MARTES", "3D_4ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),(
       "2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_1NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("2D_1NIÑOS_MIERCOLES", "2D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),
   ("2D_1NIÑOS_MIERCOLES", "2D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("2D_1NIÑOS_MIERCOLES",
    "2D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("2D_1NIÑOS_MIERCOLES", "2D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),
   ("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),(
       "2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),
   ("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_0ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),(
       "2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),
   ("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_0ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),(
       "2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),
   ("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_0ADULTOS_JUEVES"),("2D_2NIÑOS_VIERNES", "2D_1ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES", "3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES",
    "2D_2ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_1ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES", "3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),
   ("2D_2NIÑOS_VIERNES", "2D_0ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES", "3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_1ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES",
    "3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_0ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),
   ("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_0ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),(
       "3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_4ADULTOS_SABADO"),("3D_1NIÑOS_SABADO", "3D_1ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),
   ("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),(
       "2D_1NIÑOS_SABADO", "2D_0ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),
   ("2D_1NIÑOS_SABADO", "2D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO",
    "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_DOMINGO", "2D_0ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"), ("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),
   ("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO",
    "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_0ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),
   ("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO",
    "2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),
   ("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO",
    "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_0ADULTOS_DOMINGO"),
   ("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO",
    "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),
   ("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO",
    "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_0ADULTOS_DOMINGO"),
   ("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO",
    "2D_4ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_9ADULTOS_DOMINGO")
]

Calcule el numero de boletas vendidas (boletasVendidas) y el dinero recaudado por el cine (dineroRecaudado)

Presente la respuesta de la siguiente manera:
    reporteCine = [boletasVendidas, dineroRecaudado]
"""

# ------------------------ EJERCICIO 4 --------------------------------

"""Desarrolle las siguientes funciones:

NOMBRE DE LA FUNCION     PROBLEMA                                                    TIPO DE ENTRADA            RETORNO                                  NOTA
obtenerMultiplos        * Funcion que retorne los primeros 10 multiplos de un numero  * Entero (un numero)     * Lista con los multiplos                 *El cero no se tendrá en cuenta como un múltiplo
obtenerDivisores        * Función que retorne los divisores de un numero              * Entero (un numero)     * Lista con los divisores                 *El numero 1, ni el mismo numero de entrada, se considerarán divisores
obtenerNesimoFibonacci  * Función que retorne el n-esimo numero fibonacci             * Entero (un numero)     * Entero (numero fibonacci)               *El primer numero de la serie es 0, el segundo es el 1

Almacene su respuesta en un listado llamado funciones, de la siguiente manera:
    funciones = [obtenerMultiplos, obtenerDivisores, obtenerNesimoFibonacci]
"""


# ------------------------ EJERCICIO 5 --------------------------------

""" El salario de un empleado de una empresa se calcula, utilizando como base  
$1200000, más un apoyo del 10% en transporte, y uno de 5% por gastos varios.
Además se paga una comisión de acuerdo al numero de ventas de los siguientes productos:
           
                precio     comisión
* Zapatos:    $ 50 000        5%
* Tenis:      $ 70 000        4%  
* Camisa:     $ 40 000        6%
* Corbata:    $ 25 000        7%
* Pantalon:   $ 35 000        5%
* Blusa:      $ 80 000        3%
* Vestido:    $ 95 000        2%

 Realice una función llamada calcularSalario, que reciba dos parametros:
 
   * El nombre del trabajador
   * Una lista con la cantidad de productos vendidos [zapatos, tenis, camisas, corbatas, pantalones, blusas, vestidos] 
 
 La funcion debe retornar =>
    Un diccionario con el nombre y el salario obtenido, por ejemplo: 
    {"nombre": "Cristian Pachon", "salario" : 2000000}  #(conserve las claves "nombre" y "salario") 
"""