#  Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de
# grau Celsius para Fahrenheit ou vice-versa. Para cada opção, crie uma função. Crie uma
# terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama
# a função de conversão correta.

def celsius_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
    
 
def menu(opcao):
    if opcao == 1 :
        temperatura = float(input("Digite a temperatura desejada: "))
        fahrenheit =  celsius_fahrenheit(temperatura)
        print(f"{temperatura}ºC Celsius para Farenheite fica {fahrenheit:.2F}ºF ")
    elif opcao == 2:
        temperatura = float(input("Digite a temperatura desejada: "))
        celsius =  fahrenheit_celsius(temperatura)
        print(f"{temperatura}ºF Farenheite para Celsius fica {celsius:.2f}ºC ")
    else: 
        print('OPÇÃO INVÁLIDA')


opcao = int(input('''
        [1] Celsius para Fahrenheit 
        [2] Fahrenheit para Celsius
                        
        Digite a opção desejada: '''))
menu(opcao)