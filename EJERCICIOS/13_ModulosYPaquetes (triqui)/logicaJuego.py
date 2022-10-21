"""
Modulo para la lógica del triqui

Este modulo contiene 3 funciones:

* generarTableroLogico => No recibe nada, 
                          retorna una lista de Nones
* insertarCaracterEnTablero => recibe lista, posicion, caracter
                         retorna un lista actualizada
* determinarGanador => recibe una lista (tablero)
                       retorna ganador ("x", "o", None)
"""

def generarTableroLogico():
    tableroLogico = [None,None,None,None,None,None,None,None,None]
    return tableroLogico