from random import randint
from time import sleep

print('-=-'*20)
print('vou pensar em um número de 0 a 5. Tente advinhar...')
print('-=-'*20)

# computador escolhendo um número
num_computador = randint(0, 5)

resp = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(1)

if resp == num_computador:
    print('PARABÉNS!Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {num_computador}.')
