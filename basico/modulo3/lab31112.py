#Laboratorio 3.1.1.12
#Elaborado por: Ariadna Loredo

year = int(input("Introduce un año: "))

if not year % 4 == 0:
    print('Año común')
elif not(year % 100 == 0):
    print('Año bisiesto')
elif not(year % 400 == 0):
    print('Año común')
else:
    print('Año bisiesto')