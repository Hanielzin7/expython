distancia = float(input('qual é a distancia da sua viajem?'))
print (f'voce está prestes a começar uma viajem de {distancia}km.')
if distancia <= 200:

    preço = distancia * 0.50

else:

    preço = distancia * 0.45

print (f'e o preço da sua passagem será: R${preço:.2f}')