#Laboratorio 3.2.1.15
#Elaborado por: Ariadna Loredo

c0 = int(input("Ingresa cualquier número entero que no sea negativo y que no sea cero : "))
pasos = 0

if c0 <=1:
    c0 = int(input("Ingresa cualquier número entero que no sea negativo y que no sea cero : "))
    
while c0 != 1:
    if c0 %2 == 0:
        c0 = c0//2
        pasos +=1
        print(c0)
    if c0 %2 != 0:
        if c0 != 1:
            c0 = 3 * c0 + 1
            print(c0)
            pasos +=1
        if c0 == 1:
            print("Pasos= ", pasos)