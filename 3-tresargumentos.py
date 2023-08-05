# Faça um programa, com uma função que necessite de três argumentos, e que forneça a
# soma desses três argumentos através de uma função. Seu script também deve fornecer a
# média dos três números, através de uma segunda função que chama a primeira.

def soma_args(arg_um,arg_dois,arg_tres):
    soma = arg_um + arg_dois + arg_tres
    media_args(soma)

def media_args(soma):
    media = soma / 3
    print(media)

arg_um = int(input("Digite o primeiro numero: "))
arg_dois = int(input("Digite o segundo numero: "))
arg_tres = int(input("Digite o terceiro numero: "))

soma_args(arg_um,arg_dois,arg_tres)


#fzr com a isa