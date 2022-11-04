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

index = ["001", "002", "003", "004", "005", "006", "007", "008", "009", "010", "011", "012", "013", "014", "015"]
data =np.array([22, 3,  21, 10, 15, 18, 14, 13, 22, 12, 98, 32, 51, 45, 60])
serieVentas = pd.Series(data = data, index=index)
print(serieVentas)


index = ["Miguel Pineda","Maria Gonzalez","Jose Nuñez","Angelica Lozano","Camilo Suarez","Mariana Rosero","Esteban Quesada","Julia Quintero","Mauricio Lizcano","Angie Gomez","Camilo Restrepo","Mauricio Velazquez","Esteban Rodriguez"]
data = np.array([1.0,3.1,5.0,3.1,3.2,5.0,3.4,2.0,3.7,4.1,5.0,5.0,3.2])
serieCalificaciones = pd.Series(data=data, index=index)
print(serieCalificaciones)


index =  ["001",   "002",   "003",   "004",   "005",   "006",   "007",   "008",   "009",    "010",   "011",   "012",    "013",    "014",    "015",    "016",    "017",   "018",  "019",  "020",  "021",  "022",   "023",   "024",   "025",  "026",  "027",   "028",   "029",   "030",   "031",   "032",   "033",    "034",    "035",   "036",    "037",   "038",   "039",   "040", "041",   "042",   "043",   "044",   "045",  "046",   "047",   "048",   "049",   "050",   "051",  "052",    "053",    "054",   "055",   "056",   "057",   "058",   "059",  "060",  "061",   "062",   "063",   "064",   "065",   "066",  "067",   "068",   "069",   "070",   "071",   "072",   "073",    "074",   "075",   "076",    "077",   "078",   "079",   "080",   "081",   "082",   "083",   "084",   "085",  "086",   "087",   "088",   "089",   "090",   "091",  "092",    "093",    "094",   "095",    "096",   "097",  "098",  "099",  "100"]
data =   np.array(["A","B","C","B","B","B","C","B","A","C","B","A", "C",  "B",  "B",  "B",  "B", "A","B","A","A","C", "B", "B", "B","B","C", "B", "B", "C", "B", "A", "C",  "B",  "A", "C",  "B", "B", "B", "C",   "B", "C", "B", "A", "C", "B","A", "C", "B", "B", "B","B",  "A",  "B", "A", "A", "C", "B", "B","B","B", "C", "B", "B", "C", "B","A", "C", "B", "A", "C", "B", "B",  "B", "C", "A",  "B", "C", "B", "B", "A", "B", "C", "B", "B","B", "B", "B", "A", "B",  "B", "A","C","B",  "B","B",  "B", "A", "B", "B"])
serieDeportistas = pd.Series(data=data, index=index)
print(serieDeportistas)



"""
Imprimir los indices, data y tamaño de la serieVentas utilizando sus atributos
"""

print(serieVentas)
print("indices => ", serieVentas.index)
print("data =>", serieVentas.values)
print("tamaño =>", serieVentas.shape)



"""
Imprimir la media, desviacion, el minimo y el maximo de la serieCalificaciones
"""


media = serieCalificaciones.mean()
desviacion = serieCalificaciones.std()
min = serieCalificaciones.min()
max = serieCalificaciones.max()

print("estadisticos=>", media, desviacion, min, max)


"""
Imprimir el codigo del producto menos vendido, y el codigo del producto mas vendido de serieVentas
"""

productoMenosVendido = serieVentas.idxmin()
productoMasVendido = serieVentas.idxmax()

print("productos => ", productoMenosVendido, productoMasVendido)


"""
Acceder mediante indexado a 3 valores de la serieDeportistas 
utilizando el indice numerico y el indice clave
"""

print(serieDeportistas[0], serieDeportistas[-1], serieDeportistas[3])
print(serieDeportistas["001"], serieDeportistas["100"], serieDeportistas["004"])


"""
El precio de venta de los artículos de una empresa es el siguiente:
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


a) Crear 2 series => seriePrecioProductos (con claves y precios)
                  => serieVentasProductos (con claves y unidades vendidas)

b)
"""








