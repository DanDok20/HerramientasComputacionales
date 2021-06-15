"""
3. Elaborar un algoritmo que realice la transformaciónde grados
Celsius a Fahrenheit
"""

#Diseño:

"""
Obtener grados celsius
Convertir los grados celsius a fahrenheit = grados celsius * 9 / 5 + 32
Mostrar resultado
"""

def Fahrenheit(Celsius):
    Fahrenheit = Celsius * (9 / 5) + 32
    return Fahrenheit

Celsius = eval(input("Introducir grados celsius "))

F = Fahrenheit(Celsius)

print("La conversion a grados Fahrenheit equivale a: ", F)

