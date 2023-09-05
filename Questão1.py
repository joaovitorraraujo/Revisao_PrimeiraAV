# Crie um programa em Python que leia um valor inteiro e exiba todos os números pares 
# e ímpares no intervalo de 1 a esse valor, separando-os. 

num = int(input('Digite um valor inteiro: \033[032m'))
print(f'\n\033[033mNúmeros pares até {num}:\033[m',end='')
for i in range(2, num + 1, 2):
    print(f'{i} ', end='')
print(f'\n\033[033mNúmeros ímpares até {num}:\033[m',end='')
for i in range(1, num + 1, 2):
    print(f'{i} ', end='')
