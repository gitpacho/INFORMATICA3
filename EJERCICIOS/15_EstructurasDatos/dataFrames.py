#09-11-2022

"""crear un dataFrame compuesto por la siguiente informacion =>

codigo   tamaño   precio  
  001      1       12000   
  002      2       15000 
  003      3       21000
  004      2       32000
  005      1       11000
  006      2       90000"""

import numpy as np
import pandas as pd

data = np.array([[1, 12000],   
                 [2, 15000], 
                 [3, 21000],
                 [2, 32000],
                 [1, 11000],
                 [2, 90000]])

hoja1 = pd.DataFrame( data = data,
                      columns = ["tamaño", "precio"],
                      index = ["001","002","003","004","005","006"])
print(hoja1)




"""
Crear un DataFrame que cumpla con lo siguiente

cada columna va a ser referencia a 5 funciones: ["f1","f2","f3","f4","f5"]
los indices van a ser la variable independiente: [0, 0.5, 1, 1.5, ...200]

f1(x) = 3x + 5
f2(x) = x + random
f3(x) = sen(x)
f4(x) = e^x
f5(x) = x*sinx + random


    |  f1     f2      f3     f4     f5
----------------------------------------
0   |  5    | 0.3  |   0  |  2.71 |  0
0.5 |  6.5  | 0.7  |   .  |   .   |  .
1   |  8    | 1.2  |   .  |   .   |  .
1.5 |  9.5  | 1.6  |   .  |   .   |  .
.   |  .    | .    |   .  |   .   |  .
.   |  .    | .    |   .  |   .   |  .
.   |  .    | .    |   .  |   .   |  .
200 |  605  | 200.2|   .  |   .   |  .
"""

x = np.arange(0,200.5, 0.5)
f1 = 3 * x + 5
f2 = x + np.random.rand(401)
f3 = np.sin(x)
f4 = np.log(x)
f5 = x * np.sin(x) + np.random.rand(401)

print("f1 =>", f1[0:5])
print("f2 =>", f2[0:5])
print("f3 =>", f3[0:5])
print("f4 =>", f4[0:5])
print("f5 =>", f5[0:5])

hoja2 = pd.DataFrame(data=np.empty((401, 5)),
                     columns=["f1","f2","f3","f4","f5"],
                     index = np.arange(0,200.5,0.5))