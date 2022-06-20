#Façam um programa que adicione 3 valores recebidos pelo usuário na lista abaixo.
#lista = [1, 2,3, 4, 5, 6, 7, 8, 9, 10]

lista = [1,2,3, 4, 5, 6, 7, 8, 9, 10]

for i in range(3):
    lista.append(input(f'Digite o  {i+1} numero: '))
print(lista)
