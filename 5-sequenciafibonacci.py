# A série de Fibonacci é uma sequência de números, cujos dois primeiros são 0 e 1. O
# termo seguinte da sequência é obtido somando os dois anteriores. Faça um script em
# Python que solicite um inteiro positivo ao usuário, n. Então, uma função exibe todos os
# termos da sequência até o n-ésimo termo. Use recursividade.

def seq_fibonacci(n):
    fibonacci = [0,1]
    
usuario = int(input("Digite um numero inteiro positivo: "))

