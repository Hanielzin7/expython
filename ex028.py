from random import randint
import time
print ('*'*30)
computador = randint (0,5) # faz o computador pensar
print ('-='*18)
print ('vou pensar em um número entre 0 e 5')

print ('-='*18)
jogador = int (input ('o que eu pensei? rs!'))
print('PROCESSANDO...')
time.sleep(3)
if jogador == computador:
    print ('NÃOOO!Voce me venceu :(')

else:
    print ('como sempre,voce errou!hahahahahah')

print ('*'*30)