import os
import sys
import re
import helpers
from ejercicio1 import Alumno 




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
            print(B"Ejercicio 1: Alumno")
            #ejercicicios.alumno
            Alumno.cadena=input(("Ingresa tu cadena corrupta: "))
            print(Alumno.formatear_cadena(Alumno.cadena))

        

        elif opcion == "2":
            print("Ejercicio 2: Número mágico")
            n=int(input(("Ingresa un número del 1 al 9: ")))
            print(num(n))

        elif opcion == "8":
            print((F"Saliendo..."))
            break

        input((F">>> Presiona ENTER para continuar <<<"))

(iniciar())