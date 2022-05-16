'Defina una función en python que acepte el radio y devuelva el valor del area de un círculo de esas dimensiones. (4pts)'

from math import pi

radio = float(input("Introduzca el número para el radio: "))

def CalcularArea(radio):
    return pi * radio**2

area = CalcularArea(radio)

print("El área del circulo es de:", round(area, 2), "Unidades cuadradas")