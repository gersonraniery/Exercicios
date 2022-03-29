"""
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.

"""

pessoas = list()
dado = list()
maior = menor = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    while True:
        opcao = str(input("Quer continuar? [S/N] ")).upper().strip()
        if opcao in 'SN':
            break
        else:
            print('Opção errada!Escolha entre [S/N]')
    if opcao in 'N':
        break

print('-='*20)
print(f'foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior}kg. Peso de ', end='')
for cont in pessoas:
    if cont[1] == maior:
        print(f'[{cont[0]}] ', end='')
print()
print(f'O menor peso foi {menor}kg. Peso de ', end='')
for cont in pessoas:
    if cont[1] == menor:
        print(f'[{cont[0]}] ', end='')
print()
