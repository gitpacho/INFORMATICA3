"""
Este modulo sirve para imprimir unos mensajes,
este modulo no almacena nada
"""

def imprimirMensaje(nombre):
    mensaje = "hola, soy holaMundo otra vez" + nombre
    print(mensaje)
    return None

def imprimirSeparador(tipo):
    print("\n" + tipo * 50 + "\n")

def imprimirVariable(nombre, variable):
    print(nombre + " ==> " + str(variable))

def imprimirListado(lista):
    for elemento in lista:
        imprimirSeparador("-")
        print(elemento)