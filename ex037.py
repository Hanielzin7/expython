num = int (input ('digite um número qualquer:'))
print ('''\033[4;33m escolha  a base da conversão:\033[4;33m\033[34m
1] Binário
2] Octal
3] Hexadecimal\033[34m

''')
opção = int (input ('\033[31m SUA OPÇÃO:\033[m'))
if opção == 1:
    print (f'o  numero \033[30m{num}\033[m em binário vira \033[30m{bin(num)[2:]}\033[m')
elif opção == 2:
    print (f'o numero \033[30m{num}\033[m convertido para octal vira \033[30m{oct(num)[2:]}\033[m')
elif opção == 3:
    print (f'o numero \033[30m{num}\033[m convertido para hexadecimal vira \033[30m{hex(num)[2:]}\033[m')
else:
    print ('\033[7mOPÇÃO INVÁLIDA')
