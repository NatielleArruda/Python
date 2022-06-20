#Faça um programa que receba um número inteiro e imprima a tabuada desse número até o 10.

valor = int(input('Entre com um número para saber a tabuada: '))
aux = 0
print('*' * 18)
print('Tabuada de {}'.format(valor))
print('*' * 18)
while(aux <= 10):
  print('{0} X {1} = {2}'.format(aux, valor, (aux * valor)))
  aux = aux + 1