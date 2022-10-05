# 05 - 10 - 2022

#---------------------EJERCICIOS DICCIONARIOS ---------------------

#Los diccionarios son una estructura de datos que contienen
#un par clave-valor. Permite acceder a la información de una manera
# mas personalizada y eficiente

diccionarioEstudiantes = {
    "Cristian Pachon": 2.0,
    "Maria Bermudez" : 3.0,
    "Camilo Ibarra" : 4.0,
    "Fernanda Gutierrez": 5.0
}

diccionarioPaises = {
    "Colombia": ["Cali", "Manizales", "Cartagena"],
    "Argentina": ["Buenos Aires", "La plata", "Cordoba"],
    "Brasil": ["Sao Paulo", "Brasilia", "Minas Gerais"]
}

diccionarioNumeros = {
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco"
}

# ¿Cómo extraer un valos dada una clave
"""Extraer del diccionario estudiantes el valor de la clave Camilo Ibarra"""
valor = diccionarioEstudiantes["Camilo Ibarra"]
print(valor)
"""Imprimir todos los valores de diccionarioEstudiantes"""

for clave in ["Cristian Pachon","Maria Bermudez","Camilo Ibarra","Fernanda Gutierrez"]:
    print(diccionarioEstudiantes[clave])

# ¿Cómo eliminar un par clave-valor?
"""Eliminar los elementos cuya clave empiece por la letra C en diccionarioEstudiantes"""

for clave in ["Cristian Pachon","Maria Bermudez","Camilo Ibarra","Fernanda Gutierrez"]:
    if clave[0] == "C":
        diccionarioEstudiantes.pop(clave)
print(diccionarioEstudiantes)

# ¿Cómo agregar un par clave-valor?
"""Agregar los siguientes estudiantes en el diccionarioEstudiantes
- Juan Loaiza (3.2)
- Sofia Ospina (5.0)
- Miguel Pineda (3.1)
"""

diccionarioEstudiantes["Juan Loaiza"] = 3.2
diccionarioEstudiantes["Sofia Ospina"] = 5.0
diccionarioEstudiantes["Miguel Pineda"] = 3.1
print(diccionarioEstudiantes)


# ¿Cómo cambiar un valor?
"""Cambiar la calificacion de diccionarioEstudiantes así:
    -Mujeres: 5.0
    -Hombres: 0.0
"""

for clave in diccionarioEstudiantes:
    if clave.split()[0][-1] == "a":
        diccionarioEstudiantes[clave] = 5.0
    else:
        diccionarioEstudiantes[clave] = 0.0
print(diccionarioEstudiantes)


# ¿cómo extraer todas las claves de un diccionario?

claves = diccionarioEstudiantes.keys()
print(claves)

# ¿ Cómo extraer todos los valores de un diccionario

valores = diccionarioEstudiantes.values()
print(valores)


# ¿ Como extraer los pares clave-valor?
parejas = diccionarioEstudiantes.items()
print(parejas)


"""
IMPRIMIR TODAS LAS PAREJAS CLAVE-VALOR DE diccionarioEstudiantes
DE 2 MANERAS (utilice ciclo for)

ejemplo => Maria Bermudez-5.0 
           Fernanda Gutierrez-5.0
           .....
           .....
"""


"""
EJERCICIOS CLASE

1) Crear la siguiente base de datos utilizando diccionarios
Costo de entrada al cine 

                   Niños       Adultos
Entre semana        5000         7000
Fin de semana       8000         1000

* ¿Cómo acceder al precio de la entrada utilizando como claves
si es niño-adulto y si es Entre Semana-Fin de semana

2) Crear la siguiente base de datos utilizando diccionarios

CodEstudiante   Ingles Deportes Idiomas Cuantica Españos
    01           2.0     2.2     4.2       4.0    0.5
    02           2.2     1.0     4.0       3.1    4.0
    03           2.9     4.2     3.1       0.0    3.1
    04           2.0     4.0     4.0       0.2    0.0
    05           2.2     0.2     0.2       1.0    0.2
    06           2.0     5.0     1.0       1.3    1.0
    07           5.0     1.2     1.2       1.9    1.3
    08           0.2     2.9     1.0       4.2    1.9
    09           5.0     2.3     2.9       2.9    0.2
    10           4.2     5.0     4.2       4.2    3.9
    11           4.5     4.2     4.0       0.5    4.2
    12           4.2     4.5     4.2       0.0    0.5
    13           0.5     0.5     2.3       4.2    0.0
    14           4.1     3.1     2.5       4.3    3.2
    15           4.2     4.2     4.2       2.5    4.3
    16           4.1     0.0     4.5       4.2    2.5
    17           1.2     3.1     0.5       4.5    3.2
    18           0.5     0.2     4.1       4.1    4.5
    19           2.2     0.5     0.2       0.2    4.1

*Cómo acceder a la base de datos utilizando como clave
 el codigo y la materia
*Determine el promedio de cada estudiante             
*Determine el promedio de cada una de las materias
*Determine los 3 estudiantes con peor promedio



0.5
4.0
3.1
0.0
0.2
1.0
1.3
1.9
0.2
3.9
4.2
0.5
0.0
3.2
4.3
2.5
3.2
4.5
4.1
3.2








"""


