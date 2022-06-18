#Laboratorio 3.2.1.11
#Elaborado por: Ariadna Loredo

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.

user_word = input("Ingrese la palabra: ")
user_word = user_word.upper()
word_without_vowels = ""
vocales = "AEIOU"

for letter in user_word:
   if letter not in vocales: 
       word_without_vowels = word_without_vowels + letter
   else:
       continue
# Imprimir la palabra asignada a word_without_vowels.
print(word_without_vowels)