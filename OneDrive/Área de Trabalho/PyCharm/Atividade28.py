#Façam um programa que imprima os valores que não repetem entre os conjuntos.

conjunto1 = {10, 20, 30, 40, 50}
conjunto2 = {30, 40, 50, 60, 70}

for i in conjunto1:
    if i not in conjunto2:
        print(i)
for i in conjunto2:
    if i not in conjunto1:
        print(i)

