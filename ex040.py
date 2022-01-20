n1 = float (input('digite a primeira nota:'))
n2 = float (input ('digite a segunda nota:'))
nota = (n1+n2)/2
print (f'a sua nota foi de {nota}!')
if nota >= 7.0:
    print ('PARABENS voce foi APROVADO(A)')
elif nota <= 5.0:
    print ('VOCÊ foi REPROVADO!')
else:
    print ('VOCÊ ficou de RECUPERAÇÃO!')