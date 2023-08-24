#FORMATAÇÕES
nome = input('Qual seu nome?:')
print('Praze em te conhecer {:20}!'.format(nome), end = ' ')
print('Praze em te conhecer {:>20}!'.format(nome))
print('Praze em te conhecer {:<20}!'.format(nome))
print('Praze em te conhecer {:^20}!'.format(nome))
print('Praze em te conhecer {:-^20}!'.format(nome))