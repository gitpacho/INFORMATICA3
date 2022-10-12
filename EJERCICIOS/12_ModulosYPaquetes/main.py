import interfaz
import logica

#print(logica.__doc__)
#print(interfaz.__doc__)

#print(dir(interfaz))

interfaz.imprimirSeparador("#")
interfaz.imprimirMensaje("Cristian Pachon")
interfaz.imprimirSeparador("#")

variable1 = logica.sumar2Nums(2,3)
print(variable1)
interfaz.imprimirSeparador("-")

variable2 = logica.sumarNNumeros(2,3,4)
print(variable2)
interfaz.imprimirSeparador("-")


