real = float(input('Digite aqui o valor a ser convertido R$'))
dolar = float(real/4.90)
print('='*10)
print('Valor em RS{:.1f}, valor convertido para dolar ${:.1f}'.format(real, dolar))
print('='*10)