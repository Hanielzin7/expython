print ('\033[30m=============Lojas Haniel´s==============')
preço = float (input('Preço das compras:'))
print ('''FORMAS DE PAGAMENTOS:
 [ 1 ] Á VISTA  DINHEIRO/CHEQUE
 [ 2 ] Á VISTA NO CARTÃO
 [ 3 ] 2X NO CARTÃO
 [ 4 ] 3X NO CARTÃO''')
opção = int (input('SUA OPÇÃO:'))
if opção == 1:
    total = preço - (preço * 10/100)
    print(f'sua compra de R${preço} vai te custar R${total} no final.')
elif opção == 2:
    total = preço - (preço * 5/100)
    print(f'sua compra de R${preço} vai te custar R${total} no final.')
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'sua parcela de 2x vai te custar {parcela}.')

    print(f'sua compra de R${preço} vai te custar R${total} no final.')

elif opção == 4:
    total = preço
    parcelas = int (input ('quantas parcelas?'))
    parcela = total / parcelas
    print (f'sua parcela de {parcelas}x vai te custar {parcela}.')
    print (f'sua compra de R${preço} vai te custar R${total} no final.')
else:
    print ('OPÇÃO INVÁLIDA, TENTE NOVAMENTE.')
print ('========FIM=======')