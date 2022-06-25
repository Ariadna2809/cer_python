#Laboratorio 4.3.1.9
#Elaborado por: Ariadna Loredo

def is_prime(num):
    div = 2
    while div<=num:
        if num % div != 0:
            div+=1
            return num
        else:
            return False
    
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()