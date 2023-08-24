largura = float(input('Qual a largura da sua parede?'))
altura = float(input('Qual a largura da sua parede?'))
m = float(largura*altura)
print('Sua parede tem {} m²\n Para pintar ela você vai precisar de {} litros de tinta'.format(m, m/2))