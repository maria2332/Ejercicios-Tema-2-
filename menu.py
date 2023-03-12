import os
import sys
import re
import helpers
from ejercicio1 import Punto
from ejercicio1 import Rectangulo 




def iniciar():
    while True:
        helpers.limpiar_pantalla()

        lineas=("="*50)
        print(lineas)
        print(((("Bienvenido al menú de ejercicios de Python").upper()).center(50)))
        print(lineas)
        print(("[1]"),"Ejercicio 1: Alumno")
        print(("[2]"),"Ejercicio 2: Número mágico")
        print(lineas)

        opcion = input(("Elige una opción: "))
        helpers.limpiar_pantalla()

        if opcion == "1":
            print(B"Ejercicio 1: Punto")
            #ejercicicios.alumno
            Punto=input(("Ingresa un punto con cooredenadas x e y: "))
            print(Punto(Punto))

        

        elif opcion == "2":
            print("Ejercicio 2: Rectángulo")
            n=int(input(("Ingresa un punto: ")))
            print(Rectangulo(n))

        elif opcion == "8":
            print((F"Saliendo..."))
            break

        input((F">>> Presiona ENTER para continuar <<<"))

(iniciar())