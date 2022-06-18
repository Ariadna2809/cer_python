#Laboratorio 3.4.1.13
#Elaborado por: Ariadna Loredo

# paso 1
beatles = []
print("Paso 1:", beatles)

# paso 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# paso 3
for i in range(0,2):
    beatles.append(input("Ingrese los otros miembros: "))
    
print("Paso 3:", beatles)

# etapa 4
del beatles[-2:]
print("Paso 4:", beatles)

# paso 5
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))