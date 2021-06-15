"""
5. Elaborar un algoritmo casa de cambio, que reciba una cantidad de dinero en pesos colombianos y
realice su equivalente en dolares, yenes y euros, tenga en cuenta que el cambio deberá realizarse a la
tasa representativa de cada moneda (actual) y que la casa de cambio, incluye un 2% de ganancia a ese
valor.
"""

#Diseño

"""
Obtener el valor en pesos colombianos que se desea cambiar
Preguntar a que moneda quieren cambiar
Realizar el cambio en dolares (0,00028 cada peso en dolares) y restar el 2% al precio total
Reaizar el cambio en yenes y (0,029 cada peso en yenes )restar el 2% al precio total
Realizar el cambio en euros (0,00023 cada peso en yenes) y restar el 2% al precio total
Mostrar el cambio de la moneda
"""

#Algoritmo
Pesos = eval(input("Ingresa los pesos que quieres cambiar: "))
Cambio_de_Moneda = input("Ingrese a que moneda quiere cambiar (Dolares, Yenes o Euros): ").upper

if Cambio_de_Moneda == "DOLARES":
    
    Dolares = (Pesos * 0.00028) * 0.98

    print ("El cambio a doleres es: ", Dolares)
    
elif Cambio_de_Moneda == "YENES":
    
    Yenes = (Pesos * 0.029) * 0.98
    
    print ("El cambio a yenes s es: ", Yenes)
    
else:
    Euros = (Pesos * 0.00023) * 0.98
    
    print ("El cambio a euros es: ", Euros)
