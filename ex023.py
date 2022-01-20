num = int (input('informe 4 numeros:'))
u = num //1 % 10
d = num //10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print (f'analisando um numero {num}')
print (f'a unidade é:{u}')
print (f'a dezena é:{d}')
print (f'a centena é:{c}')
print (f'a unidade de milhar é: {m}')