# Você foi designado para desenvolver um programa que converta temperaturas entre diferentes escalas. 
# Suas tarefas são as seguintes:
# a) Escreva um programa em Python que exiba um menu com as seguintes opções:
#    1-Converter de Celsius para Fahrenheit
#    2-Converter de Fahrenheit para Celsius
# b) Caso usuário seleciona 1 (converter Celsius para Fahrenheit) Realize a conversão da temperatura de Celsius para Fahrenheit 
# utilizando a fórmula: Fahrenheit = (Celsius * 9/5) + 32. Exiba o resultado da conversão.
# c) Caso usuário seleciona 2 (converter Fahrenheit para Celsius)Realize a conversão da temperatura de Fahrenheit para Celsius
# utilizando a fórmula: Celsius = (Fahrenheit - 32) * 5/9. Exiba o resultado da conversão.

print('Bem-vindo ao Conversor de Temperaturas!')
print('\nEscolha uma opção:\n1.Conversor de Celsius para Fahrenheit\n2.Conversor de Fahrenheit para Celsius')
opcao = int(input('>>Opção: '))
match opcao:
    case (1):
        celsius = float(input('Digite a temperatura em Celsius: '))
        Fahrenheit = (celsius * 9/5) + 32
        print(f'{celsius} graus Celsius é igual a {Fahrenheit} graus Fahrenheit')
    case (2):
        fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
        Celsius = (fahrenheit - 32) * 5/9
        print(f'{fahrenheit} graus Fahrenheit é igual a {Celsius} graus Celsius')
