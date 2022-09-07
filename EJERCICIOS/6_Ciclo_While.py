""" Crear un ciclo infinito """


#while True:
#    print("ciclo ejecutado")


""" Crear un ciclo infinito, pero
protegerlo en caso de que se ejecute
más de 100 veces """

contador = 0
while True:
    print("ciclo ejecutado {}".format(contador))
    contador = contador + 1
    
    if contador > 100:
        print("Contador superado")
        print("Vamos a romper la ejecución")
        break


