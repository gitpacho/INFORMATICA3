"""
Aqui se controla el juego triqui
"""

import interfazJuego
import logicaJuego

interfazJuego.explicarJuego()
input(".....Ingrese enter para continuar....")
tableroJuego = logicaJuego.generarTableroLogico()

for turno in ["x", "o", "x", "o", "x", "o", "x", "o", "x"]:
    print("\nTurno judador: ", turno)
    while True:
        posicion = int(input("   Ingrese posicion de juego: "))
        validez = logicaJuego.validarPosicion(tableroJuego, posicion)
        if validez == True: break
        else: print("   warning: posicion invalida!")
    tableroJuego = logicaJuego.insertarCaracterEnTablero(tableroJuego, posicion, turno)
    interfazJuego.imprimirTablero(tableroJuego)
    posibleGanador = logicaJuego.determinarGanador(tableroJuego)
    if posibleGanador in ["x", "o"]: 
        print("Felicidades {} acaba de ganar juego".format(posibleGanador))
        break