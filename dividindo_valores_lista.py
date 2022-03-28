"""

Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os
valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""

valores = list()
pares = list()
impares = list()

while True:
    num = int((input('Digite um valor inteiro: ')))
    valores.append(num)
    # checando se quer continuar
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()
        if opcao in 'SN':
            break
        else:
            print('Opção errada! Escolha apenas "S" ou "N"')
    if opcao in 'N':
        break

for cont in range(len(valores)):
    if valores[cont] % 2 == 0:
        pares.append(valores[cont])
    else:
        impares.append(valores[cont])
print('-='*20)
print(f'Lista completa é {valores}')
print(f'A lista só com valores pares {pares}')
print(f'A lista só com valores impares {impares}')
