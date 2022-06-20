#Façam um Programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.

viagem = int(input('Informe a distância em Kilômetros da viagem: '))

above = 0.45
eq_o_un = 0.50

if viagem <= 200:
    print('O valor da viagem ficou em: R${:.2f}'.format((eq_o_un*viagem)))
else:
    print('O valor da viagem ficou em: R${:.2f}'.format(above*viagem))