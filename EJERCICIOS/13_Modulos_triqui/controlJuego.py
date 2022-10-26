"""
Aqui se controla el juego triqui
"""

import interfazJuego, logicaJuego

interfazJuego.explicarJuego()
tableroJuego = logicaJuego.generarTableroLogico()

for turno in ["x", "o", "x", "o", "x", "o", "x", "o", "x"]:
    print("Turno judador: ", turno)
    posicion = int(input("   Ingrese posicion de juego: "))
    tablero = logicaJuego.insertarCaracterEnTablero(tableroJuego, posicion, turno)
    interfazJuego.imprimirTablero(tablero)
    posibleGanador = logicaJuego.determinarGanador(tablero)

    