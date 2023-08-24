#maneira normal sem biblioteca
#co = float(input('Comprimento do cateto oposto:  '))
#ca = float(input('Comprimento do cateto adjacente:  '))
#hi = (co ** 2 + ca **2) ** (1/2)
#print('A Hipotenosa vai medir {:.2f}'.format(hi))


#jeito com importação da math 
import math
co = float(input('Comprimento do cateto oposto:  '))
ca = float(input('Comprimento do cateto adjacente:  '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))