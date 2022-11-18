nombre_completo = ""   #Por favor ingrese su nombre COMPLETO en la cadena

# ----------------------------Ejercicios INFORME 2--------------------------------
"""
Recomendaciones:
 - Recuerde almacenar las respuestas tal como se pide en cada ejercicio
 - Se resuelve de manera individual, la copia será anulada.
 - No hay necesidad de escribir las preguntas en su archivo ejercicios2.py
 - Muestre sus procedimientos de manera clara
"""


# ------------------------ EJERCICIO 1 --------------------------------
"""
    Cree los modulos: decimal, binario, octal, hexadecimal, control (en la carpeta INFORME3)
    El modulo decimal debe tener las siguientes funciones:
            convertirABinario     => recibe string (cadena_decimal), retorna string (cadena_binario)
            convertirAOctal       => recibe string (cadena_decimal), retorna string (cadena_octal)
            convertirAHexadecimal => recibe string (cadena_decimal), retorna string (cadena_hexadecimal)

    El modulo binario debe tener las siguientes funciones:
            convertirADecimal     => recibe string (cadena_binario), retorna string (cadena_decimal)
            convertirAOctal       => recibe string (cadena_binario), retorna string (cadena_octal)
            convertirAHexadecimal => recibe string (cadena_binario), retorna string (cadena_hexadecimal)

    El modulo Octal debe tener las siguientes funciones:
            convertirABinario     => recibe string (cadena_octal), retorna string (cadena_binario)
            convertirADecimal     => recibe string (cadena_octal), retorna string (cadena_decimal)
            convertirAHexadecimal => recibe string (cadena_octal), retorna string (cadena_hexadecimal)

    El modulo Hexadecimal debe tener las siguientes funciones:
            convertirABinario => recibe string (cadena_hexadecimal), retorna string (cadena_binario)
            convertirADecimal => recibe string (cadena_hexadecimal), retorna string (cadena_decimal)
            convertirAOctal   => recibe string (cadena_hexadecimal), retorna string (cadena_Octal)

    El modulo control queda a su disposicion:
            Servirá para mostrar las opciones de conversion
            y realizar el control del programa (realice las sentencias que considere necesarias)
            
"""

# ------------------------ EJERCICIO 2 --------------------------------
"""
    500 estudiantes han realizado un curso en linea. Sus calificaciones se encuentran en el archivo estudiantes.csv

    Lea el archivo utilizando el siguiente codigo:
       | import pandas as pd
       | archivo = "estudiantes.csv"
       | ruta = "INFORME3/" + archivo
       | hojaEstudiantes = pd.read_csv(ruta, index_col="codigo", dtype={"codigo":str})
       | #print(hojaEstudiantes)

    a) Determine el promedio de cada estudiante. 
       La respuesta debe ser una serie con el codigo del estudiante y el promedio de cada uno
       Guardela en una variable llamada  promediosEstudiantes
    b) Determine el promedio de cada examen
       La respuesta debe ser una serie con el examen y promedio de cada examen
       Guardela en una variable llamada  promediosExamenes
    c) Determine el codigo del estudiante con el promedio mas alto
       La respuesta debe ser un string
       Guardela en la variable llamada mejorEstudiante
    d) Determine el codigo del estudiante con el promedio mas bajo
       La respuesta debe ser un string
       Guardela en la variable llamada peorEstudiante
    e) Entregue la resupesta así:
       reporteEstudiantes = [promediosEstudiantes, promediosExamenes, mejorEstudiante, peorEstudiante]
"""

# ------------------------ EJERCICIO 3 --------------------------------

"""
    Las ventas de productos de una empresa es el siguiente: 
    ["B005-22Unidades","W307-15Unidades","A011-31Unidades","P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-12Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","A032-52Unidades","B001-29Unidades","A125-15Unidades","A032-22Unidades","P009-25Unidades","B005-20Unidades","B001-19Unidades","P009-31Unidades","B005-22Unidades","W307-15Unidades","A011-31Unidades","P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-52Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","Z278-30Unidades","Z025-24Unidades","Z278-21Unidades","A001-31unidades","A032-32Unidades","B001-22Unidades","A125-11Unidades","A032-12Unidades","P009-19Unidades","B005-11Unidades","B001-19Unidades","B005-20Unidades","B001-19Unidades","P009-31Unidades","B005-22Unidades","W307-15Unidades","Z278-30Unidades","Z025-24Unidades","P009-21Unidades","Z278-30Unidades","Z025-24Unidades","Z278-11Unidades","A001-91unidades","A032-52Unidades","B001-29Unidades","A125-15Unidades","A032-22Unidades","P009-25Unidades","B005-20Unidades","B001-19Unidades","P009-31Unidades","B005-22Unidades","W307-15Unidades","A011-31Unidades","P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-52Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","Z278-30Unidades","Z025-24Unidades","Z278-21Unidades","A001-31unidades","A032-32Unidades","B001-22Unidades","A125-11Unidades","A032-12Unidades","P009-19Unidades","B005-11Unidades","B001-19Unidades","P009-21Unidades","B005-22Unidades","W307-15Unidades","A011-31Unidades","P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-12Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","Z278-30Unidades","Z025-24Unidades","Z278-11Unidades","A001-91unidades","A032-52Unidades","B001-29Unidades","A125-10Unidades","A011-31Unidades","P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-52Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","Z278-30Unidades","Z025-24Unidades","Z278-21Unidades","A001-31unidades","A032-32Unidades","B001-22Unidades","A125-11Unidades","A032-12Unidades","P009-19Unidades","B005-11Unidades","B001-19Unidades","P009-21Unidades","B005-22Unidades","W307-15Unidades","A011-31Unidades","P019-18Unidades","A011-21Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-15Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","A032-22Unidades","P009-25Unidades","Z278-11Unidades","A001-91unidades"]

    a) Crear una serie pandas. Con el numero de unidades vendidas por producto.
       Guardela en una serie llamada ventasPorProducto (con codigo (str) y unidades vendidas(int)) 

    b) Determine la media (int), mediana (int), desviacion(int), maximo(int), minimo(int) de los productos vendidos
      Guarde los resultados así:
      estadisticas = [media, mediana,desviacion, maximo, minimo]

    c) Determine el codigo del producto mas vendido y el codigo de producto menos vendido
       extremos = [masVendido, menosVendido]

    e) Entregue la respuesta así:
       reporteVentas = [ventasPorProducto, estadisticas, extremos]
"""


# ------------------------ EJERCICIO 4 -------------------------------- 
"""
    Dados dos arreglos numpy cualquiera (arreglo x, arreglo y) provenientes de una funcion arbitraria y = f(x)

    Cree una funcion que reciba dos arreglos numpy x, y. 
    Esta funcion debe graficar  y   = f(x)   
                                y'  = f'(x)  
                                y'' = f''(x)
    (Realice las 3 graficas sobre un mismo lienzo)

    La funcion se debe llamar graficaGenerica, guiese siguiendo el siguiente esquema:

       | def graficaGenerica(x, y):
       |     #Valores numericos   
       |     y_derivadaOrden1 = ...
       |     y_derivadaOrden2 = ...
       |
       |     #Grafica
       |     import matplotlib.pyplot as plt
       |     plt.figure()
       |     plt.subplot(1,3,1)
       |     plt.plot(...)      # y vs x
       |     plt.subplot(1,3,2)
       |     plt.plot(...)      # y' vs x
       |     plt.subplot(1,3,3)
       |     plt.plot(...)      # y'' vs x
       |     plt.legend()
       |     plt.show()
"""