#Façam um script que peça um valor e mostre na tela se o valor é positivo ou negativo, caso o número seja zero, mostre que o número não é positivo e nem negativo.


num=int( input('Digite um numero: '))

if num > 0 :
    print('Positivo')
else:
    if num == 0 :
        print('Nem positivo nem negativo, é 0')

    else:
        print('Negativo')