import math
an = float(input('Digite o valor aqui:  '))
seno = math.sin(math.radians(an))
co = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('o Seno é de {:.2f} o cosseno é de {:.2f} e a tangente é de {:.2f}'.format(seno, co, tan))