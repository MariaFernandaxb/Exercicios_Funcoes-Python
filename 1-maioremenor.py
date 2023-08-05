#  Faça um programa que recebe três números do usuário, e identifica o maior através
# de uma função e o menor número através de outra função.

def num_maior(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print('O PRIMEIRO NUMERO É MAIOR')
    elif num2 > num1 and num2 > num3:
        print('O SEGUNDO NUMERO É MAIOR')
    elif num3 > num1 and num3 > num2:
        print('O TERCEIRO NUMERO É MAIOR')
    else:
        print('OPÇÃO INVÁLIDA')

def num_menor(num1,num2,num3):
    if num1 < num2 and num1 < num3:
        print("O PRIMEIRO NUMERO É MENOR")
    elif num2 < num1 and num2 < num3:
        print('O SEGUNDO NUMERO É MENOR')
    elif num3 < num1 and num3 < num2:
        print('O TERCEIRO NUMERO É MENOR')
    else:
        print("OPÇÃO INVALIDA")

num1 = int(input("Digite o primeiro numero: ")) #variável do parâmetro
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num_maior(num1,num2,num3) #chamada da função
num_menor(num1,num2,num3) #chamada da função

