from datetime import date

atual = date.today().year
nascimento = int (input('\033[34mano de nascimento:\033[m'))
idade = atual - nascimento
sexo = int ( input('''qual é o seu sexo?

[1]Homem
[2]Mulher'''))
if sexo == 1:

    print (f'\033[33mquem nasceu no ano {nascimento} tem {idade} anos em {atual}\033[m.')
    if idade == 18:
        print ('\033[34mVOCÊ PRECISA IMEDIATAMENTE SE APRESENTAR AS FORÇAS ARMADAS!')
    if idade < 18:
        saldo = idade - 18
        print(f'\033[32mVoce ainda NÃO tem 18 anos,Ainda faltam {saldo} anos para seu alistamento ')
        print(f'seu alistamento vai ser em {atual + saldo }')
    if idade > 18:
        saldo = idade - 18
        print (f'\033[31mVoce já deveria se alistado há {saldo} anos ')
        print(f'seu alistamento foi em {atual - saldo}')
else:
    print ('O alistamento obrigatório não é para mulheres.')