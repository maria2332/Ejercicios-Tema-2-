"""
Ejercicio

Crea una clase llamada Punto con sus dos coordenadas X e Y.
Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.
Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
(Optativo) Añade un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla. La fórmula es la siguiente:
"""

import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre el eje X"
        else:
            return "Sobre el origen"

    def vector(self, punto):
        return f"({punto.x - self.x}, {punto.y - self.y})"

    def distancia(self, punto):
        return math.sqrt((punto.x - self.x)**2 + (punto.y - self.y)**2)
    
punto1 = Punto(2, 3)
punto2 = Punto(-5, -10)
punto3 = Punto(0, 0)


print(punto1)
print(punto2)
print(punto3)

print(punto1.cuadrante())
print(punto2.cuadrante())
print(punto3.cuadrante())

print(punto1.vector(punto2))
print(punto2.vector(punto1))

print(punto1.distancia(punto2))
print(punto2.distancia(punto1))


"""
Crea una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.
Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.
Añade al rectángulo un método llamado base que muestre la base.
Añade al rectángulo un método llamado altura que muestre la altura.
Añade al rectángulo un método llamado area que muestre el area.
"""

import math

class Rectangulo:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        return abs(self.punto2.x - self.punto1.x)

    def altura(self):
        return abs(self.punto2.y - self.punto1.y)

    def area(self):
        return self.base() * self.altura()
    
punto1 = Punto(2, 3)
punto2 = Punto(-5, -10)

rectangulo = Rectangulo(punto1, punto2)

print(rectangulo.base())
print(rectangulo.altura())
print(rectangulo.area())
