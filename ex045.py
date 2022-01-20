#organizando tudo
import time
import random
itens = ('pedra','papel','tesoura')
computador = random.randint(0,2)
#escolhendo as jogadas
print('''SUAS JOGADAS:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')

jogador = int (input ('Qual é a sua jogada?'))
print ('JO')
time.sleep(1)
print ('KEN')
time.sleep(1)
print ('PO')

print ('-=-='*20)
print (f'O computador escolheu {itens[computador]}.')
print (f'Voce escolheu {itens[jogador]}.')
print ('-=-='*20)
#falando quem venceu
if computador  == 0: # se o computador escolheu pedra
    if jogador == 0: # jogador jogou pedra

        print ('EMPATE!')

    elif jogador == 1: #jogador jogou papel
        print('VOCÊ VENCEU!')

    elif jogador == 2: # jogador jogou tesoura
        print ('VOCÊ PERDEU!')
    else:
        print ('Jogada inválida!')

elif computador == 1: # se o computador escolheu papel

    if jogador == 0: # jogador jogou pedra

        print ('VOCÊ PERDEU!')

    elif jogador == 1: #jogador jogou papel

        print('EMPATE!')


    elif jogador == 2: # jogador jogou tesoura


        print('VOCÊ VENCEU!')
    else:
        print ('Jogada inválida!')

elif computador == 2: # se o computador escolheu tesoura

    if jogador == 0: # jogador jogou pedra
        print('VOCÊ VENCEU!')
    elif jogador == 1: #jogador jogou papel
        print('VOCÊ PERDEU!')

    elif jogador == 2: # jogador jogou tesoura
        print('EMPATE!')

    else:
        print ('Jogada inválida!')
time.sleep(60)
print ('===========FIM==========')
