salario = float(input('qual é o salario?'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'quem ganhava {salario}agora ganha {novo}')
