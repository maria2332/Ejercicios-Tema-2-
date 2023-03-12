import os
import sys
import re
import helpers
from ejercicios.ejercicio1 import Alumno 
from ejercicios.ejercicio2 import num
from ejercicios.ejercicio3 import listas
from ejercicios.ejercicio4 import estructura_cola
from ejercicios.ejercicio5 import descomponer
from ejercicios.ejercicio6 import separar
from ejercicios.ejercicio7 import agregar_una_vez




def iniciar():
    while True:
        helpers.limpiar_pantalla()

        lineas=("="*50)
        print(lineas)
        print(((("Bienvenido al menú de ejercicios de Python").upper()).center(50)))
        print(lineas)
        print(("[1]"),"Ejercicio 1: Alumno")
        print(("[2]"),"Ejercicio 2: Número mágico")
        print(("[3]"),"Ejercicio 3: Listas")
        print(("[4]"),"Ejercicio 4: Tareas")
        print(("[5]"),"Ejercicio 5: Descomposicion")
        print(("[6]"),"Ejercicio 6: Pares e impares")
        print(("[7]"),"Ejercicio 7: Agregar una vez")
        print(("[8]"),("SALIR"))
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

        elif opcion == "3":
            print("Ejercicio 3: Listas")
            list1 =list(input(("Ingresa tu primera lista: ")))
            list2 =list(input(("Ingresa tu segunda lista: ")))
            print(listas(list1, list2))

        elif opcion == "4":
            print("Ejercicio 4: Tareas")
            list_cola=[]
            NumeroTareas = int(input(("Ingresa el número de tareas: ")))
            for i in range(NumeroTareas):
                # Crear un diccionario
                cola = {}
                # Agregar elementos al diccionario
                cola['tarea '] = input(('Ingresa la tarea: '))
                cola['prioridad'] = input(('Ingresa la prioridad de la tarea: '))
                list_cola.append(cola)
            estructura_cola(list_cola)
            
        
        elif opcion == "5":
            print("Ejercicio 5: Descomposicion")
            n=input(("Ingresa un número: "))
            descomponer(n)

        elif opcion == "6":
            print("Ejercicio 6: Pares e impares")
            n=int(input(("Longitud de la lista: ")))
            lista6=[]
            for i in range(n):
                lista6.append(int(input(("Ingresa el número: "))))
            print(separar(lista6))


        elif opcion == "7":
            print("Ejercicio 7: Agregar una vez")
            # lista por inputs con ints y strings
            lista7= []
            n = int(input(("Longitud de la lista: ")))
            for i in range(n):
                lista7.append(input(("Ingresa el elemento de la lista: ")))
                if lista7[i].isnumeric():
                    lista7[i] = int(lista7[i])
            elemento = input(("Ingresa el elemento: "))
            print(agregar_una_vez(lista7, elemento))



        elif opcion == "8":
            print((F"Saliendo..."))
            break

        input((F">>> Presiona ENTER para continuar <<<"))

(iniciar())