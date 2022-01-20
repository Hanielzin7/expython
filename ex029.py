velocidade = float (input ('qual é a velocidade atual do carro?'))
if velocidade > 80:
    print ('MULTADO! voce ultrapassou o limite que é de 80km/h')
    multa = (velocidade-80)*7
    print (f'voce tem que pagar a multa de {multa:.2f}')
else:
    print ('tenha um bom dia, dirija com segurança!')
print ('-=-=-=-=-=-FIM!-=-=-=-=-=--=')