#Façam um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input("Digite seu primeiro nome: ")

senha = input("Digite uma senha: ")

while nome == senha:

   print("Digite uma senha diferente do nome!")

   nome = input("Digite seu primeiro nome: ")

   senha = input("Digite uma senha: ")