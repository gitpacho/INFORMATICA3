# 14-09-2022

# Todo elemento en python es un objeto de alguna Clase (modelo)
isinstance([1,2,3], list)
isinstance("sdafa", str)
isinstance({1:2}, dict)

cadena1 = "Anita lava la tina"

cadena1.upper()                        #Retorna una nueva cadena en mayus
cadena1.lower()                        #Retorna una nueva cadena en minus
cadena1.count("a")                     #Retorna un entero
cadena1.isalpha()                      #Retorna un booleano
cadena1.isalnum()                      #Retorna un booleano
cadena1.isnumeric()                    #Retorna un booleano
cadena1.replace("Anita", "Cristian")   #Retorna una nueva cadena con reemplazos
cadena1.center(50)                     #Retorna una nueva cadena centrada 50 espacios


# Estan retornando una nueva cadena sin alterar la original
# Cadenas son inmutables (no se pueden alterar)


#--------------------- Indexación y slicing -------------------------

# Indexacion:  Es un método para acceder a los elementos de las cadenas
# slicing:     Es un método para acceder a rebanadas de las cadenas

cadena2 = "Mensaje para Informatica 3"
# Indexacion
print("primer => ", cadena2[0])  #primer elemento de la cadena
print("Segundo => ", cadena2[1])  #Segundo elemento de la cadena
print("PenUltimo => ", cadena2[-2]) #PenUltimo elemento de la cadena         
print("Ultimo => ", cadena2[-1]) #Ultimo elemento de la cadena

#Slicing
#Extraer toda la cadena al revés
print("Opcion 1: ", cadena2[-1:-27:-1])
print("Opcion 2: ", cadena2[-1::-1])
print("Opcion 3: ", cadena2[::-1])

#Extraer cada tercer elemento empezando en el segundo indice
print("Opcion 1: ", cadena2[2:27:3])
print("Opcion 2: ", cadena2[2::3])
print("Opcion 3: ", cadena2[-24::3])

#Extraer los dos elementos en la mitad de la cadena
print("Opcion 1: ", cadena2[12:14:1])
print("Opcion 2: ", cadena2[-14:-12:1])