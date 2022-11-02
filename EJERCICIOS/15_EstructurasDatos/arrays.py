#####################################################################
""" Ejemplo: Crear los siguientes vectores, matrices y tensores. (Para ello utilice arreglos de numpy)

                     => vector1 = 1,2,3,4,5
                     => vector2 = 10,20,30,40,50

                     => matriz1 = [1 1 1
                                1 1 1
                                1 1 1]
                     => matriz2 = [1 2 3
                                4 5 6
                                7 8 9]

                     => tensor1=[[0 0 0
                                0 0 0
                                0 0 0]
                                [2 2 2
                                2 2 2
                                2 2 2]] 

                     => tensor2= [[1  2  3
                                4  5  6
                                7  8  9]
                                [10 11 12
                                13 14 15
                                16 17 18]] 
"""

import numpy as np

# Vectores con numpy
vector1 = np.array([1,2,3,4,5])
vector2 = np.array([10,20,30,40,50])

# Matrices con numpy
matriz1 = np.array([[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]])

matriz2 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

# Tensores con numpy
tensor1= np.array([ [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]],
                 
                    [[2, 2, 2],
                     [2, 2, 2],
                     [2, 2, 2]]
                 ])
tensor2= np.array([ [[1,  2,  3],
                     [4,  5,  6],
                     [7,  8,  9]],
                  
                    [[10, 11, 12],
                     [13, 14, 15],
                     [16, 17, 18]]
                 ])


#####################################################################
"""
Ejemplo: ¿Cómo crear los anteriores arreglos (vectores, matrices, tensores) de manera automática?
"""
vector1 = np.arange(1,6,1) #inicio,fin,salto
vector2 = np.arange(10, 51, 10)

matriz1 = np.ones((3,3))   #tamaño (filas,columnas)
matriz2 = np.arange(1, 10).reshape((3,3))  #reshape (filas, columnas)

tensor1 = "pendiente!!!"
tensor2 = np.arange(1,19).reshape((2,3,3))



"""
ejemplos: a) ¿Cómo apilar vector1 y vector2 ? (formar nuevo vector mas largo)
          b) ¿Cómo apilar vector1 y vector2 ? (formar nueva matriz)
          c) ¿Cómo apilar matriz1 y matriz2 ? (formar nueva matriz mas ancha)
          d) ¿Cómo apilar matriz1 y matriz2 ? (formar nueva matriz más larga)
          e) ¿Cómo apilar un vector y una matriz? (formar nueva matriz más larga o más ancha)
"""

""" a) ¿Cómo apilar vector1 y vector2 ? (formar nuevo vector mas largo)
        
        vector1 = 1 2 3 4 5       vector2 = 10 20 30 40 50
        
        vectorResultante = 1 2 3 4 5 10 20 30 40 50 
"""
vectorResultante = np.hstack((vector1, vector2))
print(vectorResultante)


""" b) ¿Cómo apilar vector1 y vector2 ? (formar nueva matriz)
        
        vector1 = 1 2 3 4 5     vector2 = 10 20 30 40 50

        matrizResultante =   1  2  3  4  5
                            10 20 30 40 50
"""

matrizResultante = np.vstack((vector1, vector2))
print(matrizResultante)


""" c) ¿Cómo apilar matriz1 y matriz2 ? (formar nueva matriz mas ancha)
        
        matriz1 =  1 1 1     matriz2 = 1 2 3
                   1 1 1               4 5 6
                   1 1 1               7 8 9
        
        => Apilarlas horizontalmente
        matrizAncha  =  1 1 1 1 2 3
                        1 1 1 4 5 6
                        1 1 1 7 8 9
"""

matrizAncha = np.hstack((matriz1, matriz2))
print(matrizAncha)


""" d) ¿Cómo apilar matriz1 y matriz2 ? (formar nueva matriz más larga)

        matriz1 =  1 1 1     matriz2 =  1 2 3
                   1 1 1                4 5 6
                   1 1 1                7 8 9
    
        => Apilarlas verticalmente
        matrizLarga =  1 1 1 
                       1 1 1 
                       1 1 1 
                       1 2 3
                       4 5 6
                       7 8 9
"""

matrizLarga = np.vstack((matriz1, matriz2))
print(matrizLarga)


"""
        e) ¿Cómo apilar una matriz y un vector? (formar una matriz más larga o más ancha)

        matriz =  1 2 3      vector = 10 20 30
            
            
                  4 5 6                            
                  7 8 9                            

        matrizResultante1 =  1  2  3
                             4  5  6
                             7  8  9
                             10 20 30

        matrizResultante2 =  1  2  3 10
                             4  5  6 20
                             7  8  9 30
           
"""
vector = np.array([10,20,30])
matriz = np.arange(1,10).reshape((3,3))

matrizResultante1 = np.vstack((matriz, vector))
print("=>", matrizResultante1)

matrizResultante2 = np.hstack((matriz, vector.reshape((3,1))))
print("=>", matrizResultante2)


# 02-11-2022


#-------------Indexado y slicing de arreglos numpy -----------------

