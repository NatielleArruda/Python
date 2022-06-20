#Façam um programa que pergunta a idade do usuário. Se o usuário não for menor de idade, exiba uma mensagem de boas vindas. Caso o contrário, exiba uma mensagem informando que não é permitido menores de idade no estabelecimento.

idade=int(input('Entre com a idade: '))

if idade>17 :
    print('Você é de maior, Boas vindas!!')
else:
    print(f'Não é permitido menores de idade no estabelecimento.')

    