#Laboratorio 3.6.1.9
#Elaborado por: Ariadna Loredo

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []

for i in my_list:
    if i not in new_list:
        new_list.append(i)

print("La lista con elementos únicos: ", new_list)
print(my_list)