from datetime import date
from time import sleep

nasc = int(input('sua data de nascimento:'))
atual = date.today().year
idade = atual - nasc
print(f'ANALISANDO.',end= ' ')
sleep(1)
print ('.',end=' ')
sleep(1)
print ('.')
sleep(3)
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('MIRIM.')
elif idade < 15 and idade > 9:
    print('INFANTIL.')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SENIOR')
else:
    print('MASTER')
print('======FIM=====')
