#Façam um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.


salario = float(input('Informe o valor do seu salário: '))

if salario > 1250:
    print('Você receberá um aumento no valor de R${:.2f} e seu salário total será de R${:.2f}'.format(salario*0.1, (salario*0.1)+salario))

else:
    print('Você receberá um aumento no valor de R${:.2f} e seu salário total será de R${:.2f}'.format(salario*0.15, (salario*0.15)+salario))
