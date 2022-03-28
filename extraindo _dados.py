"""

Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

numeros = list()

while True:
    valor = (input('Digite um valor inteiro: '))
    if valor.isdigit():
        numeros.append(int(valor))
    while True:
        opcao = str(input('Quer continuar: [S/N] ')).upper()
        if 'N' == opcao or 'S' == opcao:
            break
        else:
            print('Opção errada! Escolha entre "S" ou "N".')
    if 'N' == opcao:
        break

print('-='*20)
print(f'Você digitou {len(numeros)} números.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente: {numeros}')
print(f'O valor 5 apareceu {numeros.count(5)} vezes na lista.')