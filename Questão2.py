# Desenvolva um algoritmo em Python que receba 3 notas e faça a média. O sistema deverá exibir:
# - Aprovado: se a média for maior ou igual a 7;
# - Reposição: se a média for menor que 7 mas maior ou igual a 4;
# - Reprovado: se a média for menor que 4.

print(">>Digite suas notas abaixo para o cálculo de média\n")
nota1 = float(input("Digite sua primeira nota:\033[032m"))
nota2 = float(input("\033[mDigite sua segunda nota:\033[032m"))
nota3 = float(input("\033[mDigite sua terceira nota:\033[032m"))

media = (nota1 + nota2 + nota3)/3

if media >=7:
    resultado = "\033[032mAprovado"
elif media >=4 and media<7:
        resultado = "\033[033mReposição"
else:
        resultado = "\033[031mReprovado"

print(f'\n\033[mMedia:\033[032m {media:.2f}')
print(f'\033[mResultado: {resultado}!\033[m')