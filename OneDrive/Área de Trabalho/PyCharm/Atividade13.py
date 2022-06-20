#Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida. Escreva uma mensagem de erro se a opção for inválida. Escolha a opção:
#1- Soma de 2 números.
#2- Diferença entre 2 números (maior pelo menor).
#3- Produto entre 2 números.
#4- Divisão entre 2 números (o denominador não pode ser zero).

op = 0

while op != 5:
        print ('''Escolha uma das opções abaixo!
        [ 1 ] Soma de 2 números.
        [ 2 ] Diferença entre 2 números.
        [ 3 ] Produto entre 2 números.   
        [ 4 ] Divisão entre 2 números.
        [ 5 ] PARA PROGAMA AGORA''')
        op = int(input('Qual é a sua opção?'))
        if op == 1:
            s1 = int(input('Digite um número: '))
            s2 = int(input('Digite outro número: '))
            resultado = s1 + s2
            print('O resultado de {} + {} é igual a {}'.format(s1, s2, resultado))

        elif op == 2:
            m1 = int(input('Digite um número: '))
            m2 = int(input('Digite outro número: '))
            if m1 < m2: print('O resultado de {} - {} é igual a {}'.format(m2, m1,(m2-m1)))
            elif m1 > m2: print('O resultado de {} - {} é igual a {}'.format(m1, m2, (m1-m2)))

        elif op == 3:
            v1=int(input('Digite um número: '))
            v2=int(input('Digite outro número: '))
            print('O resultado de {} x {} é igual a {}'.format(v1, v2, (v1*v2)))

        elif op == 4:
            d1=int(input('Digite um número: '))
            d2=int(input('Digite outro número: '))
            print('O resultado de {} ÷ {} é igual a {}'.format(d1, d2, (d1/d2)))

        elif op == 5:
            break
            print('Opção Invalida')