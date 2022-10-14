from termios import FF1
import interfaz
import logica

#print(logica.__doc__)
#print(interfaz.__doc__)

#print(dir(interfaz))

interfaz.imprimirSeparador("#")
interfaz.imprimirMensaje("Cristian Pachon")
interfaz.imprimirSeparador("#")

variable1 = logica.sumar2Nums(2,3)
interfaz.imprimirVariable("suma2Nums", variable1)
interfaz.imprimirSeparador("-")

variable2 = logica.sumarNNumeros(2,3,4)
interfaz.imprimirVariable("sumaNNumeros", variable2)
interfaz.imprimirSeparador("-")


"""
Crear un modulo llamado fechas en el cual almacene fechas importantes

ejemplo:
fechaImportante1 = "20-07"
fechaImportante2 = "15-05"
fechaImportante3 = "06-03"
... 3 mas

consuma desde main.py todas las fechas importantes, 
almacenandolas en una lista llamada listaFechasImportantes
imprima cada elemento del listado
 separando las fechas consumiendo la funcion imprimirSeparador
"""
import fechas
f1 = fechas.fechaImportante1
f2 = fechas.fechaImportante2
f3 = fechas.fechaImportante3
f4 = fechas.fechaImportante4
f5 = fechas.fechaImportante5
f6 = fechas.fechaImportante6
listaFechasImportantes = [f1, f2, f3, f4, f5, f6]
interfaz.imprimirListado(listaFechasImportantes)
