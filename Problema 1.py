"""
1. Elaborar un algoritmo para calcular el área de un triangulo cuya altura
es de 30 cm y la base de 50 cm. Realizar una versión genérica de este
algoritmo para calcular el area de un triangulo dada una altura y una
base cualquiera, ¿Qué cambio se debe hacer?
"""

#Diseño

"""
Obtener primer dato = 50
Obtener segundo dato = 30
Obtener primera operacion = 50 * 30 = 1500
Obeter segunda operacion = 1500 / 2 = 750 
Mostrar resultado = 750
"""

#Algoritmo

Altura = 30

Base = 50

Area = (Altura * Base) / 2

print("El area del triangulo es:", Area ,"cm")

#Algoritmo general

Altura = eval(input("Digita la altura del triangulo "))

Base = eval(input("Digita la base del triangulo "))

Area = (Altura * Base) / 2

print("El area del triangulo es:", Area ,"cm")
