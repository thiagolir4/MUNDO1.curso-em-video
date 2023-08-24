import random
numero = ['0', '1', '2', '3', '4', '5']
escolhido = random.choice(numero)
n = input('Digite aqui o numero que você acha que vai ser o escolhido entre 0 e 5 ... ')
if n == escolhido:
    print('PARABENS VOCÊ ACERTOU!!')
else: 
    print('TENTE NOVAMENTE .... o numero escolhido era {}'.format(escolhido))