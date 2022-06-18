#Laboratorio 3.2.1.14
#Elaborado por: Ariadna Loredo

blocks = int(input("Ingresa el número de bloques: "))

height = 0
capa = 1

while capa <= blocks:
    height += 1
    blocks -= capa
    capa += 1

print("La altura de la pirámide es: ", height)