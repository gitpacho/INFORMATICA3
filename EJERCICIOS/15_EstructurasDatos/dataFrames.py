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

data = np.Array([[1, 12000],   
                 [2, 15000], 
                 [3, 21000],
                 [2, 32000],
                 [1, 11000],
                 [2, 90000]])

hoja1 = pd.DataFrame( data = data,
                      columns = ["tamaño", "precio"],
                      index = ["001","002","003","004","005","006"])

print(hoja1)

