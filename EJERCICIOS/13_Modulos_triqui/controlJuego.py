"""
Aqui se controla el juego triqui
"""

import interfazJuego, logicaJuego

interfazJuego.explicarJuego()
input(".....Ingrese enter para continuar....")

tableroJuego = logicaJuego.generarTableroLogico()
for turno in ["x", "o", "x", "o", "x", "o", "x", "o", "x"]:
    print("\nTurno judador: ", turno)
    posicion = int(input("   Ingrese posicion de juego: "))
    tablero = logicaJuego.insertarCaracterEnTablero(tableroJuego, posicion, turno)
    interfazJuego.imprimirTablero(tablero)
    posibleGanador = logicaJuego.determinarGanador(tablero)
    if posibleGanador in ["x", "o"]: 
        print("Felicidades {} acaba de ganar juego".format(posibleGanador))
        break

    