peso = float (input ('Digite seu peso: (Kg)'))
altura = float (input('digite sua altura:'))
imc = peso / (altura ** 2)
print (f'o imc dessa pessoa é {imc:.2f}.')
if imc < 18.5:
    print ('voce está ABAIXO DO PESO.')
elif imc > 18.5 and imc < 25:
    print ('voce está no peso IDEAL.')
elif imc > 25 and  imc < 30:
    print ('voce esta com SOBREPESO.')
elif imc > 30 and imc < 40:
    print ('voce está com OBESIDADE.')
elif imc > 40:
    print ('voce está com OBESIDADE MÓBIDADE')
print ('======FIM======')