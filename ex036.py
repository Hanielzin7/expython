casa = float (input ('qual é o preço da casa?'))
salario = float (input ('salario do comprador:'))
anos = int (input ('quantos anos voce quer financiar:'))
prestação = casa / (anos * 12)
minimo = salario * 30/100
print (f'para pagar uma casa de R${casa:.2f} em {anos} anos', end=(''))
print (f' a prestação será de R${prestação:.2f}')
if prestação <= minimo:
    print('emprestimo CONCEDIDO COM SUCESSO!')
else:
    print ('emprestimo NEGADO!')