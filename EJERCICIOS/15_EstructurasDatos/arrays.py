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





















