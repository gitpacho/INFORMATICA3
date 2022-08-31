########### Operador de asignación:

a = 1
b = 2
c = 3

########### Operadores aritméticos:

print("-------------Operadores aritméticos------------")
print("suma            ==>", 1+2+3)
print("mult y suma     ==>", 1*2+3)
print("suma y mult     ==>", 1+2*3)
print("division entera ==>", 5//3)
print("division entera ==>", 0//3)
print("residuo         ==>", 5%2)
print("residuo         ==>", 13%9)
print("potenciacion    ==>", 9**2)
print("potenciacion    ==>", 9**0.5)


 ## orden de operaciones: **,
 #                        */,
 #                        +-,

print("concatenacion ==>", "hola" + " mundo")
print("replicacion   ==>", "a" * 10)
print("concatenacion ==>", [1] + [1,2,3])
print("repiclacion   ==>", [0] * 10)


######### Operadores lógicos

print("---------------Operadores lógicos---------------")
print("and ==>", True and False) #Solo es verdadero si ambos son verdadero
print("and ==>", False and True)
print("or ==>", True or False)  #Solo es falso si ambos son falsos
print("or ==>", False or False)

#¿Se pueden utilizar solo con booleanos?
print(1 and 1)
print(1 and 0)
print(19 and 20)
print(0 and 100)
print(100 or 0)
print(-2 or 20)
print("cristan" and "elias")
print("Unal" and " ")

## para pensar:
   #Desarrolle un algoritmo, que me imprima si un numero es mayor de 18,
   #sin utilizar el condicional if, utilice operadores lógicos para ello



############## Operadores de comparación

print("-------Operadores de comparacion----")
print("mayor         ==> ", 1 > 2)
print("menor         ==>", 19 < 0)
print("menor o igual ==>", -1001 <= -1001)
print("igual         ==>", 3 == -5)
print("mayor o igual ==>", 19 >= 20)
print("diferente de  ==>", 30 != 31)

print("cristian" > "elias")
print(True > False)
print(True > True)
print([20,2] > [20,1])

######## Operadores de pertenencia #########

#Sirve para evaluar si un elemento está contenido en otro
print("-----------Operadores de pertenencia-------------")
print('"a" in  "holamundo"       ==>',  "a" in  "holamundo")
print('"A" in "holamundo"        ==>',  "A" in "holamundo")
print('"hola" in "holamundo"     ==>',  "hola" in "holamundo")
print('" " in "hola mundo"       ==>',  " " in "hola mundo")
print('1 in [1,2,3]              ==>',  1 in [1,2,3])
print('1 in ["1", "2", "3"]      ==>',  1 in ["1", "2", "3"])
print('"3" not in "124567890"    ==>',  "3" not in "124567890" )
print('"01" in "0 1 2 3 4 5 6 7" ==>',  "01" in "0 1 2 3 4 5 6 7")




