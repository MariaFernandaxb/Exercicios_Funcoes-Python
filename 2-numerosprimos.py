# Faça um script que recebe um inteiro n e mostra todos os primos, de 1 até n.
def numero_primo(n):
    for numero in range(1,n+1): #começando do 1 e somando a variavel 
        if n % numero == 0: # Identificando numeros primos --  N divisível por numero restando 0 
            print(numero)


n = int(input("Digite um número: "))
numero_primo(n)

