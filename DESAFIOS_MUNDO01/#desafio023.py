n=(int(input('Digite um numero entre 0 a 9999: ')))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print ('Analisando seu numero .............')
print('A unidade do seu numero é {}'.format(u))
print('A dezena é {}'.format(d))
print('A centena é {}'.format(c))
print('O milhar é {}'.format(m))
