import math

an = float(input('qual é o grau?'))
seno = math.sin(math.radians(an))
print(f'o angulo {an} tem o seno de {seno:.2f} ')
co = math.cos(math.radians(an))
print(f'o cosseno de {an} é de {co:.2f}')
tangente = math.tan(math.radians(an))
print(f'o tagente de {an} é {tangente:.2f}')
