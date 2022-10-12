"""
Este modulo sirve para realizar algunas operaciones
y se almacenan algunas variables

contiene dos funciones
"""


def sumar2Nums(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

def sumarNNumeros(*numeros): #numeros se interpreta como un listado
    suma = sum(numeros)
    return suma

##### Para hacer el testeo del modulos ####
if __name__ == "__main__":
    a = sumar2Nums(1,2)
    print(a)
    b = sumarNNumeros(1,2,3,4,5,6,7,8)
    print(b)




