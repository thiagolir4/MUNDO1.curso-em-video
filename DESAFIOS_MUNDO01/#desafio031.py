km = float(input('Digite aqui quantos km tem sua viagem '))
kmp = km * 0.5
kmc = km * 0.45
if km <= 200:
    print('Sua passagem vai ficar R${:.2f}'.format(kmp))
else:
    print('Sua passagem vai ficar R${:.2f}'.format(kmc))