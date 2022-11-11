import pandas as pd
import numpy as np

"""
Creamos un dataFrame con 3 columnas: ["F1", "F2", "F3"]
                         100 indices: [0.01, 0.02 ..0.99, 1] (valores de x)

F1(x) = xsin(x) + 0.2*random(x)
F2(x) = cos(x) +  0.1*random(x) 
F3(x) = x + 1/2
 """

hoja1 = pd.DataFrame(data= np.empty((100,3)),
                     index= np.arange(0.01, 1.01, 0.01),
                     columns= ["F1", "F2", "F3"]
)

print(hoja1)



