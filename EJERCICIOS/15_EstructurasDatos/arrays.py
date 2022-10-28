"""
Ejemplos: crear los siguientes vectores, matrices y tensores


vector1 = 1,2,3,4,5
vector2 = 10,20,30,40,50

matriz1 = [1 1 1
           1 1 1
           1 1 1]
matriz2 = [1 2 3
           4 5 6
           7 8 9]

tensor1=[[0 0 0
          0 0 0
          0 0 0]
         [2 2 2
          2 2 2
          2 2 2]] 

tensor2= [[1  2  3
           4  5  6
           7  8  9]
          [10 11 12
           13 14 15
           16 17 18]] 
"""
import numpy as np

#Como crear los vectores numpy
vector1 = np.array([1,2,3,4,5])
vector2 = np.array([10,20,30,40,50])

#como crear matrices numpy
matriz1 = np.array([[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]])

matriz2 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

#como crear tensores
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


"""
ejemplos: como crear los anteriores elementos de manera rapida
"""

vector1 = np.arange(1,6,1) #inicio,fin,salto
vector2 = np.arange(10, 51, 10)

matriz1 = np.ones((3,3))   #tamaño (filas,columnas)
matriz2 = np.arange(1, 10).reshape((3,3))  #reshape (filas, columnas)

tensor1 = "pendiente"
tensor2 = np.arange(1,19).reshape((2,3,3))



"""
ejemplos: a) como apilar vector1 y vector2 y formar vector mas grande
          b) como apilar vector1 y vector2 y formar una matriz
          c) como apilar matriz1 y matriz1 y formar matriz mas grande
          d) como apilar matriz1 y matriz1 y formar un tensor
"""

"""
vector1 = 1,2,3,4,5,6,100
vector2 = 10,20,30,40,50
vectorResultante = 1,2,3,4,5,6,100, 10,20,30,40,50 ?????
"""
vectorResultante = np.hstack((vector1, vector2))
print(vectorResultante)

"""
vector1 = 1,2,3,4,5,6,100
vector2 = 10,20,30,40,50
matrizResultante = 1,2,3,4,5,6,100, 
                   10,20,30,40,50
"""

matrizResultante = np.vstack((vector1, vector2))
print(matrizResultante)















