# Escreva um programa em Python que solicite ao usuário um valor inteiro (denominado como 'n').
# O programa deve exibir o dobro desse valor para todos os números de 1 até 'n', ou seja, para 
# cada número no intervalo de 1 até 'n', você deverá calcular e mostrar o dobro desse número.

num = int(input('>>Digite um valor inteiro: \033[032m'))
print(f'\n\033[mDobro dos números de 1 até {num}:')
for i in range(1, num + 1):
    dobro = i * 2
    print(f'\033[032m{i}\033[m:{dobro}')