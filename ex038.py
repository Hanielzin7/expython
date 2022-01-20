import time
v1 = int (input ('digite um valor:'))
v2 = int (input ('digite outro valor:'))
print ('analisando...')
time.sleep(3)
if v1 > v2:
    print (f'{v1} é maior que {v2}')
elif v2 > v1:
    print (f'{v2} é maior que {v1}')
elif v1 == v2 or v2 == v1:
    print ('os dois valores são IGUAIS!')