#  vector [#columna]
#  matriz [#fila, #columna]
#  tensor [#profundidad, #fila, #columna]


"""
                     => vector1 = 1,2,3,4,5
                     => vector2 = 10,20,30,40,50

                     => matriz1 = [1 1 1
                                1 1 1
                                1 1 1]
                     => matriz2 = [1 2 3
                                4 5 6
                                7 8 9]

                     => tensor1=[[0 0 0
                                0 0 0
                                0 0 0]
                                [2 2 2
                                2 2 2
                                2 2 2]] 

                     => tensor2= [[1  2  3
                                4  5  6
                                7  8  9]
                                [10 11 12
                                13 14 15
                                16 17 18]] 
"""

"Ejemplo: Acceder al valores en 3 columnas distintas de vector1"

print("-------------indexado------------- \n\n")
value1 = vector1[0] 
value2 = vector1[2]
value3 = vector1[-1]
print(value1, value2, value3)

"Ejemplo: Acceder al valor ubicado en la fila 1, columna 3 de matriz2"
"         Acceder al valor ubicado en la mitad de  matriz2"

value1 = matriz2[0,2]
print(matriz2, value1)
value2 = matriz2[1,2]
print(matriz2, value2)

"Ejemplo: Acceder a toda la fila 2 de matriz 2"
"         Acceder a toda la columna 3 de matriz 2"

fila2 = matriz2[1,:]  #Extrae toda la fila
columna3 = matriz2[:,2]  #Extra toda la fila

print(matriz2)
print(fila2, columna3)

"""Ejemplo: Extraer la seccion  4 5   a partir de la matriz 2 
                                7 8   
 """

seccion = matriz2[1:,0:2]
print("Seccion: \n", seccion)



"""
Cree la siguiente matriz y el siguiente vector
matriz = 1  2  3  4  5    
         6  7  8  9  10  
         11 12 13 14 15  
vector = 1 2 3

Apile el vector a la matriz
y luego extraiga una seccion compuesta
por la fila 2 (indice 1) y fila 3 (indice 2)
"""

matriz = np.arange(1,16).reshape(3,5)
vector =  np.array([1,2,3]).reshape(3,1)
print(matriz, "\n",vector)
matrizApilada = np.hstack((matriz, vector))
print(matrizApilada)


#-------------- funciones estadísticas mean, std, min, max -------------

""" Ejemplo: calcular la media de vector1 y vector2 """
print("medias => ",vector1.mean(), vector2.mean())

"""Ejemplo: calcular la media de matriz 2
            por fila, 
            por columna
            total
"""

print(matriz2) 
print(matriz2.mean())        # media de todos los valores
print(matriz2.mean(axis=0))  # axis 0 es por columnas,
print(matriz2.mean(axis=1))  # axis 1 es por filas

"""
Ejemplo: determinar la desviacion estandar por filas, columnas, total => std
         determinar el maximo por filas, columnas, total => max
         determinar el minimo por filas, columnas, total => min
"""

print(matriz2.std(axis=0)) #por columnas
print(matriz2.std(axis=1)) #por filas
print(matriz2.std())       #total

print(matriz2)
print(matriz2.max(axis=0)) #por columnas
print(matriz2.max(axis=1)) #por filas
print(matriz2.max())       #total



"""
Ejemplo:  
Determine la media de productos vendidos por trabajador
Determine la media por cada producto
Determine el producto menos vendido
Determine la cantidad de productos vendidos por trabajador


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

data = [[20,      22,     30,      2,        40,        20,      3  ],
        [31,      14,     32,      15,       13,        20,      11 ],
        [24,      32,     40,      9,        12,        50,      13 ],
        [42,      12,     33,      24,       22,        32,      23 ],
        [51,      21,     25,      10,       19,        14,      2  ],
        [22,      31,     51,      21,       35,        15,      11 ],
        [21,      36,     22,      32,       39,        32,      15 ],
        [22,      33,     41,      21,       43,        31,      36 ],
        [33,      31,     20,      42,       33,        42,      35 ],
        [22,      47,     5,       28,       37,        31,      32 ],
        [24,      38,     33,      21,       41,        31,      16 ],
        [21,      18,     32,      37,       39,        22,      12 ],
        [33,      31,     21,      21,       33,        39,      25 ],
        [25,      39,     20,      48,       15,        30,      32 ],
        [27,      32,     29,      28,       37,        35,      16 ],
        [24,      12,     31,      21,       39,        32,      13 ],
        [31,      31,     50,      22,       13,        30,      21 ],
        [23,      35,     35,      39,       31,        19,      19 ],
        [26,      36,     39,      27,       35,        32,      16 ],
        [25,      31,     21,      21,       25,        37,      15 ],
        [23,      34,     35,      32,       37,        20,      49 ],
        [31,      14,     29,      39,       25,        37,      16 ],
        [26,      31,     31,      27,       37,        32,      41 ],
        [40,      42,     23,      11,       21,        15,      19 ],
        [27,      31,     39,      21,       31,        32,      25 ],
        [38,      32,     19,      29,       35,        50,      16] ]


dataArray = np.array(data)
print(dataArray)








