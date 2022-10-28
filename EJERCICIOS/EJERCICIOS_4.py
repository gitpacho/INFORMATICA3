""" En este archivo encontramos ejercicios con los siguientes temas: 

        * Modulos
        * 
        * 

"""

#====================== EJERCICIOS MODULOS ====================

"""
Cree los modulos que indica cada ejercicio, para desarrollar los siguientes programas:

1) Algoritmo conversor de numeros     => modulos: decimal binario hexadecimal octal, control
2) Algoritmo para jugar un sudoku 4*4 => modulos: logica, interfaz, control
3) Herramienta de calificaciones      => modulos: estudiante, materia, control
4) Algoritmo operador de vectores     => modulos: vector, operacionesVectores, control
5) Algoritmo operador de matrices     => modulos: matriz, operacionesMatrices, control 

Además, tenga en cuenta agregar la documentacion de cada modulo con las funciones que considere necesarias,
Recuerde que el modulo control, consume los demás modulos y organiza el respectivo programa
"""


#====================== EJERCICIOS CLASES Y OBJETOS ====================

#==> EJERCICIO 1 
"""Los automoviles pueden ser utilizados como clases en python.
La siguiente tabla muestra el diseño en programación orientada a objetos
de diferentes tipos de autos.
----------------------------------------------------------------------------
CLASE     =>   Automoviles
OBJETOS   =>   FERRARI 458      |   MCLAREN 720S     |  AUTOLEGAL
ATRIBUTOS =>   Color rojo       |   color negro      |  Color blanco
               2-personas       |   4-personas       |  20-personas
               Deportivo        |   Deportivo        |  Publico
MÉTODOS   =>   acelerar, frenar |   acelerar, frenar |  acelerar, frenar
----------------------------------------------------------------------------

1) Crear la clase, Automoviles de la siguiente manera: 
   a) Asigne un nombre genérico a los atributos.  (color, personasSentadas, uso)
   b) Cree los métodos con el mismo nombre indicado (acelerar, frenar).
      El metodo acelerar debe recibir la aceleración (a) y tiempo (t) empleado por el vehículo. Debe retornar la velocidad alcanzada (v = a * t)
      El metodo frenar debe recibir la velocidad (v) y desaceleracion (a) empleada por el vehículo. Debe retornar el tiempo de detención (t = -v/a)

2 Crear los objetos de la clase Automoviles, de la siguiente manera:
    a) Los objetos deben tener los siguientes nombres: FERRARI_458, MCLAREN_720S, AUTOLEGAL
       Tenga en cuenta el tipo de variable en los atributos: 
                  color            =>  "rojo", "negro", "blanco"  (strings)
                  personasSentadas =>  2,4,8                      (enteros)
                  uso              => "Deportivo", "Publico"      (string)
    b) Imprima los atributos del objeto MCLAREN_720S
    c) Cambie el atributo personasSentadas del objeto MCLAREN_720S a 2
    d) Ejecute el método acelerar del objeto FERRARI_458, tomando una aceleración de 10m/s² en un tiempo de 5 s. Muestre la velocidad alcanzada en pantalla
    e) Ejecute el método frenar del objeto AUTOLEGAL, tomando una velocidad inicial de 30 m/s y una desaceleracion de -4 m/s². Muestre el tiempo de detención en pantalla
"""

   
#==> EJERCICIO 2
""" Los profesores pueden ser utilizados como clases en python.
La siguiente tabla muestra el diseño en programación orientada a objetos
de diferentes profesores.
----------------------------------------------------------------------------
CLASE     =>   Profesores Unal
OBJETOS   =>   Profe Elisabeth Restrepo |   Profe Luis Mulcue      | Profe Cristian Pachon
ATRIBUTOS =>   Mujer                    |   Hombre                 |  Hombre
               30 años                  |   25 años                |  41 años
               Agil                     |   Reflexivo              |  Observador
MÉTODOS   =>   enseñar, evaluar         |   enseñar, evaluar       |  enseñar, evaluar
----------------------------------------------------------------------------

1) Crear la clase ProfesoresUnal de la siguiente manera:    
   a) Asigne un nombre genérico a los atributos.  (nombre, sexo, edad, cualidad)
   b) Cree los métodos con el mismo nombre indicado (enseñar, evaluar).
      El metodo enseñar debe recibir la experiencia y energia empleada por el profesor en la clase. Debe retornar la calidad de su clase (de 0 al 100 en nivel de calidad)
      El metodo evaluar debe recibir el estado de ánimo del profesor. Debe retornar la dificultad del examen (de 0 a 100 en un nivel de dificultad)

2 Crear los objetos de la clase ProfesoresUnal, de la siguiente manera:
    a) Los objetos deben tener los siguientes nombres: PROFESOR1, PROFESOR2, PROFESOR3
       Tenga en cuenta el tipo de variable en los atributos: 
                  nombre   =>  "Elisabeth Restrepo",...   (strings)
                  sexo     =>  "M", "F", ...              (strings)
                  edad     =>  30, 25, 41 ...             (enteros)
                  cualidad => "Agil", "Reflexivo", ...    (strings)
    b) Imprima los atributos del objeto PROFESOR3
    c) Cambie el atributo edad del objeto PROFESOR3 a 20
    d) Ejecute el método enseñar del objeto PROFESOR1, tomando una experiencia alta y una energía baja. Muestre la calidad de su clase en pantalla
    e) Ejecute el método evaluar del objeto PROFESOR2, tomando un buen estado de animo. Muestre el nivel de dificultaden pantalla
"""

#==> EJERCICIO 3
"""Diseñe dos clases: Estudiante y Curso
La clase Estudiante debe tener los atributos: codigo, nombre, edad y 4 calificaciones
La clase Estudiante debe tener un método que permita saber el promedio de sus calificaciones

La clase Curso debe tener los atributos: Nombre de la materia, nombre del profesor, listado de estudiantes
La clase Curso debe tener un método para agregar estudiantes a mi lista, otro para eliminar un estudiante por codigo, y otro para determinar cuales estudiantes pasan la materia

Realice el ejercicio de la manera que crea más conveniente,
Luego intente abstraer que en el listado de estudiantes, utiliza objetos de la clase Estudiante,
"""


