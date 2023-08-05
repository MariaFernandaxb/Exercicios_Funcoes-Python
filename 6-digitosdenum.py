# Faça uma função que informe a quantidade de dígitos de um determinado número
# inteiro informado.

def qntd_digitos(numero):
    digitos = len(numero)
    return digitos


informe = input("Digite um número: ")
digitos = qntd_digitos(informe)
print(f"O numero {informe} contém {digitos} digitos")