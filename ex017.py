import math
co = float (input('comprimento do cateto oposto:'))
ca = float (input('comprimento do cateto adjescente:'))
hi = math.hypot(co,ca)
print (f'a hipotenusa vai medir {hi:.2f}')