#Façam um programa que adiciona os itens do conjunto 2 ao conjunto 1 se o item não for repetido.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

for i in set2:
    if i not in set1:
        set1.add(i)
print(set1)

