ano = int(input('Digite aqui o ano que direi se ele é bissexto ou não '))
b = ano % 4 
if b == 0: 
    print('O ano {} é bissexto!'.format(ano))
else: 
    print('O ano {} não é bissexto'.format(ano)) 