#Faça um programa que receba o faturamento e o custo de uma venda, calcule o lucro, depois calcule e imprima a margem de lucro(lucro/ faturamento) com somente duas casas decimais.


faturamento = float(input('Digite o valor: '))
print(f'Seu valor é: {faturamento} ')

custo = float(input('Digite seu valor: '))

lucro = faturamento - custo
margem = lucro / faturamento
print(f'Margem: {margem:.2f}')

