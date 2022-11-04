"""
Crear las siguientes series

* Ventas de productos
    codigo      001 002 003 004 005 006 007 008 009 010 011 012 013 014 015
    cantidades  22  3   21  10  15  18  14  13  22  12  98  32  51  45  60

* Calificaciones
    Nombre              Nota 
    Miguel Pineda        1.0 
    Maria Gonzalez       3.1 
    Jose Nuñez           5.0 
    Angelica Lozano      3.1 
    Camilo Suarez        3.2 
    Mariana Rosero       5.0 
    Esteban Quesada      3.4 
    Julia Quintero       2.0 
    Mauricio Lizcano     3.7 
    Angie Gomez          4.1 
    Camilo Restrepo      5.0 
    Mauricio Velazquez   5.0 
    Esteban Rodriguez    3.2 

 * Rendimiento deportivo
   
   Cod. Deportista (str) =>   001   002   003   004   005   006   007   008   009    010   011   012    013    014    015    016    017   018  019  020  021  022   023   024   025  026  027   028   029   030   031   032   033    034    035   036    037   038   039   040 041   042   043   044   045  046   047   048   049   050   051  052    053    054   055   056   057   058   059  060  061   062   063   064   065   066  067   068   069   070   071   072   073    074   075   076    077   078   079   080   081   082   083   084   085  086   087   088   089   090   091  092    093    094   095    096   097  098  099  100
   rendimiento     (str) =>   A     B     C     B     B     B     C     B     A      C     B     A      C      B      B      B      B     A    B    A    A    C     B     B     B    B    C     B     B     C     B     A     C      B      A     C      B     B     B     C   B     C     B     A     C     B    A     C     B     B     B    B      A      B     A     A     C     B     B    B    B     C     B     B     C     B    A     C     B     A     C     B     B      B     C     A      B     C     B     B     A     B     C     B     B    B     B     B     A     B     B    A      C      B     B      B     B    A    B    B  
"""

import pandas as pd
import numpy as np

data =np.array([22, 3,  21, 10, 15, 18, 14, 13, 22, 12, 98, 32, 51, 45, 60])
index = ["001", "002", "003", "004", "005", "006", "007", "008", "009", "010", "011", "012", "013", "014", "015"]
serieVentas = pd.Series(data = data, index=index)






