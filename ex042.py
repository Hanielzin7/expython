print ('=*-'* 20)
print ('ANALISADOR DE TRIANGULO!')
print ('=*-'* 20)
r1 = float (input ('digite um segmento:'))
r2 = float (input ('digite um segmento:'))
r3 = float (input ('digite um segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +  r2:
    print ('os segmentos podem formar um triangulo',end= '')
    if r1 == r2 == r3:
        print ('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print ('ESCALENO!')
    else:
        print ('ISÓCELES!')
else:
    print ('os segmentos NÃO podem formar um triangulo!')