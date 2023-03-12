import math
import helpers
from ejercicio1 import Punto
from ejercicio1 import Rectangulo

def menu():
    while True:
        helpers.limpiar_pantalla()

        print("="*50)
        print("Bienvenido al menú de ejercicios de Python".upper().center(50))
        print("="*50)
        print("[1] Ejercicio 1: Punto")
        print("[2] Ejercicio 2: Rectángulo")
        print("[3] Salir")
        opcion = input("Elige una opción: ")
        helpers.limpiar_pantalla()

        print("="*50)

        if opcion == "1":
            print("Ejercicio 1: Punto")
            x = float(input("Ingrese la coordenada x: "))
            y = float(input("Ingrese la coordenada y: "))
            punto = Punto(x, y)
            print(punto)
            print(punto.cuadrante())
            x2 = float(input("Ingrese la coordenada x del segundo punto: "))
            y2 = float(input("Ingrese la coordenada y del segundo punto: "))
            punto2 = Punto(x2, y2)
            print(punto.vector(punto2))
            print(punto.distancia(punto2))

        elif opcion == "2":
            print("Ejercicio 2: Rectángulo")
            x1 = float(input("Ingrese la coordenada x del primer punto: "))
            y1 = float(input("Ingrese la coordenada y del primer punto: "))
            punto1 = Punto(x1, y1)
            x2 = float(input("Ingrese la coordenada x del segundo punto: "))
            y2 = float(input("Ingrese la coordenada y del segundo punto: "))
            punto2 = Punto(x2, y2)
            rectangulo = Rectangulo(punto1, punto2)
            print(rectangulo.base())
            print(rectangulo.altura())
            print(rectangulo.area())

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")
            print("="*50)

        input("Presione ENTER para continuar...")
        print("="*50)
        
(menu())