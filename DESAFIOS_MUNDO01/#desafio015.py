d = float(input('Quantos dias o carro ficou alugado?'))
km = float(input('Quantos KM ele rodou?'))
pago = (d*60) + (km * 0.15)
print('O valor do aluguel do carro final foi de R${:.2f}'.format(pago))