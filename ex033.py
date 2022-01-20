a = int(input('digite um valor'))
b = int(input('digite um valor'))
c = int(input('digite um valor'))
#verificando quem é o menor
menor = a

if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#verificando qual é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print (f'o menor valor é {menor}')
print (f'o maior valor é {maior}')

