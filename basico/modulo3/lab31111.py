#Laboratorio 3.1.1.11
#Elaborado por: Ariadna Loredo

ingreso = float(input("Introduce el ingreso anual: "))
impuesto = 0

if ingreso <= 85528:
    impuesto = 0.18*ingreso - 556.02
else:
    impuesto = 14839.02 + (ingreso-85528)*0.32
    
impuesto = round(impuesto, 0)
print("El impuesto es:", impuesto, "pesos")