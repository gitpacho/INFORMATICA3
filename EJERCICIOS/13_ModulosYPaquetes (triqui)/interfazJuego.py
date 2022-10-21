"""
Aqui contenemos la parte visual del
triqui. Este modulo contiene 2 funciones:

* explicarJuego: retornar mensaje explicativo
* imprimirTablero: retornar string con el tablero
"""

def explicarJuego():
    explicacion  = """
    ============================================
    Bienvenido, esto es triki.

    Para ganar debe completar una linea recta, 
    compuesta por un mismo caracter ("x" o "o")

    Linea recta => horizontal o vertical o diagonal

    Debe ingresar la posicion 0-8, para ingresar
    la opcion durante su turno. Las posiciones son
    las siguientes:

    tablero  =>    0 | 1 | 2  
                 -------------
                   3 | 4 | 5  
                 -------------
                   6 | 7 | 8  

    ============================================
    """
    print(explicacion)

lista = ["x", None, None,None ,None ,"x",None ,None ,"o"]

def imprimirTablero(tableroLogico:list):
    tableroVisual = """
                     {} | {} | {}  
                   -------------
                     {} | {} | {}  
                   -------------
                     {} | {} | {}  """.format(tableroLogico[0],
                     tableroLogico[1], tableroLogico[2], tableroLogico[3],
                     tableroLogico[4], tableroLogico[5], tableroLogico[6],
                     tableroLogico[7], tableroLogico[8])
    print(tableroVisual)




    



